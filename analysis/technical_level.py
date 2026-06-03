"""
Расчёт коэффициента технического уровня (КТУ) по методу аддитивной свёртки.
Для каждого показателя вычисляется q_i = значение/эталон (прямой) или эталон/значение (обратный).
T = sum(w_i * q_i)
"""

from dataclasses import dataclass


@dataclass
class Indicator:
    label: str       # human-readable name
    weight: float
    q_value: float   # relative value (vs reference)
    contribution: float  # w_i * q_i


@dataclass
class KTUResult:
    class_name: str
    object_name: str
    indicators: list  # list of Indicator
    total_T: float


# ---------- Reference values (эталон) ----------
# Sources: MLT-0.25, 1N4148, КТ315Б, NE555, DT-830B, ЕПСН-25, FR4 70×50mm
REFERENCE = {
    "Resistor": {
        "power_w":          {"ref": 0.25, "inverse": False, "weight": 0.35, "label": "Мощность (Вт)"},
        "accuracy_percent": {"ref": 5.0,  "inverse": True,  "weight": 0.35, "label": "Точность (%)"},
        "price_rub":        {"ref": 5.0,  "inverse": True,  "weight": 0.30, "label": "Цена (руб)"},
    },
    "Capacitor": {
        "working_voltage_v": {"ref": 50.0,    "inverse": False, "weight": 0.45, "label": "Напряжение (В)"},
        "capacitance_f":     {"ref": 0.1e-6,  "inverse": False, "weight": 0.25, "label": "Ёмкость (Ф)"},
        "price_rub":         {"ref": 3.0,     "inverse": True,  "weight": 0.30, "label": "Цена (руб)"},
    },
    "IntegratedCircuit": {
        "supply_voltage_v": {"ref": 5.0,  "inverse": False, "weight": 0.40, "label": "Напряжение пит. (В)"},
        "price_rub":        {"ref": 15.0, "inverse": True,  "weight": 0.60, "label": "Цена (руб)"},
    },
    "Transistor": {
        "max_current_a": {"ref": 0.1,  "inverse": False, "weight": 0.35, "label": "Макс. ток (А)"},
        "voltage_v":     {"ref": 40.0, "inverse": False, "weight": 0.35, "label": "Напряжение (В)"},
        "price_rub":     {"ref": 5.0,  "inverse": True,  "weight": 0.30, "label": "Цена (руб)"},
    },
    "Diode": {
        "max_current_a":    {"ref": 0.3, "inverse": False, "weight": 0.35, "label": "Макс. ток (А)"},
        "forward_voltage_v":{"ref": 0.7, "inverse": True,  "weight": 0.35, "label": "Прямое напр. (В)"},
        "price_rub":        {"ref": 3.0, "inverse": True,  "weight": 0.30, "label": "Цена (руб)"},
    },
    "Board": {
        "size_mm":   {"ref": 3500.0, "inverse": False, "weight": 0.35, "label": "Площадь (мм²)"},
        "layer_type":{"ref": 1.0,    "inverse": False, "weight": 0.35, "label": "Многослойность"},
        "price_rub": {"ref": 40.0,   "inverse": True,  "weight": 0.30, "label": "Цена (руб)"},
    },
    "Connector": {
        "contact_count": {"ref": 40.0, "inverse": False, "weight": 0.40, "label": "Контакты (шт)"},
        "mount_th":      {"ref": 1.0,  "inverse": False, "weight": 0.30, "label": "Сквозной монтаж"},
        "price_rub":     {"ref": 15.0, "inverse": True,  "weight": 0.30, "label": "Цена (руб)"},
    },
    "SolderingEquipment": {
        "power_w":       {"ref": 25.0,  "inverse": False, "weight": 0.30, "label": "Мощность (Вт)"},
        "heating_temp_c":{"ref": 300.0, "inverse": False, "weight": 0.30, "label": "Температура (°C)"},
        "price_rub":     {"ref": 350.0, "inverse": True,  "weight": 0.40, "label": "Цена (руб)"},
    },
    "MeasuringInstrument": {
        "accuracy_percent": {"ref": 1.0,   "inverse": True,  "weight": 0.40, "label": "Точность (%)"},
        "range_value":      {"ref": 600.0, "inverse": False, "weight": 0.30, "label": "Диапазон"},
        "price_rub":        {"ref": 500.0, "inverse": True,  "weight": 0.30, "label": "Цена (руб)"},
    },
    "Prototyping": {
        "service_price_rub":   {"ref": 5000.0, "inverse": True,  "weight": 0.35, "label": "Цена услуги (руб)"},
        "avg_execution_days":  {"ref": 7.0,    "inverse": True,  "weight": 0.25, "label": "Срок (дней)"},
        "circuit_design":      {"ref": 1.0,    "inverse": False, "weight": 0.20, "label": "Разработка схем"},
        "prototype_assembly":  {"ref": 1.0,    "inverse": False, "weight": 0.20, "label": "Сборка прототипа"},
    },
    "Repair": {
        "service_price_rub":    {"ref": 1500.0, "inverse": True,  "weight": 0.30, "label": "Цена услуги (руб)"},
        "avg_execution_days":   {"ref": 3.0,    "inverse": True,  "weight": 0.30, "label": "Срок (дней)"},
        "fault_diagnosis":      {"ref": 1.0,    "inverse": False, "weight": 0.20, "label": "Диагностика"},
        "component_replacement":{"ref": 1.0,    "inverse": False, "weight": 0.20, "label": "Замена компонентов"},
    },
    "TechnicalDocumentation": {
        "service_price_rub":  {"ref": 3000.0, "inverse": True,  "weight": 0.30, "label": "Цена услуги (руб)"},
        "avg_execution_days": {"ref": 5.0,    "inverse": True,  "weight": 0.30, "label": "Срок (дней)"},
        "circuit_preparation":{"ref": 1.0,    "inverse": False, "weight": 0.20, "label": "Подготовка схем"},
        "bom_creation":       {"ref": 1.0,    "inverse": False, "weight": 0.20, "label": "Создание BOM"},
    },
    "EngineerConsultation": {
        "service_price_rub":  {"ref": 1000.0, "inverse": True,  "weight": 0.30, "label": "Цена услуги (руб)"},
        "avg_execution_days": {"ref": 1.0,    "inverse": True,  "weight": 0.25, "label": "Срок (дней)"},
        "component_selection":{"ref": 1.0,    "inverse": False, "weight": 0.25, "label": "Подбор компонентов"},
        "circuit_optimization":{"ref": 1.0,   "inverse": False, "weight": 0.20, "label": "Оптимизация схем"},
    },
    "Hobbyist": {
        "min_order_rub":                  {"ref": 500.0, "inverse": True,  "weight": 0.40, "label": "Мин. заказ (руб)"},
        "component_selection_assistance": {"ref": 1.0,   "inverse": False, "weight": 0.30, "label": "Подбор компонентов"},
        "device_assembly_setup":          {"ref": 1.0,   "inverse": False, "weight": 0.30, "label": "Сборка/настройка"},
    },
    "ServiceCenter": {
        "min_order_rub":             {"ref": 2000.0, "inverse": True,  "weight": 0.40, "label": "Мин. заказ (руб)"},
        "spare_parts_supply":        {"ref": 1.0,    "inverse": False, "weight": 0.30, "label": "Поставка запчастей"},
        "urgent_component_delivery": {"ref": 1.0,    "inverse": False, "weight": 0.30, "label": "Срочная доставка"},
    },
    "ElectronicsManufacturer": {
        "min_order_rub":    {"ref": 10000.0, "inverse": True,  "weight": 0.40, "label": "Мин. заказ (руб)"},
        "wholesale_supply": {"ref": 1.0,     "inverse": False, "weight": 0.30, "label": "Оптовые поставки"},
        "contract_assembly":{"ref": 1.0,     "inverse": False, "weight": 0.30, "label": "Контрактная сборка"},
    },
}


def _get_value(obj, attr: str):
    """Extract numeric value from object attribute; handle bool -> float."""
    val = getattr(obj, attr)
    if isinstance(val, bool):
        return 1.0 if val else 0.0
    return float(val)


def _board_layer_type(board) -> float:
    return 1.0 if "multi" in board.type.lower() else 0.0


def _connector_mount_th(connector) -> float:
    return 1.0 if "through" in connector.mounting_method.lower() else 0.0


def compute_ktu(obj, object_name: str) -> KTUResult:
    class_name = type(obj).__name__
    spec = REFERENCE.get(class_name)
    if spec is None:
        raise ValueError(f"No reference defined for class '{class_name}'")

    indicators = []
    for attr, cfg in spec.items():
        # Special derived attrs
        if attr == "layer_type":
            value = _board_layer_type(obj)
        elif attr == "mount_th":
            value = _connector_mount_th(obj)
        else:
            value = _get_value(obj, attr)

        ref = cfg["ref"]
        w = cfg["weight"]
        label = cfg["label"]

        if cfg["inverse"]:
            # smaller is better: q = ref / value (avoid division by zero)
            q = ref / value if value != 0 else 0.0
        else:
            # larger is better: q = value / ref
            q = value / ref if ref != 0 else 0.0

        indicators.append(Indicator(label=label, weight=w, q_value=q, contribution=w * q))

    total_T = sum(ind.contribution for ind in indicators)
    return KTUResult(class_name=class_name, object_name=object_name, indicators=indicators, total_T=total_T)

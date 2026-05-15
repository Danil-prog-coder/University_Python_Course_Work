"""
Конфигурация показателей для каждой модели.

Структура каждой записи:
  weight  — вес показателя (сумма по классу = 1.0)
  inverse — True, если меньше = лучше (цена, погрешность, время)
  binary  — True, если поле булево (0/1), нормализуется напрямую

Примечание: строковые поля (type, material, package, pricing_condition,
measurement_range, accuracy) в радиальную диаграмму не включаются —
они отображаются как метки.
"""

INDICATOR_CONFIG: dict[str, dict[str, dict]] = {

    # ------------------------------------------------------------------
    # 2.5.1  Электронные компоненты
    # ------------------------------------------------------------------
    "Resistor": {
        # Мощность важнее цены: определяет применимость в силовых цепях
        "power_w":          {"weight": 0.35, "inverse": False, "binary": False},
        # Точность (допуск) — ключевой параметр качества; чем меньше, тем лучше
        "accuracy_percent": {"weight": 0.35, "inverse": True,  "binary": False},
        "price_rub":        {"weight": 0.30, "inverse": True,  "binary": False},
    },

    "Capacitor": {
        # Рабочее напряжение критично: превышение → пробой
        "capacitance_f":     {"weight": 0.25, "inverse": False, "binary": False},
        "working_voltage_v": {"weight": 0.45, "inverse": False, "binary": False},
        "price_rub":         {"weight": 0.30, "inverse": True,  "binary": False},
    },

    "IntegratedCircuit": {
        # Для ИС ключевой числовой параметр — напряжение питания (совместимость)
        # Цена имеет высокий вес: разброс цен на ИС очень велик
        "supply_voltage_v": {"weight": 0.40, "inverse": False, "binary": False},
        "price_rub":        {"weight": 0.60, "inverse": True,  "binary": False},
    },

    "Transistor": {
        # Ток и напряжение определяют класс мощности — оба одинаково важны
        "max_current_a": {"weight": 0.35, "inverse": False, "binary": False},
        "voltage_v":     {"weight": 0.35, "inverse": False, "binary": False},
        "price_rub":     {"weight": 0.30, "inverse": True,  "binary": False},
    },

    "Diode": {
        # Максимальный ток — главный параметр выпрямительного диода
        # Прямое напряжение инверсное: меньше → меньше потери на нагрев
        "max_current_a":     {"weight": 0.40, "inverse": False, "binary": False},
        "forward_voltage_v": {"weight": 0.30, "inverse": True,  "binary": False},
        "price_rub":         {"weight": 0.30, "inverse": True,  "binary": False},
    },

    # ------------------------------------------------------------------
    # 2.5.2  Комплектующие
    # ------------------------------------------------------------------
    "Board": {
        # Числовых качественных параметров нет — только цена
        "price_rub": {"weight": 1.00, "inverse": True, "binary": False},
    },

    "Connector": {
        # Количество контактов — основная характеристика разъёма
        "contact_count": {"weight": 0.55, "inverse": False, "binary": False},
        "price_rub":     {"weight": 0.45, "inverse": True,  "binary": False},
    },

    # ------------------------------------------------------------------
    # 2.5.3  Паяльное оборудование и измерительные приборы
    # ------------------------------------------------------------------
    "SolderingEquipment": {
        # Мощность и температура определяют возможности инструмента
        # Цена имеет наибольший вес: диапазон от 300 до 30 000 руб.
        "power_w":        {"weight": 0.30, "inverse": False, "binary": False},
        "heating_temp_c": {"weight": 0.30, "inverse": False, "binary": False},
        "price_rub":      {"weight": 0.40, "inverse": True,  "binary": False},
    },

    "MeasuringInstrument": {
        # accuracy и measurement_range — строки, не числа; только цена числовая
        "price_rub": {"weight": 1.00, "inverse": True, "binary": False},
    },

    # ------------------------------------------------------------------
    # 2.5.4  Услуги прототипирования
    # ------------------------------------------------------------------
    "Prototyping": {
        "circuit_design":     {"weight": 0.25, "inverse": False, "binary": True},
        "prototype_assembly": {"weight": 0.25, "inverse": False, "binary": True},
        "service_price_rub":  {"weight": 0.25, "inverse": True,  "binary": False},
        "avg_execution_days": {"weight": 0.25, "inverse": True,  "binary": False},
    },

    # ------------------------------------------------------------------
    # 2.5.5  Серийное производство
    # ------------------------------------------------------------------
    "MassProduction": {
        "board_assembly":     {"weight": 0.25, "inverse": False, "binary": True},
        "product_testing":    {"weight": 0.25, "inverse": False, "binary": True},
        "service_price_rub":  {"weight": 0.25, "inverse": True,  "binary": False},
        "avg_execution_days": {"weight": 0.25, "inverse": True,  "binary": False},
    },

    # ------------------------------------------------------------------
    # 2.5.6  Дополнительные услуги
    # ------------------------------------------------------------------
    "TechnicalDocumentation": {
        "circuit_preparation": {"weight": 0.25, "inverse": False, "binary": True},
        "bom_creation":        {"weight": 0.25, "inverse": False, "binary": True},
        "service_price_rub":   {"weight": 0.25, "inverse": True,  "binary": False},
        "avg_execution_days":  {"weight": 0.25, "inverse": True,  "binary": False},
    },

    "EngineerConsultation": {
        "component_selection":  {"weight": 0.25, "inverse": False, "binary": True},
        "circuit_optimization": {"weight": 0.25, "inverse": False, "binary": True},
        "service_price_rub":    {"weight": 0.25, "inverse": True,  "binary": False},
        "avg_execution_days":   {"weight": 0.25, "inverse": True,  "binary": False},
    },

    # ------------------------------------------------------------------
    # 2.5.7  Работа с клиентами
    # ------------------------------------------------------------------
    "Hobbyist": {
        # Наличие услуг важно, но минимальная сумма заказа — барьер входа
        "component_selection_assistance": {"weight": 0.30, "inverse": False, "binary": True},
        "device_assembly_setup":          {"weight": 0.30, "inverse": False, "binary": True},
        "min_order_rub":                  {"weight": 0.40, "inverse": True,  "binary": False},
    },

    "ServiceCenter": {
        "spare_parts_supply":        {"weight": 0.30, "inverse": False, "binary": True},
        "urgent_component_delivery": {"weight": 0.30, "inverse": False, "binary": True},
        "min_order_rub":             {"weight": 0.40, "inverse": True,  "binary": False},
    },

    "ElectronicsManufacturer": {
        "wholesale_supply":  {"weight": 0.30, "inverse": False, "binary": True},
        "contract_assembly": {"weight": 0.30, "inverse": False, "binary": True},
        "min_order_rub":     {"weight": 0.40, "inverse": True,  "binary": False},
    },
}

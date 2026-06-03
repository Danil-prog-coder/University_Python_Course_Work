"""
Точка входа — магазин электронных комплектующих.
Демонстрирует создание объектов всех классов, вывод сводной информации,
анализ оптимальной закупки (линейное программирование) и
диаграммы КТУ (радарные / столбчатые).

Использование:
    python main.py                                  # демо-данные
    python main.py --file input.json                # данные из JSON-файла
    python main.py --chart radar                    # все диаграммы КТУ (радарные)
    python main.py --chart bar --category tools     # столбчатая для инструментов
    python main.py --chart radar --save-dir ./out   # сохранить PNG
"""

import argparse
import json
import sys
from pathlib import Path

from models import (
    Resistor, Capacitor, IntegratedCircuit, Transistor, Diode,
    Board, Connector,
    SolderingEquipment, MeasuringInstrument,
    Prototyping, Repair,
    TechnicalDocumentation, EngineerConsultation,
    Hobbyist, ServiceCenter, ElectronicsManufacturer,
)
from classes import (
    ElectronicComponents, Components, Tools,
    Services, AdditionalServices,
    CustomerRelations, MassProduction,
)
from analysis import OptimalPurchaseAnalysis, Supplier
from analysis.technical_level import compute_ktu
from visualization import show_category


def print_section(title: str) -> None:
    print(f"\n{'=' * 50}")
    print(f"  {title}")
    print('=' * 50)


# ---------- Demo objects (shared by text demo AND chart demo) ----------

def _make_demo_objects() -> dict:
    resistor   = Resistor(resistance_ohm=470.0, power_w=0.5, accuracy_percent=1.0, price_rub=8.0)
    capacitor  = Capacitor(capacitance_f=100e-6, working_voltage_v=25.0, type="electrolytic", price_rub=12.0)
    ic         = IntegratedCircuit(type_purpose="controller", supply_voltage_v=5.0, package="DIP", price_rub=20.0)
    transistor = Transistor(type="NPN", max_current_a=0.6, voltage_v=40.0, price_rub=8.0)
    diode      = Diode(type="rectifier", forward_voltage_v=0.7, max_current_a=1.0, price_rub=5.0)

    board     = Board(type="multilayer", material="FR4", size="100x80 мм", size_mm=8000.0, price_rub=120.0)
    connector = Connector(type="pin header", contact_count=40, mounting_method="through-hole", price_rub=15.0)

    soldering = SolderingEquipment(power_w=40.0, heating_temp_c=450.0, type="station", price_rub=1200.0)
    meter     = MeasuringInstrument(type="multimeter", accuracy="0.5%", measurement_range="0–600 В / 0–10 А",
                                    accuracy_percent=0.5, range_value=600.0, price_rub=800.0)

    prototyping   = Prototyping(service_price_rub=4500.0, avg_execution_days=5.0, circuit_design=True, prototype_assembly=True)
    repair        = Repair(service_price_rub=1200.0, avg_execution_days=2.0, fault_diagnosis=True, component_replacement=True)
    doc           = TechnicalDocumentation(service_price_rub=2500.0, avg_execution_days=4.0, circuit_preparation=True, bom_creation=True)
    consultation  = EngineerConsultation(service_price_rub=800.0, avg_execution_days=1.0, component_selection=True, circuit_optimization=True)

    hobbyist     = Hobbyist(min_order_rub=300.0, component_selection_assistance=True, device_assembly_setup=True)
    svc_center   = ServiceCenter(min_order_rub=1500.0, spare_parts_supply=True, urgent_component_delivery=True)
    manufacturer = ElectronicsManufacturer(min_order_rub=8000.0, wholesale_supply=True, contract_assembly=False)

    return {
        "resistor": resistor, "capacitor": capacitor, "ic": ic,
        "transistor": transistor, "diode": diode,
        "board": board, "connector": connector,
        "soldering": soldering, "meter": meter,
        "prototyping": prototyping, "repair": repair,
        "doc": doc, "consultation": consultation,
        "hobbyist": hobbyist, "svc_center": svc_center, "manufacturer": manufacturer,
    }


_DEMO = None


def get_demo() -> dict:
    global _DEMO
    if _DEMO is None:
        _DEMO = _make_demo_objects()
    return _DEMO


# ---------- Text demos ----------

def demo_electronic_components() -> None:
    print_section("Электронные компоненты")
    d = get_demo()
    ec = ElectronicComponents(
        resistors=d["resistor"], capacitors=d["capacitor"],
        integrated_circuits=d["ic"], transistors=d["transistor"], diodes=d["diode"],
    )
    print(f"Резистор:    {ec.resistors.resistance_ohm} Ом, {ec.resistors.power_w} Вт, ±{ec.resistors.accuracy_percent}%,  {ec.resistors.price_rub} руб.")
    print(f"Конденсатор: {ec.capacitors.capacitance_f * 1e6:.0f} мкФ, {ec.capacitors.working_voltage_v} В, тип: {ec.capacitors.type},  {ec.capacitors.price_rub} руб.")
    print(f"Микросхема:  {ec.integrated_circuits.type_purpose}, {ec.integrated_circuits.supply_voltage_v} В, корпус: {ec.integrated_circuits.package},  {ec.integrated_circuits.price_rub} руб.")
    print(f"Транзистор:  {ec.transistors.type}, I_max={ec.transistors.max_current_a} А, U={ec.transistors.voltage_v} В,  {ec.transistors.price_rub} руб.")
    print(f"Диод:        {ec.diodes.type}, U_пр={ec.diodes.forward_voltage_v} В, I_max={ec.diodes.max_current_a} А,  {ec.diodes.price_rub} руб.")


def demo_components() -> None:
    print_section("Комплектующие (платы и разъёмы)")
    d = get_demo()
    comp = Components(boards=d["board"], connectors=d["connector"])
    print(f"Плата:   {comp.boards.type}, материал: {comp.boards.material}, размер: {comp.boards.size},  {comp.boards.price_rub} руб.")
    print(f"Разъём:  {comp.connectors.type}, контактов: {comp.connectors.contact_count}, монтаж: {comp.connectors.mounting_method},  {comp.connectors.price_rub} руб.")


def demo_tools() -> None:
    print_section("Инструменты")
    d = get_demo()
    tools = Tools(soldering_equipment=d["soldering"], measuring_instruments=d["meter"])
    print(f"Паяльное: {tools.soldering_equipment.type}, {tools.soldering_equipment.power_w} Вт, до {tools.soldering_equipment.heating_temp_c} °C,  {tools.soldering_equipment.price_rub} руб.")
    print(f"Прибор:   {tools.measuring_instruments.type}, точность: {tools.measuring_instruments.accuracy}, диапазон: {tools.measuring_instruments.measurement_range},  {tools.measuring_instruments.price_rub} руб.")


def demo_services() -> None:
    print_section("Услуги")
    d = get_demo()
    services = Services(prototyping=d["prototyping"], repair=d["repair"])
    print(f"Прототипирование — цена: {services.prototyping.service_price_rub} руб., срок: {services.prototyping.avg_execution_days} дн., разработка схем: {services.prototyping.circuit_design}, сборка прототипа: {services.prototyping.prototype_assembly}")
    print(f"Ремонт           — цена: {services.repair.service_price_rub} руб., срок: {services.repair.avg_execution_days} дн., диагностика: {services.repair.fault_diagnosis}, замена компонентов: {services.repair.component_replacement}")


def demo_additional_services() -> None:
    print_section("Дополнительные услуги")
    d = get_demo()
    add = AdditionalServices(technical_documentation=d["doc"], engineer_consultations=d["consultation"])
    print(f"Техдокументация  — цена: {add.technical_documentation.service_price_rub} руб., срок: {add.technical_documentation.avg_execution_days} дн., подготовка схем: {add.technical_documentation.circuit_preparation}, создание BOM: {add.technical_documentation.bom_creation}")
    print(f"Консультации     — цена: {add.engineer_consultations.service_price_rub} руб., срок: {add.engineer_consultations.avg_execution_days} дн., подбор компонентов: {add.engineer_consultations.component_selection}, оптимизация схем: {add.engineer_consultations.circuit_optimization}")


def demo_customer_relations() -> None:
    print_section("Работа с клиентами")
    d = get_demo()
    cr = CustomerRelations(hobbyists=d["hobbyist"], service_centers=d["svc_center"], electronics_manufacturers=d["manufacturer"])
    print(f"Радиолюбители    — мин. заказ: {cr.hobbyists.min_order_rub} руб., подбор компонентов: {cr.hobbyists.component_selection_assistance}, сборка/настройка: {cr.hobbyists.device_assembly_setup}")
    print(f"Сервисные центры — мин. заказ: {cr.service_centers.min_order_rub} руб., поставка запчастей: {cr.service_centers.spare_parts_supply}, срочная доставка: {cr.service_centers.urgent_component_delivery}")
    print(f"Производители    — мин. заказ: {cr.electronics_manufacturers.min_order_rub} руб., оптовые поставки: {cr.electronics_manufacturers.wholesale_supply}, контрактная сборка: {cr.electronics_manufacturers.contract_assembly}")


def demo_mass_production() -> None:
    print_section("Серийное производство")
    mp = MassProduction(board_assembly=True, product_testing=True)
    print(f"Сборка плат: {mp.board_assembly}, тестирование изделий: {mp.product_testing}")


# ---------- KTU Charts ----------

CATEGORIES = {
    "electronic_components": {
        "title": "Электронные компоненты",
        "items": lambda d: [
            compute_ktu(d["resistor"],   "Резистор"),
            compute_ktu(d["capacitor"],  "Конденсатор"),
            compute_ktu(d["ic"],         "Микросхема"),
            compute_ktu(d["transistor"], "Транзистор"),
            compute_ktu(d["diode"],      "Диод"),
        ],
    },
    "components": {
        "title": "Комплектующие (платы и разъёмы)",
        "items": lambda d: [
            compute_ktu(d["board"],     "Плата"),
            compute_ktu(d["connector"], "Разъём"),
        ],
    },
    "tools": {
        "title": "Инструменты",
        "items": lambda d: [
            compute_ktu(d["soldering"], "Паяльная станция"),
            compute_ktu(d["meter"],     "Мультиметр"),
        ],
    },
    "services": {
        "title": "Услуги",
        "items": lambda d: [
            compute_ktu(d["prototyping"], "Прототипирование"),
            compute_ktu(d["repair"],      "Ремонт"),
        ],
    },
    "additional_services": {
        "title": "Дополнительные услуги",
        "items": lambda d: [
            compute_ktu(d["doc"],          "Техдокументация"),
            compute_ktu(d["consultation"], "Консультация"),
        ],
    },
    "customer_relations": {
        "title": "Работа с клиентами",
        "items": lambda d: [
            compute_ktu(d["hobbyist"],     "Радиолюбитель"),
            compute_ktu(d["svc_center"],   "Сервисный центр"),
            compute_ktu(d["manufacturer"], "Производитель"),
        ],
    },
}


def demo_charts(chart_type: str = "radar", category: str = "all", save_dir: str | None = None) -> None:
    print_section(f"Диаграммы КТУ  (тип: {chart_type})")
    d = get_demo()

    if save_dir:
        Path(save_dir).mkdir(parents=True, exist_ok=True)

    keys = list(CATEGORIES.keys()) if category == "all" else [category]
    for key in keys:
        if key not in CATEGORIES:
            print(f"  Неизвестная категория: {key}. Доступные: {', '.join(CATEGORIES)}")
            continue
        cfg = CATEGORIES[key]
        results = cfg["items"](d)
        print(f"  {cfg['title']}")
        for r in results:
            print(f"    {r.object_name}: T = {r.total_T:.3f}")
        show_category(cfg["title"], results, chart_type=chart_type, save_dir=save_dir)


# ---------- Optimal purchase (unchanged) ----------

def load_purchase_data_from_file(path: str) -> dict:
    file = Path(path)
    if not file.exists():
        print(f"Ошибка: файл '{path}' не найден.", file=sys.stderr)
        sys.exit(1)
    try:
        with file.open(encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Ошибка разбора JSON: {e}", file=sys.stderr)
        sys.exit(1)

    required = {"category", "selling_price", "target_profit", "suppliers"}
    missing = required - data.keys()
    if missing:
        print(f"Ошибка: в файле отсутствуют поля: {', '.join(missing)}", file=sys.stderr)
        sys.exit(1)

    return data


def demo_optimal_purchase(file_path: str | None = None) -> None:
    print_section("Анализ оптимальной закупки (линейное программирование)")
    print("Задача: минимизировать суммарные затраты, обеспечив целевую прибыль.")
    print("Решатель: scipy.optimize.linprog (HiGHS) — методы highs, highs-ds, highs-ipm.")
    print()
    print("  min Z = sum(c_i * x_i)")
    print("  s.t.  sum((p - c_i) * x_i) >= target_profit")
    print("        0 <= x_i <= cap_i")
    print()

    if file_path:
        print(f"Источник данных: {file_path}")
        data = load_purchase_data_from_file(file_path)
        suppliers = [
            Supplier(name=s["name"], cost_per_unit=float(s["cost_per_unit"]), max_capacity=float(s["max_capacity"]))
            for s in data["suppliers"]
        ]
        category      = data["category"]
        selling_price = float(data["selling_price"])
        target_profit = float(data["target_profit"])
    else:
        print("Источник данных: встроенные демо-данные")
        suppliers = [
            Supplier(name="Поставщик А", cost_per_unit=85.0,  max_capacity=2000),
            Supplier(name="Поставщик Б", cost_per_unit=92.0,  max_capacity=1500),
            Supplier(name="Поставщик В", cost_per_unit=78.0,  max_capacity=1000),
        ]
        category      = "Электронные компоненты"
        selling_price = 120.0
        target_profit = 50_000.0

    result = OptimalPurchaseAnalysis(
        category=category, selling_price=selling_price,
        target_profit=target_profit, suppliers=suppliers,
    ).analyze()

    if not result.success:
        print("Задача не имеет допустимого решения.")
        print("Суммарной ёмкости поставщиков недостаточно для достижения целевой прибыли.")
        return

    print(f"Категория:       {result.category}")
    print(f"Цена продажи:    {result.selling_price:.2f} руб./ед.")
    print(f"Целевая прибыль: {result.target_profit:,.2f} руб.")
    print()

    cw  = [16, 10, 10, 14, 14]
    sep = "-" * (sum(cw) + len(cw) - 1)
    print(f"{'Поставщик':<{cw[0]}} {'Объём':>{cw[1]}} {'Цена/ед.':>{cw[2]}} {'Затраты':>{cw[3]}} {'Прибыль':>{cw[4]}}")
    print(sep)
    for sp in result.supplier_plan:
        print(f"{sp.name:<{cw[0]}} {sp.units:>{cw[1]}.1f} {sp.cost_per_unit:>{cw[2]}.2f} {sp.total_cost:>{cw[3]}.2f} {sp.contribution_to_profit:>{cw[4]}.2f}")
    print(sep)
    print(f"{'Итого':<{cw[0]}} {result.total_units:>{cw[1]}.1f} {'':>{cw[2]}} {result.total_cost:>{cw[3]}.2f} {result.actual_profit:>{cw[4]}.2f}")
    print()
    print(f"Выручка: {result.total_revenue:,.2f} руб.  |  Затраты: {result.total_cost:,.2f} руб.  |  Прибыль: {result.actual_profit:,.2f} руб.")
    print()

    print(f"{'Метод':<12} {'Статус':<10} {'Затраты, руб.':>16} {'Время, мс':>12}")
    print("-" * 52)
    for m in result.methods:
        cost_str = f"{m.total_cost:,.2f}" if m.total_cost is not None else "—"
        print(f"{m.method:<12} {'Успех' if m.success else 'Ошибка':<10} {cost_str:>16} {m.solve_time_ms:>12.4f}")


# ---------- CLI ----------

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Магазин электронных комплектующих — демонстрация системы")
    parser.add_argument("--file", "-f", metavar="PATH",
                        help="JSON-файл с параметрами закупки")
    parser.add_argument("--chart", choices=["radar", "bar"],
                        help="Тип диаграммы КТУ: radar или bar")
    parser.add_argument("--category", default="all",
                        choices=["all"] + list(CATEGORIES.keys()),
                        help="Категория для диаграммы (по умолчанию: all)")
    parser.add_argument("--save-dir", metavar="DIR",
                        help="Папка для сохранения PNG-диаграмм")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    print("Магазин электронных комплектующих — демонстрация системы")
    demo_electronic_components()
    demo_components()
    demo_tools()
    demo_services()
    demo_additional_services()
    demo_customer_relations()
    demo_mass_production()
    demo_optimal_purchase(file_path=args.file)

    if args.chart:
        demo_charts(chart_type=args.chart, category=args.category, save_dir=args.save_dir)

    print("\nГотово.")


if __name__ == "__main__":
    main()

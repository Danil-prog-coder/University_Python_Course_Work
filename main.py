"""
Точка входа — магазин электронных комплектующих.
Демонстрирует создание объектов всех классов, вывод сводной информации
и анализ оптимальной закупки методами линейного программирования.
"""

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


def print_section(title: str) -> None:
    print(f"\n{'=' * 50}")
    print(f"  {title}")
    print('=' * 50)


def demo_electronic_components() -> None:
    print_section("Электронные компоненты")

    resistor = Resistor(resistance_ohm=470.0, power_w=0.25, accuracy_percent=5.0)
    capacitor = Capacitor(capacitance_f=100e-6, working_voltage_v=25.0, type="electrolytic")
    ic = IntegratedCircuit(type_purpose="controller", supply_voltage_v=5.0, package="DIP")
    transistor = Transistor(type="NPN", max_current_a=0.6, voltage_v=40.0)
    diode = Diode(type="rectifier", forward_voltage_v=0.7, max_current_a=1.0)

    ec = ElectronicComponents(
        resistors=resistor,
        capacitors=capacitor,
        integrated_circuits=ic,
        transistors=transistor,
        diodes=diode,
    )

    print(f"Резистор:    {ec.resistors.resistance_ohm} Ом, {ec.resistors.power_w} Вт, ±{ec.resistors.accuracy_percent}%")
    print(f"Конденсатор: {ec.capacitors.capacitance_f * 1e6:.0f} мкФ, {ec.capacitors.working_voltage_v} В, тип: {ec.capacitors.type}")
    print(f"Микросхема:  {ec.integrated_circuits.type_purpose}, {ec.integrated_circuits.supply_voltage_v} В, корпус: {ec.integrated_circuits.package}")
    print(f"Транзистор:  {ec.transistors.type}, I_max={ec.transistors.max_current_a} А, U={ec.transistors.voltage_v} В")
    print(f"Диод:        {ec.diodes.type}, U_пр={ec.diodes.forward_voltage_v} В, I_max={ec.diodes.max_current_a} А")


def demo_components() -> None:
    print_section("Комплектующие (платы и разъёмы)")

    board = Board(type="multilayer", material="FR4", size="100x80 мм")
    connector = Connector(type="pin header", contact_count=40, mounting_method="through-hole")

    comp = Components(boards=board, connectors=connector)

    print(f"Плата:   {comp.boards.type}, материал: {comp.boards.material}, размер: {comp.boards.size}")
    print(f"Разъём:  {comp.connectors.type}, контактов: {comp.connectors.contact_count}, монтаж: {comp.connectors.mounting_method}")


def demo_tools() -> None:
    print_section("Инструменты")

    soldering = SolderingEquipment(power_w=40.0, heating_temp_c=450.0, type="station")
    meter = MeasuringInstrument(type="multimeter", accuracy="0.5%", measurement_range="0–600 В / 0–10 А")

    tools = Tools(soldering_equipment=soldering, measuring_instruments=meter)

    print(f"Паяльное: {tools.soldering_equipment.type}, {tools.soldering_equipment.power_w} Вт, до {tools.soldering_equipment.heating_temp_c} °C")
    print(f"Прибор:   {tools.measuring_instruments.type}, точность: {tools.measuring_instruments.accuracy}, диапазон: {tools.measuring_instruments.measurement_range}")


def demo_services() -> None:
    print_section("Услуги")

    prototyping = Prototyping(circuit_design=True, prototype_assembly=True)
    repair = Repair(fault_diagnosis=True, component_replacement=True)

    services = Services(prototyping=prototyping, repair=repair)

    print(f"Прототипирование — разработка схем: {services.prototyping.circuit_design}, сборка прототипа: {services.prototyping.prototype_assembly}")
    print(f"Ремонт           — диагностика: {services.repair.fault_diagnosis}, замена компонентов: {services.repair.component_replacement}")


def demo_additional_services() -> None:
    print_section("Дополнительные услуги")

    doc = TechnicalDocumentation(circuit_preparation=True, bom_creation=True)
    consultation = EngineerConsultation(component_selection=True, circuit_optimization=True)

    add = AdditionalServices(technical_documentation=doc, engineer_consultations=consultation)

    print(f"Техдокументация  — подготовка схем: {add.technical_documentation.circuit_preparation}, создание BOM: {add.technical_documentation.bom_creation}")
    print(f"Консультации     — подбор компонентов: {add.engineer_consultations.component_selection}, оптимизация схем: {add.engineer_consultations.circuit_optimization}")


def demo_customer_relations() -> None:
    print_section("Работа с клиентами")

    hobbyist = Hobbyist(component_selection_assistance=True, device_assembly_setup=True)
    service_center = ServiceCenter(spare_parts_supply=True, urgent_component_delivery=True)
    manufacturer = ElectronicsManufacturer(wholesale_supply=True, contract_assembly=False)

    cr = CustomerRelations(
        hobbyists=hobbyist,
        service_centers=service_center,
        electronics_manufacturers=manufacturer,
    )

    print(f"Радиолюбители    — подбор компонентов: {cr.hobbyists.component_selection_assistance}, сборка/настройка: {cr.hobbyists.device_assembly_setup}")
    print(f"Сервисные центры — поставка запчастей: {cr.service_centers.spare_parts_supply}, срочная доставка: {cr.service_centers.urgent_component_delivery}")
    print(f"Производители    — оптовые поставки: {cr.electronics_manufacturers.wholesale_supply}, контрактная сборка: {cr.electronics_manufacturers.contract_assembly}")


def demo_mass_production() -> None:
    print_section("Серийное производство")

    mp = MassProduction(board_assembly=True, product_testing=True)

    print(f"Сборка плат: {mp.board_assembly}, тестирование изделий: {mp.product_testing}")


def demo_optimal_purchase() -> None:
    print_section("Анализ оптимальной закупки (линейное программирование)")
    print("Задача: минимизировать суммарные затраты, обеспечив целевую прибыль.")
    print("Решатель: scipy.optimize.linprog (HiGHS) — методы highs, highs-ds, highs-ipm.")
    print()
    print("  min Z = sum(c_i * x_i)")
    print("  s.t.  sum((p - c_i) * x_i) >= target_profit")
    print("        0 <= x_i <= cap_i")
    print()

    suppliers = [
        Supplier(name="Поставщик А", cost_per_unit=85.0,  max_capacity=2000),
        Supplier(name="Поставщик Б", cost_per_unit=92.0,  max_capacity=1500),
        Supplier(name="Поставщик В", cost_per_unit=78.0,  max_capacity=1000),
    ]

    result = OptimalPurchaseAnalysis(
        category="Электронные компоненты",
        selling_price=120.0,
        target_profit=50_000.0,
        suppliers=suppliers,
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
        print(f"{sp.name:<{cw[0]}} {sp.units:>{cw[1]}.1f} "
              f"{sp.cost_per_unit:>{cw[2]}.2f} "
              f"{sp.total_cost:>{cw[3]}.2f} "
              f"{sp.contribution_to_profit:>{cw[4]}.2f}")
    print(sep)
    print(f"{'Итого':<{cw[0]}} {result.total_units:>{cw[1]}.1f} "
          f"{'':>{cw[2]}} {result.total_cost:>{cw[3]}.2f} "
          f"{result.actual_profit:>{cw[4]}.2f}")
    print()
    print(f"Выручка: {result.total_revenue:,.2f} руб.  "
          f"|  Затраты: {result.total_cost:,.2f} руб.  "
          f"|  Прибыль: {result.actual_profit:,.2f} руб.")
    print()

    print(f"{'Метод':<12} {'Статус':<10} {'Затраты, руб.':>16} {'Время, мс':>12}")
    print("-" * 52)
    for m in result.methods:
        cost_str = f"{m.total_cost:,.2f}" if m.total_cost is not None else "—"
        print(f"{m.method:<12} {'Успех' if m.success else 'Ошибка':<10} {cost_str:>16} {m.solve_time_ms:>12.4f}")


def main() -> None:
    print("Магазин электронных комплектующих — демонстрация системы")
    demo_electronic_components()
    demo_components()
    demo_tools()
    demo_services()
    demo_additional_services()
    demo_customer_relations()
    demo_mass_production()
    demo_optimal_purchase()
    print("\nГотово.")


if __name__ == "__main__":
    main()

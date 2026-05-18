# ==============================================================
# МАГАЗИН ЭЛЕКТРОННЫХ КОМПЛЕКТУЮЩИХ — ПОЛНЫЙ ИСХОДНЫЙ КОД
# ==============================================================

from __future__ import annotations
from typing import Optional


# ==============================================================
# Файл: models/resistor.py
# ==============================================================

"""
Модель резистора.
Описывает резистор с сопротивлением, мощностью и допуском точности.
"""


class Resistor:
    def __init__(self, resistance_ohm: float, power_w: float, accuracy_percent: float):
        self._resistance_ohm = resistance_ohm
        self._power_w = power_w
        self._accuracy_percent = accuracy_percent

    @property
    def resistance_ohm(self) -> float:
        return self._resistance_ohm

    @resistance_ohm.setter
    def resistance_ohm(self, value: float):
        self._resistance_ohm = value

    @property
    def power_w(self) -> float:
        return self._power_w

    @power_w.setter
    def power_w(self, value: float):
        self._power_w = value

    @property
    def accuracy_percent(self) -> float:
        return self._accuracy_percent

    @accuracy_percent.setter
    def accuracy_percent(self, value: float):
        self._accuracy_percent = value


# ==============================================================
# Файл: models/capacitor.py
# ==============================================================

"""
Модель конденсатора.
Описывает конденсатор с ёмкостью, рабочим напряжением и типом диэлектрика.
"""


class Capacitor:
    def __init__(self, capacitance_f: float, working_voltage_v: float, type: str):
        self._capacitance_f = capacitance_f
        self._working_voltage_v = working_voltage_v
        self._type = type  # "ceramic" | "electrolytic"

    @property
    def capacitance_f(self) -> float:
        return self._capacitance_f

    @capacitance_f.setter
    def capacitance_f(self, value: float):
        self._capacitance_f = value

    @property
    def working_voltage_v(self) -> float:
        return self._working_voltage_v

    @working_voltage_v.setter
    def working_voltage_v(self, value: float):
        self._working_voltage_v = value

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, value: str):
        self._type = value


# ==============================================================
# Файл: models/integrated_circuit.py
# ==============================================================

"""
Модель микросхемы.
Описывает микросхему с её назначением, напряжением питания и типом корпуса.
"""


class IntegratedCircuit:
    def __init__(self, type_purpose: str, supply_voltage_v: float, package: str):
        self._type_purpose = type_purpose  # "logic" | "controller" | ...
        self._supply_voltage_v = supply_voltage_v
        self._package = package  # "DIP" | "SMD"

    @property
    def type_purpose(self) -> str:
        return self._type_purpose

    @type_purpose.setter
    def type_purpose(self, value: str):
        self._type_purpose = value

    @property
    def supply_voltage_v(self) -> float:
        return self._supply_voltage_v

    @supply_voltage_v.setter
    def supply_voltage_v(self, value: float):
        self._supply_voltage_v = value

    @property
    def package(self) -> str:
        return self._package

    @package.setter
    def package(self, value: str):
        self._package = value


# ==============================================================
# Файл: models/transistor.py
# ==============================================================

"""
Модель транзистора.
Описывает транзистор с типом (NPN/PNP/MOSFET), максимальным током и напряжением.
"""


class Transistor:
    def __init__(self, type: str, max_current_a: float, voltage_v: float):
        self._type = type  # "NPN" | "PNP" | "MOSFET"
        self._max_current_a = max_current_a
        self._voltage_v = voltage_v

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, value: str):
        self._type = value

    @property
    def max_current_a(self) -> float:
        return self._max_current_a

    @max_current_a.setter
    def max_current_a(self, value: float):
        self._max_current_a = value

    @property
    def voltage_v(self) -> float:
        return self._voltage_v

    @voltage_v.setter
    def voltage_v(self, value: float):
        self._voltage_v = value


# ==============================================================
# Файл: models/diode.py
# ==============================================================

"""
Модель диода.
Описывает диод (выпрямительный, стабилитрон или светодиод) с прямым напряжением и максимальным током.
"""


class Diode:
    def __init__(self, type: str, forward_voltage_v: float, max_current_a: float):
        self._type = type  # "rectifier" | "zener" | "LED"
        self._forward_voltage_v = forward_voltage_v
        self._max_current_a = max_current_a

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, value: str):
        self._type = value

    @property
    def forward_voltage_v(self) -> float:
        return self._forward_voltage_v

    @forward_voltage_v.setter
    def forward_voltage_v(self, value: float):
        self._forward_voltage_v = value

    @property
    def max_current_a(self) -> float:
        return self._max_current_a

    @max_current_a.setter
    def max_current_a(self, value: float):
        self._max_current_a = value


# ==============================================================
# Файл: models/board.py
# ==============================================================

"""
Модель печатной платы (PCB).
Описывает плату с типом слойности, материалом основания и физическим размером.
"""


class Board:
    def __init__(self, type: str, material: str, size: str):
        self._type = type  # "single-sided" | "multilayer"
        self._material = material
        self._size = size

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, value: str):
        self._type = value

    @property
    def material(self) -> str:
        return self._material

    @material.setter
    def material(self, value: str):
        self._material = value

    @property
    def size(self) -> str:
        return self._size

    @size.setter
    def size(self, value: str):
        self._size = value


# ==============================================================
# Файл: models/connector.py
# ==============================================================

"""
Модель разъёма.
Описывает разъём с типом интерфейса, количеством контактов и способом монтажа.
"""


class Connector:
    def __init__(self, type: str, contact_count: int, mounting_method: str):
        self._type = type  # "USB" | "HDMI" | "pin header" | ...
        self._contact_count = contact_count
        self._mounting_method = mounting_method  # "SMD" | "through-hole"

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, value: str):
        self._type = value

    @property
    def contact_count(self) -> int:
        return self._contact_count

    @contact_count.setter
    def contact_count(self, value: int):
        self._contact_count = value

    @property
    def mounting_method(self) -> str:
        return self._mounting_method

    @mounting_method.setter
    def mounting_method(self, value: str):
        self._mounting_method = value


# ==============================================================
# Файл: models/soldering_equipment.py
# ==============================================================

"""
Модель паяльного оборудования.
Описывает паяльный инструмент (паяльник или станция) с мощностью и максимальной температурой нагрева.
"""


class SolderingEquipment:
    def __init__(self, power_w: float, heating_temp_c: float, type: str):
        self._power_w = power_w
        self._heating_temp_c = heating_temp_c
        self._type = type  # "soldering iron" | "station"

    @property
    def power_w(self) -> float:
        return self._power_w

    @power_w.setter
    def power_w(self, value: float):
        self._power_w = value

    @property
    def heating_temp_c(self) -> float:
        return self._heating_temp_c

    @heating_temp_c.setter
    def heating_temp_c(self, value: float):
        self._heating_temp_c = value

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, value: str):
        self._type = value


# ==============================================================
# Файл: models/measuring_instrument.py
# ==============================================================

"""
Модель измерительного прибора.
Описывает прибор (мультиметр, осциллограф) с точностью и диапазоном измерений.
"""


class MeasuringInstrument:
    def __init__(self, type: str, accuracy: str, measurement_range: str):
        self._type = type  # "multimeter" | "oscilloscope"
        self._accuracy = accuracy
        self._measurement_range = measurement_range

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, value: str):
        self._type = value

    @property
    def accuracy(self) -> str:
        return self._accuracy

    @accuracy.setter
    def accuracy(self, value: str):
        self._accuracy = value

    @property
    def measurement_range(self) -> str:
        return self._measurement_range

    @measurement_range.setter
    def measurement_range(self, value: str):
        self._measurement_range = value


# ==============================================================
# Файл: models/prototyping.py
# ==============================================================

"""
Модель услуги прототипирования.
Описывает доступные подуслуги: разработка схем и сборка прототипа.
"""


class Prototyping:
    def __init__(self, circuit_design: bool, prototype_assembly: bool):
        self._circuit_design = circuit_design
        self._prototype_assembly = prototype_assembly

    @property
    def circuit_design(self) -> bool:
        return self._circuit_design

    @circuit_design.setter
    def circuit_design(self, value: bool):
        self._circuit_design = value

    @property
    def prototype_assembly(self) -> bool:
        return self._prototype_assembly

    @prototype_assembly.setter
    def prototype_assembly(self, value: bool):
        self._prototype_assembly = value


# ==============================================================
# Файл: models/repair.py
# ==============================================================

"""
Модель услуги ремонта.
Описывает доступные подуслуги: диагностика неисправностей и замена компонентов.
"""


class Repair:
    def __init__(self, fault_diagnosis: bool, component_replacement: bool):
        self._fault_diagnosis = fault_diagnosis
        self._component_replacement = component_replacement

    @property
    def fault_diagnosis(self) -> bool:
        return self._fault_diagnosis

    @fault_diagnosis.setter
    def fault_diagnosis(self, value: bool):
        self._fault_diagnosis = value

    @property
    def component_replacement(self) -> bool:
        return self._component_replacement

    @component_replacement.setter
    def component_replacement(self, value: bool):
        self._component_replacement = value


# ==============================================================
# Файл: models/technical_documentation.py
# ==============================================================

"""
Модель услуги технической документации.
Описывает доступные подуслуги: подготовка схем и создание спецификаций (BOM).
"""


class TechnicalDocumentation:
    def __init__(self, circuit_preparation: bool, bom_creation: bool):
        self._circuit_preparation = circuit_preparation
        self._bom_creation = bom_creation

    @property
    def circuit_preparation(self) -> bool:
        return self._circuit_preparation

    @circuit_preparation.setter
    def circuit_preparation(self, value: bool):
        self._circuit_preparation = value

    @property
    def bom_creation(self) -> bool:
        return self._bom_creation

    @bom_creation.setter
    def bom_creation(self, value: bool):
        self._bom_creation = value


# ==============================================================
# Файл: models/engineer_consultation.py
# ==============================================================

"""
Модель услуги консультации инженера.
Описывает доступные подуслуги: подбор компонентов и оптимизация схем.
"""


class EngineerConsultation:
    def __init__(self, component_selection: bool, circuit_optimization: bool):
        self._component_selection = component_selection
        self._circuit_optimization = circuit_optimization

    @property
    def component_selection(self) -> bool:
        return self._component_selection

    @component_selection.setter
    def component_selection(self, value: bool):
        self._component_selection = value

    @property
    def circuit_optimization(self) -> bool:
        return self._circuit_optimization

    @circuit_optimization.setter
    def circuit_optimization(self, value: bool):
        self._circuit_optimization = value


# ==============================================================
# Файл: models/hobbyist.py
# ==============================================================

"""
Модель сегмента клиентов — радиолюбители.
Описывает услуги для радиолюбителей: помощь в подборе компонентов и сборка/настройка устройств.
"""


class Hobbyist:
    def __init__(self, component_selection_assistance: bool, device_assembly_setup: bool):
        self._component_selection_assistance = component_selection_assistance
        self._device_assembly_setup = device_assembly_setup

    @property
    def component_selection_assistance(self) -> bool:
        return self._component_selection_assistance

    @component_selection_assistance.setter
    def component_selection_assistance(self, value: bool):
        self._component_selection_assistance = value

    @property
    def device_assembly_setup(self) -> bool:
        return self._device_assembly_setup

    @device_assembly_setup.setter
    def device_assembly_setup(self, value: bool):
        self._device_assembly_setup = value


# ==============================================================
# Файл: models/service_center.py
# ==============================================================

"""
Модель сегмента клиентов — сервисные центры.
Описывает услуги для сервисных центров: поставка запчастей и срочная доставка компонентов.
"""


class ServiceCenter:
    def __init__(self, spare_parts_supply: bool, urgent_component_delivery: bool):
        self._spare_parts_supply = spare_parts_supply
        self._urgent_component_delivery = urgent_component_delivery

    @property
    def spare_parts_supply(self) -> bool:
        return self._spare_parts_supply

    @spare_parts_supply.setter
    def spare_parts_supply(self, value: bool):
        self._spare_parts_supply = value

    @property
    def urgent_component_delivery(self) -> bool:
        return self._urgent_component_delivery

    @urgent_component_delivery.setter
    def urgent_component_delivery(self, value: bool):
        self._urgent_component_delivery = value


# ==============================================================
# Файл: models/electronics_manufacturer.py
# ==============================================================

"""
Модель сегмента клиентов — производители электроники.
Описывает услуги для производителей: оптовые поставки и контрактная сборка.
"""


class ElectronicsManufacturer:
    def __init__(self, wholesale_supply: bool, contract_assembly: bool):
        self._wholesale_supply = wholesale_supply
        self._contract_assembly = contract_assembly

    @property
    def wholesale_supply(self) -> bool:
        return self._wholesale_supply

    @wholesale_supply.setter
    def wholesale_supply(self, value: bool):
        self._wholesale_supply = value

    @property
    def contract_assembly(self) -> bool:
        return self._contract_assembly

    @contract_assembly.setter
    def contract_assembly(self, value: bool):
        self._contract_assembly = value


# ==============================================================
# Файл: classes/electronic_components.py
# ==============================================================

"""
Класс электронных компонентов.
Объединяет пять основных типов компонентов: резисторы, конденсаторы,
микросхемы, транзисторы и диоды.
"""



class ElectronicComponents:
    def __init__(
        self,
        resistors: Optional[Resistor] = None,
        capacitors: Optional[Capacitor] = None,
        integrated_circuits: Optional[IntegratedCircuit] = None,
        transistors: Optional[Transistor] = None,
        diodes: Optional[Diode] = None,
    ):
        self._resistors = resistors
        self._capacitors = capacitors
        self._integrated_circuits = integrated_circuits
        self._transistors = transistors
        self._diodes = diodes

    @property
    def resistors(self) -> Optional[Resistor]:
        return self._resistors

    @resistors.setter
    def resistors(self, value: Resistor):
        self._resistors = value

    @property
    def capacitors(self) -> Optional[Capacitor]:
        return self._capacitors

    @capacitors.setter
    def capacitors(self, value: Capacitor):
        self._capacitors = value

    @property
    def integrated_circuits(self) -> Optional[IntegratedCircuit]:
        return self._integrated_circuits

    @integrated_circuits.setter
    def integrated_circuits(self, value: IntegratedCircuit):
        self._integrated_circuits = value

    @property
    def transistors(self) -> Optional[Transistor]:
        return self._transistors

    @transistors.setter
    def transistors(self, value: Transistor):
        self._transistors = value

    @property
    def diodes(self) -> Optional[Diode]:
        return self._diodes

    @diodes.setter
    def diodes(self, value: Diode):
        self._diodes = value


# ==============================================================
# Файл: classes/components.py
# ==============================================================

"""
Класс комплектующих.
Объединяет платы (PCB) и разъёмы как две основные категории комплектующих.
"""



class Components:
    def __init__(
        self,
        boards: Optional[Board] = None,
        connectors: Optional[Connector] = None,
    ):
        self._boards = boards
        self._connectors = connectors

    @property
    def boards(self) -> Optional[Board]:
        return self._boards

    @boards.setter
    def boards(self, value: Board):
        self._boards = value

    @property
    def connectors(self) -> Optional[Connector]:
        return self._connectors

    @connectors.setter
    def connectors(self, value: Connector):
        self._connectors = value


# ==============================================================
# Файл: classes/tools.py
# ==============================================================

"""
Класс инструментов.
Объединяет паяльное оборудование и измерительные приборы, используемые в работе с электроникой.
"""



class Tools:
    def __init__(
        self,
        soldering_equipment: Optional[SolderingEquipment] = None,
        measuring_instruments: Optional[MeasuringInstrument] = None,
    ):
        self._soldering_equipment = soldering_equipment
        self._measuring_instruments = measuring_instruments

    @property
    def soldering_equipment(self) -> Optional[SolderingEquipment]:
        return self._soldering_equipment

    @soldering_equipment.setter
    def soldering_equipment(self, value: SolderingEquipment):
        self._soldering_equipment = value

    @property
    def measuring_instruments(self) -> Optional[MeasuringInstrument]:
        return self._measuring_instruments

    @measuring_instruments.setter
    def measuring_instruments(self, value: MeasuringInstrument):
        self._measuring_instruments = value


# ==============================================================
# Файл: classes/services.py
# ==============================================================

"""
Класс услуг.
Охватывает два основных направления услуг: прототипирование и ремонт.
"""



class Services:
    def __init__(
        self,
        prototyping: Optional[Prototyping] = None,
        repair: Optional[Repair] = None,
    ):
        self._prototyping = prototyping
        self._repair = repair

    @property
    def prototyping(self) -> Optional[Prototyping]:
        return self._prototyping

    @prototyping.setter
    def prototyping(self, value: Prototyping):
        self._prototyping = value

    @property
    def repair(self) -> Optional[Repair]:
        return self._repair

    @repair.setter
    def repair(self, value: Repair):
        self._repair = value


# ==============================================================
# Файл: classes/additional_services.py
# ==============================================================

"""
Класс дополнительных услуг.
Объединяет вспомогательные направления: техническая документация и консультации инженеров.
"""



class AdditionalServices:
    def __init__(
        self,
        technical_documentation: Optional[TechnicalDocumentation] = None,
        engineer_consultations: Optional[EngineerConsultation] = None,
    ):
        self._technical_documentation = technical_documentation
        self._engineer_consultations = engineer_consultations

    @property
    def technical_documentation(self) -> Optional[TechnicalDocumentation]:
        return self._technical_documentation

    @technical_documentation.setter
    def technical_documentation(self, value: TechnicalDocumentation):
        self._technical_documentation = value

    @property
    def engineer_consultations(self) -> Optional[EngineerConsultation]:
        return self._engineer_consultations

    @engineer_consultations.setter
    def engineer_consultations(self, value: EngineerConsultation):
        self._engineer_consultations = value


# ==============================================================
# Файл: classes/customer_relations.py
# ==============================================================

"""
Класс работы с клиентами.
Делит клиентов на три сегмента: радиолюбители, сервисные центры
и производители электроники — каждый со своим набором услуг.
"""



class CustomerRelations:
    def __init__(
        self,
        hobbyists: Optional[Hobbyist] = None,
        service_centers: Optional[ServiceCenter] = None,
        electronics_manufacturers: Optional[ElectronicsManufacturer] = None,
    ):
        self._hobbyists = hobbyists
        self._service_centers = service_centers
        self._electronics_manufacturers = electronics_manufacturers

    @property
    def hobbyists(self) -> Optional[Hobbyist]:
        return self._hobbyists

    @hobbyists.setter
    def hobbyists(self, value: Hobbyist):
        self._hobbyists = value

    @property
    def service_centers(self) -> Optional[ServiceCenter]:
        return self._service_centers

    @service_centers.setter
    def service_centers(self, value: ServiceCenter):
        self._service_centers = value

    @property
    def electronics_manufacturers(self) -> Optional[ElectronicsManufacturer]:
        return self._electronics_manufacturers

    @electronics_manufacturers.setter
    def electronics_manufacturers(self, value: ElectronicsManufacturer):
        self._electronics_manufacturers = value


# ==============================================================
# Файл: classes/mass_production.py
# ==============================================================

"""
Класс серийного производства.
Описывает возможности серийного производства: сборка плат и тестирование изделий.
"""


class MassProduction:
    def __init__(
        self,
        board_assembly: bool = False,
        product_testing: bool = False,
    ):
        self._board_assembly = board_assembly
        self._product_testing = product_testing

    @property
    def board_assembly(self) -> bool:
        return self._board_assembly

    @board_assembly.setter
    def board_assembly(self, value: bool):
        self._board_assembly = value

    @property
    def product_testing(self) -> bool:
        return self._product_testing

    @product_testing.setter
    def product_testing(self, value: bool):
        self._product_testing = value


# ==============================================================
# Файл: main.py
# ==============================================================

"""
Точка входа — магазин электронных комплектующих.
Демонстрирует создание объектов всех классов и вывод сводной информации.
"""



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


def main() -> None:
    print("Магазин электронных комплектующих — демонстрация системы")
    demo_electronic_components()
    demo_components()
    demo_tools()
    demo_services()
    demo_additional_services()
    demo_customer_relations()
    demo_mass_production()
    print("\nГотово.")


if __name__ == "__main__":
    main()

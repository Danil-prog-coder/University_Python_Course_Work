from typing import List


# ─────────────────────────────────────────────
# Sub-classes for ElectronicComponents
# ─────────────────────────────────────────────

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


# ─────────────────────────────────────────────
# Sub-classes for Components
# ─────────────────────────────────────────────

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


# ─────────────────────────────────────────────
# Sub-classes for Tools
# ─────────────────────────────────────────────

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


# ─────────────────────────────────────────────
# Sub-classes for Services
# ─────────────────────────────────────────────

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


# ─────────────────────────────────────────────
# Sub-classes for AdditionalServices
# ─────────────────────────────────────────────

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


# ─────────────────────────────────────────────
# Sub-classes for CustomerRelations
# ─────────────────────────────────────────────

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


# ─────────────────────────────────────────────
# 1. Electronic components
# ─────────────────────────────────────────────

class ElectronicComponents:
    def __init__(
        self,
        resistors: List[Resistor] = None,
        capacitors: List[Capacitor] = None,
        integrated_circuits: List[IntegratedCircuit] = None,
        transistors: List[Transistor] = None,
        diodes: List[Diode] = None,
    ):
        self._resistors = resistors or []
        self._capacitors = capacitors or []
        self._integrated_circuits = integrated_circuits or []
        self._transistors = transistors or []
        self._diodes = diodes or []

    @property
    def resistors(self) -> List[Resistor]:
        return self._resistors

    @resistors.setter
    def resistors(self, value: List[Resistor]):
        self._resistors = value

    @property
    def capacitors(self) -> List[Capacitor]:
        return self._capacitors

    @capacitors.setter
    def capacitors(self, value: List[Capacitor]):
        self._capacitors = value

    @property
    def integrated_circuits(self) -> List[IntegratedCircuit]:
        return self._integrated_circuits

    @integrated_circuits.setter
    def integrated_circuits(self, value: List[IntegratedCircuit]):
        self._integrated_circuits = value

    @property
    def transistors(self) -> List[Transistor]:
        return self._transistors

    @transistors.setter
    def transistors(self, value: List[Transistor]):
        self._transistors = value

    @property
    def diodes(self) -> List[Diode]:
        return self._diodes

    @diodes.setter
    def diodes(self, value: List[Diode]):
        self._diodes = value


# ─────────────────────────────────────────────
# 2. Components / Hardware
# ─────────────────────────────────────────────

class Components:
    def __init__(
        self,
        boards: List[Board] = None,
        connectors: List[Connector] = None,
    ):
        self._boards = boards or []
        self._connectors = connectors or []

    @property
    def boards(self) -> List[Board]:
        return self._boards

    @boards.setter
    def boards(self, value: List[Board]):
        self._boards = value

    @property
    def connectors(self) -> List[Connector]:
        return self._connectors

    @connectors.setter
    def connectors(self, value: List[Connector]):
        self._connectors = value


# ─────────────────────────────────────────────
# 3. Tools
# ─────────────────────────────────────────────

class Tools:
    def __init__(
        self,
        soldering_equipment: List[SolderingEquipment] = None,
        measuring_instruments: List[MeasuringInstrument] = None,
    ):
        self._soldering_equipment = soldering_equipment or []
        self._measuring_instruments = measuring_instruments or []

    @property
    def soldering_equipment(self) -> List[SolderingEquipment]:
        return self._soldering_equipment

    @soldering_equipment.setter
    def soldering_equipment(self, value: List[SolderingEquipment]):
        self._soldering_equipment = value

    @property
    def measuring_instruments(self) -> List[MeasuringInstrument]:
        return self._measuring_instruments

    @measuring_instruments.setter
    def measuring_instruments(self, value: List[MeasuringInstrument]):
        self._measuring_instruments = value


# ─────────────────────────────────────────────
# 4. Services
# ─────────────────────────────────────────────

class Services:
    def __init__(
        self,
        prototyping: List[Prototyping] = None,
        repair: List[Repair] = None,
    ):
        self._prototyping = prototyping or []
        self._repair = repair or []

    @property
    def prototyping(self) -> List[Prototyping]:
        return self._prototyping

    @prototyping.setter
    def prototyping(self, value: List[Prototyping]):
        self._prototyping = value

    @property
    def repair(self) -> List[Repair]:
        return self._repair

    @repair.setter
    def repair(self, value: List[Repair]):
        self._repair = value


# ─────────────────────────────────────────────
# 5. Mass production
# ─────────────────────────────────────────────

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


# ─────────────────────────────────────────────
# 6. Additional services
# ─────────────────────────────────────────────

class AdditionalServices:
    def __init__(
        self,
        technical_documentation: List[TechnicalDocumentation] = None,
        engineer_consultations: List[EngineerConsultation] = None,
    ):
        self._technical_documentation = technical_documentation or []
        self._engineer_consultations = engineer_consultations or []

    @property
    def technical_documentation(self) -> List[TechnicalDocumentation]:
        return self._technical_documentation

    @technical_documentation.setter
    def technical_documentation(self, value: List[TechnicalDocumentation]):
        self._technical_documentation = value

    @property
    def engineer_consultations(self) -> List[EngineerConsultation]:
        return self._engineer_consultations

    @engineer_consultations.setter
    def engineer_consultations(self, value: List[EngineerConsultation]):
        self._engineer_consultations = value


# ─────────────────────────────────────────────
# 7. Customer relations
# ─────────────────────────────────────────────

class CustomerRelations:
    def __init__(
        self,
        hobbyists: List[Hobbyist] = None,
        service_centers: List[ServiceCenter] = None,
        electronics_manufacturers: List[ElectronicsManufacturer] = None,
    ):
        self._hobbyists = hobbyists or []
        self._service_centers = service_centers or []
        self._electronics_manufacturers = electronics_manufacturers or []

    @property
    def hobbyists(self) -> List[Hobbyist]:
        return self._hobbyists

    @hobbyists.setter
    def hobbyists(self, value: List[Hobbyist]):
        self._hobbyists = value

    @property
    def service_centers(self) -> List[ServiceCenter]:
        return self._service_centers

    @service_centers.setter
    def service_centers(self, value: List[ServiceCenter]):
        self._service_centers = value

    @property
    def electronics_manufacturers(self) -> List[ElectronicsManufacturer]:
        return self._electronics_manufacturers

    @electronics_manufacturers.setter
    def electronics_manufacturers(self, value: List[ElectronicsManufacturer]):
        self._electronics_manufacturers = value

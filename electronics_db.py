from typing import List


# 1. Electronic components
class ElectronicComponents:
    def __init__(
        self,
        resistors: List = None,
        capacitors: List = None,
        integrated_circuits: List = None,
        transistors: List = None,
        diodes: List = None,
    ):
        self._resistors = resistors or []
        self._capacitors = capacitors or []
        self._integrated_circuits = integrated_circuits or []
        self._transistors = transistors or []
        self._diodes = diodes or []

    @property
    def resistors(self) -> List:
        return self._resistors

    @resistors.setter
    def resistors(self, value: List):
        self._resistors = value

    @property
    def capacitors(self) -> List:
        return self._capacitors

    @capacitors.setter
    def capacitors(self, value: List):
        self._capacitors = value

    @property
    def integrated_circuits(self) -> List:
        return self._integrated_circuits

    @integrated_circuits.setter
    def integrated_circuits(self, value: List):
        self._integrated_circuits = value

    @property
    def transistors(self) -> List:
        return self._transistors

    @transistors.setter
    def transistors(self, value: List):
        self._transistors = value

    @property
    def diodes(self) -> List:
        return self._diodes

    @diodes.setter
    def diodes(self, value: List):
        self._diodes = value


# 2. Components / Hardware
class Components:
    def __init__(
        self,
        boards: List = None,
        connectors: List = None,
    ):
        self._boards = boards or []
        self._connectors = connectors or []

    @property
    def boards(self) -> List:
        return self._boards

    @boards.setter
    def boards(self, value: List):
        self._boards = value

    @property
    def connectors(self) -> List:
        return self._connectors

    @connectors.setter
    def connectors(self, value: List):
        self._connectors = value


# 3. Tools
class Tools:
    def __init__(
        self,
        soldering_equipment: List = None,
        measuring_instruments: List = None,
    ):
        self._soldering_equipment = soldering_equipment or []
        self._measuring_instruments = measuring_instruments or []

    @property
    def soldering_equipment(self) -> List:
        return self._soldering_equipment

    @soldering_equipment.setter
    def soldering_equipment(self, value: List):
        self._soldering_equipment = value

    @property
    def measuring_instruments(self) -> List:
        return self._measuring_instruments

    @measuring_instruments.setter
    def measuring_instruments(self, value: List):
        self._measuring_instruments = value


# 4. Services
class Services:
    def __init__(
        self,
        prototyping: List = None,
        repair: List = None,
    ):
        self._prototyping = prototyping or []
        self._repair = repair or []

    @property
    def prototyping(self) -> List:
        return self._prototyping

    @prototyping.setter
    def prototyping(self, value: List):
        self._prototyping = value

    @property
    def repair(self) -> List:
        return self._repair

    @repair.setter
    def repair(self, value: List):
        self._repair = value


# 5. Mass production
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


# 6. Additional services
class AdditionalServices:
    def __init__(
        self,
        technical_documentation: List = None,
        engineer_consultations: List = None,
    ):
        self._technical_documentation = technical_documentation or []
        self._engineer_consultations = engineer_consultations or []

    @property
    def technical_documentation(self) -> List:
        return self._technical_documentation

    @technical_documentation.setter
    def technical_documentation(self, value: List):
        self._technical_documentation = value

    @property
    def engineer_consultations(self) -> List:
        return self._engineer_consultations

    @engineer_consultations.setter
    def engineer_consultations(self, value: List):
        self._engineer_consultations = value


# 7. Customer relations
class CustomerRelations:
    def __init__(
        self,
        hobbyists: List = None,
        service_centers: List = None,
        electronics_manufacturers: List = None,
    ):
        self._hobbyists = hobbyists or []
        self._service_centers = service_centers or []
        self._electronics_manufacturers = electronics_manufacturers or []

    @property
    def hobbyists(self) -> List:
        return self._hobbyists

    @hobbyists.setter
    def hobbyists(self, value: List):
        self._hobbyists = value

    @property
    def service_centers(self) -> List:
        return self._service_centers

    @service_centers.setter
    def service_centers(self, value: List):
        self._service_centers = value

    @property
    def electronics_manufacturers(self) -> List:
        return self._electronics_manufacturers

    @electronics_manufacturers.setter
    def electronics_manufacturers(self, value: List):
        self._electronics_manufacturers = value

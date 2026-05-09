from typing import Optional
from models.resistor import Resistor
from models.capacitor import Capacitor
from models.integrated_circuit import IntegratedCircuit
from models.transistor import Transistor
from models.diode import Diode


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

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

"""
Модель микросхемы.
Описывает микросхему с её назначением, напряжением питания и типом корпуса.
"""


class IntegratedCircuit:
    def __init__(self, type_purpose: str, supply_voltage_v: float, package: str, price_rub: float):
        self._type_purpose = type_purpose  # "logic" | "controller" | ...
        self._supply_voltage_v = supply_voltage_v
        self._package = package  # "DIP" | "SMD"
        self._price_rub = price_rub

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

    @property
    def price_rub(self) -> float:
        return self._price_rub

    @price_rub.setter
    def price_rub(self, value: float):
        self._price_rub = value

"""
Модель резистора.
Описывает резистор с сопротивлением, мощностью и допуском точности.
"""


class Resistor:
    def __init__(self, resistance_ohm: float, power_w: float, accuracy_percent: float, price_rub: float):
        self._resistance_ohm = resistance_ohm
        self._power_w = power_w
        self._accuracy_percent = accuracy_percent
        self._price_rub = price_rub

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

    @property
    def price_rub(self) -> float:
        return self._price_rub

    @price_rub.setter
    def price_rub(self, value: float):
        self._price_rub = value

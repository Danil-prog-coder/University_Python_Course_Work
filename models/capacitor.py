"""
Модель конденсатора.
Описывает конденсатор с ёмкостью, рабочим напряжением и типом диэлектрика.
"""


class Capacitor:
    def __init__(self, capacitance_f: float, working_voltage_v: float, type: str, price_rub: float):
        self._capacitance_f = capacitance_f
        self._working_voltage_v = working_voltage_v
        self._type = type  # "ceramic" | "electrolytic"
        self._price_rub = price_rub

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

    @property
    def price_rub(self) -> float:
        return self._price_rub

    @price_rub.setter
    def price_rub(self, value: float):
        self._price_rub = value

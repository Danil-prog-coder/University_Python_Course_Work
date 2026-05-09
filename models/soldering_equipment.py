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

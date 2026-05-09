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

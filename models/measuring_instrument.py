"""
Модель измерительного прибора.
Описывает прибор (мультиметр, осциллограф) с точностью и диапазоном измерений.
"""


class MeasuringInstrument:
    def __init__(self, type: str, accuracy: str, measurement_range: str,
                 accuracy_percent: float, range_value: float, price_rub: float):
        self._type = type  # "multimeter" | "oscilloscope"
        self._accuracy = accuracy
        self._measurement_range = measurement_range
        self._accuracy_percent = accuracy_percent
        self._range_value = range_value
        self._price_rub = price_rub

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

    @property
    def accuracy_percent(self) -> float:
        return self._accuracy_percent

    @accuracy_percent.setter
    def accuracy_percent(self, value: float):
        self._accuracy_percent = value

    @property
    def range_value(self) -> float:
        return self._range_value

    @range_value.setter
    def range_value(self, value: float):
        self._range_value = value

    @property
    def price_rub(self) -> float:
        return self._price_rub

    @price_rub.setter
    def price_rub(self, value: float):
        self._price_rub = value

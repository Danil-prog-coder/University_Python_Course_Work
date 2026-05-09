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

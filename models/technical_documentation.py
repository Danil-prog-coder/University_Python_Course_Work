class TechnicalDocumentation:
    def __init__(self, circuit_preparation: bool, bom_creation: bool):
        self._circuit_preparation = circuit_preparation
        self._bom_creation = bom_creation

    @property
    def circuit_preparation(self) -> bool:
        return self._circuit_preparation

    @circuit_preparation.setter
    def circuit_preparation(self, value: bool):
        self._circuit_preparation = value

    @property
    def bom_creation(self) -> bool:
        return self._bom_creation

    @bom_creation.setter
    def bom_creation(self, value: bool):
        self._bom_creation = value

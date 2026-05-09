class Prototyping:
    def __init__(self, circuit_design: bool, prototype_assembly: bool):
        self._circuit_design = circuit_design
        self._prototype_assembly = prototype_assembly

    @property
    def circuit_design(self) -> bool:
        return self._circuit_design

    @circuit_design.setter
    def circuit_design(self, value: bool):
        self._circuit_design = value

    @property
    def prototype_assembly(self) -> bool:
        return self._prototype_assembly

    @prototype_assembly.setter
    def prototype_assembly(self, value: bool):
        self._prototype_assembly = value

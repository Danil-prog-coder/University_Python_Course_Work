class Repair:
    def __init__(self, fault_diagnosis: bool, component_replacement: bool):
        self._fault_diagnosis = fault_diagnosis
        self._component_replacement = component_replacement

    @property
    def fault_diagnosis(self) -> bool:
        return self._fault_diagnosis

    @fault_diagnosis.setter
    def fault_diagnosis(self, value: bool):
        self._fault_diagnosis = value

    @property
    def component_replacement(self) -> bool:
        return self._component_replacement

    @component_replacement.setter
    def component_replacement(self, value: bool):
        self._component_replacement = value

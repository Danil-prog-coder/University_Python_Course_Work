"""
Engineer consultation service model.
Describes available consultation services: component selection and circuit optimization.
"""


class EngineerConsultation:
    def __init__(self, component_selection: bool, circuit_optimization: bool):
        self._component_selection = component_selection
        self._circuit_optimization = circuit_optimization

    @property
    def component_selection(self) -> bool:
        return self._component_selection

    @component_selection.setter
    def component_selection(self, value: bool):
        self._component_selection = value

    @property
    def circuit_optimization(self) -> bool:
        return self._circuit_optimization

    @circuit_optimization.setter
    def circuit_optimization(self, value: bool):
        self._circuit_optimization = value

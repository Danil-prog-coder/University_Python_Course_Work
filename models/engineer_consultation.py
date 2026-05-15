"""
Модель услуги консультации инженера.
Описывает доступные подуслуги: подбор компонентов и оптимизация схем.
"""


class EngineerConsultation:
    def __init__(self, component_selection: bool, circuit_optimization: bool, service_price_rub: float, avg_execution_days: int):
        self._component_selection = component_selection
        self._circuit_optimization = circuit_optimization
        self._service_price_rub = service_price_rub
        self._avg_execution_days = avg_execution_days

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

    @property
    def service_price_rub(self) -> float:
        return self._service_price_rub

    @service_price_rub.setter
    def service_price_rub(self, value: float):
        self._service_price_rub = value

    @property
    def avg_execution_days(self) -> int:
        return self._avg_execution_days

    @avg_execution_days.setter
    def avg_execution_days(self, value: int):
        self._avg_execution_days = value

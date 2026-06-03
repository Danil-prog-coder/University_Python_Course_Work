"""
Модель услуги ремонта.
Описывает доступные подуслуги: диагностика неисправностей и замена компонентов.
"""


class Repair:
    def __init__(self, fault_diagnosis: bool, component_replacement: bool,
                 service_price_rub: float, avg_execution_days: float):
        self._service_price_rub = service_price_rub
        self._avg_execution_days = avg_execution_days
        self._fault_diagnosis = fault_diagnosis
        self._component_replacement = component_replacement

    @property
    def service_price_rub(self) -> float:
        return self._service_price_rub

    @service_price_rub.setter
    def service_price_rub(self, value: float):
        self._service_price_rub = value

    @property
    def avg_execution_days(self) -> float:
        return self._avg_execution_days

    @avg_execution_days.setter
    def avg_execution_days(self, value: float):
        self._avg_execution_days = value

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

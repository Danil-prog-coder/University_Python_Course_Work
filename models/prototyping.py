"""
Модель услуги прототипирования.
Описывает доступные подуслуги: разработка схем и сборка прототипа.
"""


class Prototyping:
    def __init__(self, circuit_design: bool, prototype_assembly: bool, service_price_rub: float, avg_execution_days: int):
        self._circuit_design = circuit_design
        self._prototype_assembly = prototype_assembly
        self._service_price_rub = service_price_rub
        self._avg_execution_days = avg_execution_days

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

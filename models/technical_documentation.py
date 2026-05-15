"""
Модель услуги технической документации.
Описывает доступные подуслуги: подготовка схем и создание спецификаций (BOM).
"""


class TechnicalDocumentation:
    def __init__(self, circuit_preparation: bool, bom_creation: bool, service_price_rub: float, avg_execution_days: int):
        self._circuit_preparation = circuit_preparation
        self._bom_creation = bom_creation
        self._service_price_rub = service_price_rub
        self._avg_execution_days = avg_execution_days

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

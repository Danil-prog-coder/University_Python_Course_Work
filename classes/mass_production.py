"""
Класс серийного производства.
Описывает возможности серийного производства: сборка плат и тестирование изделий.
"""


class MassProduction:
    def __init__(
        self,
        board_assembly: bool = False,
        product_testing: bool = False,
        service_price_rub: float = 0.0,
        avg_execution_days: int = 0,
    ):
        self._board_assembly = board_assembly
        self._product_testing = product_testing
        self._service_price_rub = service_price_rub
        self._avg_execution_days = avg_execution_days

    @property
    def board_assembly(self) -> bool:
        return self._board_assembly

    @board_assembly.setter
    def board_assembly(self, value: bool):
        self._board_assembly = value

    @property
    def product_testing(self) -> bool:
        return self._product_testing

    @product_testing.setter
    def product_testing(self, value: bool):
        self._product_testing = value

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

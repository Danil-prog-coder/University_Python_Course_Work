"""
Класс серийного производства.
Описывает возможности серийного производства: сборка плат и тестирование изделий.
"""


class MassProduction:
    def __init__(
        self,
        board_assembly: bool = False,
        product_testing: bool = False,
    ):
        self._board_assembly = board_assembly
        self._product_testing = product_testing

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

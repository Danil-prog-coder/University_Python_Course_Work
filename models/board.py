"""
Модель печатной платы (PCB).
Описывает плату с типом слойности, материалом основания и физическим размером.
"""


class Board:
    def __init__(self, type: str, material: str, size: str, price_rub: float):
        self._type = type  # "single-sided" | "multilayer"
        self._material = material
        self._size = size
        self._price_rub = price_rub

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, value: str):
        self._type = value

    @property
    def material(self) -> str:
        return self._material

    @material.setter
    def material(self, value: str):
        self._material = value

    @property
    def size(self) -> str:
        return self._size

    @size.setter
    def size(self, value: str):
        self._size = value

    @property
    def price_rub(self) -> float:
        return self._price_rub

    @price_rub.setter
    def price_rub(self, value: float):
        self._price_rub = value

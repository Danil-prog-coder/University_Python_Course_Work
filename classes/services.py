"""
Класс услуг.
Охватывает два основных направления услуг: прототипирование и ремонт.
"""

from typing import Optional
from models.prototyping import Prototyping
from models.repair import Repair


class Services:
    def __init__(
        self,
        prototyping: Optional[Prototyping] = None,
        repair: Optional[Repair] = None,
    ):
        self._prototyping = prototyping
        self._repair = repair

    @property
    def prototyping(self) -> Optional[Prototyping]:
        return self._prototyping

    @prototyping.setter
    def prototyping(self, value: Prototyping):
        self._prototyping = value

    @property
    def repair(self) -> Optional[Repair]:
        return self._repair

    @repair.setter
    def repair(self, value: Repair):
        self._repair = value

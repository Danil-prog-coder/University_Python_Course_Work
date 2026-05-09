"""
Класс инструментов.
Объединяет паяльное оборудование и измерительные приборы, используемые в работе с электроникой.
"""

from typing import Optional
from models.soldering_equipment import SolderingEquipment
from models.measuring_instrument import MeasuringInstrument


class Tools:
    def __init__(
        self,
        soldering_equipment: Optional[SolderingEquipment] = None,
        measuring_instruments: Optional[MeasuringInstrument] = None,
    ):
        self._soldering_equipment = soldering_equipment
        self._measuring_instruments = measuring_instruments

    @property
    def soldering_equipment(self) -> Optional[SolderingEquipment]:
        return self._soldering_equipment

    @soldering_equipment.setter
    def soldering_equipment(self, value: SolderingEquipment):
        self._soldering_equipment = value

    @property
    def measuring_instruments(self) -> Optional[MeasuringInstrument]:
        return self._measuring_instruments

    @measuring_instruments.setter
    def measuring_instruments(self, value: MeasuringInstrument):
        self._measuring_instruments = value

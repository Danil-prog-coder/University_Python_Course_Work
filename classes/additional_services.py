"""
Класс дополнительных услуг.
Объединяет вспомогательные направления: техническая документация и консультации инженеров.
"""

from typing import Optional
from models.technical_documentation import TechnicalDocumentation
from models.engineer_consultation import EngineerConsultation


class AdditionalServices:
    def __init__(
        self,
        technical_documentation: Optional[TechnicalDocumentation] = None,
        engineer_consultations: Optional[EngineerConsultation] = None,
    ):
        self._technical_documentation = technical_documentation
        self._engineer_consultations = engineer_consultations

    @property
    def technical_documentation(self) -> Optional[TechnicalDocumentation]:
        return self._technical_documentation

    @technical_documentation.setter
    def technical_documentation(self, value: TechnicalDocumentation):
        self._technical_documentation = value

    @property
    def engineer_consultations(self) -> Optional[EngineerConsultation]:
        return self._engineer_consultations

    @engineer_consultations.setter
    def engineer_consultations(self, value: EngineerConsultation):
        self._engineer_consultations = value

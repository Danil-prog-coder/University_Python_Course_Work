"""
Класс работы с клиентами.
Делит клиентов на три сегмента: радиолюбители, сервисные центры
и производители электроники — каждый со своим набором услуг.
"""

from typing import Optional
from models.hobbyist import Hobbyist
from models.service_center import ServiceCenter
from models.electronics_manufacturer import ElectronicsManufacturer


class CustomerRelations:
    def __init__(
        self,
        hobbyists: Optional[Hobbyist] = None,
        service_centers: Optional[ServiceCenter] = None,
        electronics_manufacturers: Optional[ElectronicsManufacturer] = None,
    ):
        self._hobbyists = hobbyists
        self._service_centers = service_centers
        self._electronics_manufacturers = electronics_manufacturers

    @property
    def hobbyists(self) -> Optional[Hobbyist]:
        return self._hobbyists

    @hobbyists.setter
    def hobbyists(self, value: Hobbyist):
        self._hobbyists = value

    @property
    def service_centers(self) -> Optional[ServiceCenter]:
        return self._service_centers

    @service_centers.setter
    def service_centers(self, value: ServiceCenter):
        self._service_centers = value

    @property
    def electronics_manufacturers(self) -> Optional[ElectronicsManufacturer]:
        return self._electronics_manufacturers

    @electronics_manufacturers.setter
    def electronics_manufacturers(self, value: ElectronicsManufacturer):
        self._electronics_manufacturers = value

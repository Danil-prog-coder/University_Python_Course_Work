"""
Модель сегмента клиентов — сервисные центры.
Описывает услуги для сервисных центров: поставка запчастей и срочная доставка компонентов.
"""


class ServiceCenter:
    def __init__(self, spare_parts_supply: bool, urgent_component_delivery: bool,
                 min_order_rub: float):
        self._min_order_rub = min_order_rub
        self._spare_parts_supply = spare_parts_supply
        self._urgent_component_delivery = urgent_component_delivery

    @property
    def min_order_rub(self) -> float:
        return self._min_order_rub

    @min_order_rub.setter
    def min_order_rub(self, value: float):
        self._min_order_rub = value

    @property
    def spare_parts_supply(self) -> bool:
        return self._spare_parts_supply

    @spare_parts_supply.setter
    def spare_parts_supply(self, value: bool):
        self._spare_parts_supply = value

    @property
    def urgent_component_delivery(self) -> bool:
        return self._urgent_component_delivery

    @urgent_component_delivery.setter
    def urgent_component_delivery(self, value: bool):
        self._urgent_component_delivery = value

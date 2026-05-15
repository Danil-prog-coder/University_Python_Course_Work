"""
Модель сегмента клиентов — сервисные центры.
Описывает услуги для сервисных центров: поставка запчастей и срочная доставка компонентов.
"""


class ServiceCenter:
    def __init__(self, spare_parts_supply: bool, urgent_component_delivery: bool, pricing_condition: str, min_order_rub: float):
        self._spare_parts_supply = spare_parts_supply
        self._urgent_component_delivery = urgent_component_delivery
        self._pricing_condition = pricing_condition  # "retail" | "wholesale" | "contract assembly"
        self._min_order_rub = min_order_rub

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

    @property
    def pricing_condition(self) -> str:
        return self._pricing_condition

    @pricing_condition.setter
    def pricing_condition(self, value: str):
        self._pricing_condition = value

    @property
    def min_order_rub(self) -> float:
        return self._min_order_rub

    @min_order_rub.setter
    def min_order_rub(self, value: float):
        self._min_order_rub = value

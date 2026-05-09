class ServiceCenter:
    def __init__(self, spare_parts_supply: bool, urgent_component_delivery: bool):
        self._spare_parts_supply = spare_parts_supply
        self._urgent_component_delivery = urgent_component_delivery

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

"""
Модель сегмента клиентов — производители электроники.
Описывает услуги для производителей: оптовые поставки и контрактная сборка.
"""


class ElectronicsManufacturer:
    def __init__(self, wholesale_supply: bool, contract_assembly: bool, pricing_condition: str, min_order_rub: float):
        self._wholesale_supply = wholesale_supply
        self._contract_assembly = contract_assembly
        self._pricing_condition = pricing_condition  # "retail" | "wholesale" | "contract assembly"
        self._min_order_rub = min_order_rub

    @property
    def wholesale_supply(self) -> bool:
        return self._wholesale_supply

    @wholesale_supply.setter
    def wholesale_supply(self, value: bool):
        self._wholesale_supply = value

    @property
    def contract_assembly(self) -> bool:
        return self._contract_assembly

    @contract_assembly.setter
    def contract_assembly(self, value: bool):
        self._contract_assembly = value

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

"""
Electronics manufacturer customer segment model.
Describes services offered to manufacturers: wholesale supply and contract assembly.
"""


class ElectronicsManufacturer:
    def __init__(self, wholesale_supply: bool, contract_assembly: bool):
        self._wholesale_supply = wholesale_supply
        self._contract_assembly = contract_assembly

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

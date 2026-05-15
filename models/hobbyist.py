"""
Модель сегмента клиентов — радиолюбители.
Описывает услуги для радиолюбителей: помощь в подборе компонентов и сборка/настройка устройств.
"""


class Hobbyist:
    def __init__(self, component_selection_assistance: bool, device_assembly_setup: bool, pricing_condition: str, min_order_rub: float):
        self._component_selection_assistance = component_selection_assistance
        self._device_assembly_setup = device_assembly_setup
        self._pricing_condition = pricing_condition  # "retail" | "wholesale" | "contract assembly"
        self._min_order_rub = min_order_rub

    @property
    def component_selection_assistance(self) -> bool:
        return self._component_selection_assistance

    @component_selection_assistance.setter
    def component_selection_assistance(self, value: bool):
        self._component_selection_assistance = value

    @property
    def device_assembly_setup(self) -> bool:
        return self._device_assembly_setup

    @device_assembly_setup.setter
    def device_assembly_setup(self, value: bool):
        self._device_assembly_setup = value

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

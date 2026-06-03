"""
Модель сегмента клиентов — радиолюбители.
Описывает услуги для радиолюбителей: помощь в подборе компонентов и сборка/настройка устройств.
"""


class Hobbyist:
    def __init__(self, component_selection_assistance: bool, device_assembly_setup: bool,
                 min_order_rub: float):
        self._min_order_rub = min_order_rub
        self._component_selection_assistance = component_selection_assistance
        self._device_assembly_setup = device_assembly_setup

    @property
    def min_order_rub(self) -> float:
        return self._min_order_rub

    @min_order_rub.setter
    def min_order_rub(self, value: float):
        self._min_order_rub = value

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

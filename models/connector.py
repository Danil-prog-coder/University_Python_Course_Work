class Connector:
    def __init__(self, type: str, contact_count: int, mounting_method: str):
        self._type = type  # "USB" | "HDMI" | "pin header" | ...
        self._contact_count = contact_count
        self._mounting_method = mounting_method  # "SMD" | "through-hole"

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, value: str):
        self._type = value

    @property
    def contact_count(self) -> int:
        return self._contact_count

    @contact_count.setter
    def contact_count(self, value: int):
        self._contact_count = value

    @property
    def mounting_method(self) -> str:
        return self._mounting_method

    @mounting_method.setter
    def mounting_method(self, value: str):
        self._mounting_method = value

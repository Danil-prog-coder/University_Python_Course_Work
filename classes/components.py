"""
Класс комплектующих.
Объединяет платы (PCB) и разъёмы как две основные категории комплектующих.
"""

from typing import Optional
from models.board import Board
from models.connector import Connector


class Components:
    def __init__(
        self,
        boards: Optional[Board] = None,
        connectors: Optional[Connector] = None,
    ):
        self._boards = boards
        self._connectors = connectors

    @property
    def boards(self) -> Optional[Board]:
        return self._boards

    @boards.setter
    def boards(self, value: Board):
        self._boards = value

    @property
    def connectors(self) -> Optional[Connector]:
        return self._connectors

    @connectors.setter
    def connectors(self, value: Connector):
        self._connectors = value

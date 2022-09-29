from __future__ import annotations
from MagicSquare import MagicSquare


class Node:
    def __init__(self, magic_square: MagicSquare = None) -> None:
        self.__magic_square: MagicSquare = magic_square or MagicSquare()
        self.__children: list[Node] = []

    @property
    def magic_square(self) -> MagicSquare:
        return self.__magic_square

    @property
    def children(self) -> list[Node]:
        return self.__children

    def get_child(self, position: int) -> Node | None:
        try:
            return self.children[position]
        except IndexError:
            return None

    def append_child(self, value: Node) -> None:
        self.children.append(value)

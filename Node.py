from __future__ import annotations


class Node:
    def __init__(self, parent: Node = None) -> None:
        self.__children: list[Node] = []
        self.__parent: Node = parent

        self.__parent.append_child(self)

    @property
    def children(self) -> list[Node]:
        return self.__children

    @property
    def parent(self) -> Node:
        return self.__parent

    def get_child(self, position: int) -> Node | None:
        try:
            return self.children[position]
        except IndexError:
            return None

    def append_child(self, value: Node) -> None:
        self.children.append(value)

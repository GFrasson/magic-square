from Node import Node


class SearchTree:
    def __init__(self) -> None:
        self.__root: Node = Node()

    @property
    def root(self) -> Node:
        return self.__root

from State import State


class SearchTree:
    def __init__(self) -> None:
        self.__root: State = State()

    @property
    def root(self) -> State:
        return self.__root

class SearchRule:
    def __init__(self, row: int, column: int, name: str) -> None:
        self.__row = row
        self.__column = column
        self.__name = name

    @property
    def row(self) -> int:
        return self.__row

    @property
    def column(self) -> int:
        return self.__column

    @property
    def name(self) -> str:
        return self.__name

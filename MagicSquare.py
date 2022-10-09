class MagicSquare:
    def __init__(self, square=None, current_number=1, size=3) -> None:
        self.__current_number = current_number
        self.__size = size
        self.__desired_sum = 15
        self.__square = list()

        for i in range(0, self.__size):
            row = [0 for j in range(0, self.__size)]
            self.__square.append(row)

        if square:
            for row in range(0, self.__size):
                for column in range(0, self.__size):
                    self.__square[row][column] = square[row][column]

    def __str__(self) -> str:
        matrix_representation = ''

        for row in self.square:
            for element in row:
                matrix_representation += f'{element} '
            matrix_representation += '\n'

        return matrix_representation

    @property
    def square(self) -> list[list[int]]:
        return self.__square

    @property
    def size(self) -> int:
        return self.__size

    @property
    def current_number(self) -> int:
        return self.__current_number

    @property
    def desired_sum(self) -> int:
        return self.__desired_sum

    def insert_next_number(self, row: int, column: int) -> None:
        try:
            self.square[row][column] = self.current_number
            self.__current_number += 1
        except IndexError:
            print('Index out of range')

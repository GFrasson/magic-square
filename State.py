from __future__ import annotations

from MagicSquare import MagicSquare
from Node import Node
from SearchRule import SearchRule


class State(Node):
    def __init__(self, magic_square: MagicSquare = None, parent: Node = None, current_magic_square_number=1) -> None:
        super().__init__(parent)
        self.__magic_square: MagicSquare = magic_square or MagicSquare()
        self.__magic_square_size = len(self.__magic_square[0])
        self.__current_rule_index = 0
        self.__max_rule_index = 8
        self.__current_magic_square_number = current_magic_square_number
        self.__valid = True

    @property
    def magic_square(self) -> MagicSquare:
        return self.__magic_square

    @property
    def magic_square_size(self) -> int:
        return self.__magic_square_size

    @property
    def current_rule_index(self) -> int:
        return self.__current_rule_index

    @property
    def current_magic_square_number(self) -> int:
        return self.__current_magic_square_number

    @property
    def valid(self) -> bool:
        return self.__valid

    @valid.setter
    def valid(self, value: bool) -> None:
        self.__valid = value

    def __reset_current_rule_index(self) -> None:
        self.current_rule = 0

    def update_current_rule_index(self) -> None:
        self.current_rule += 1
        if self.current_rule > self.__max_rule_index:
            # Forçar impasse (?)
            self.__reset_current_rule_index()

    def visit_state(self, rule: SearchRule) -> State:
        new_state = State(self.magic_square, super().parent,
                          self.current_magic_square_number + 1)

        if self.magic_square[rule.row][rule.column] is not 0:
            new_state.valid = False
            return new_state

        new_state.magic_square[rule.row][rule.column] = new_state.current_magic_square_number

        row_sum, column_sum, primary_diagonal_sum, secondary_diagonal_sum = 0
        row_count, column_count, primary_diagonal_count, secondary_diagonal_count = 0

        for i in range(0, new_state.magic_square_size):
            row_sum += new_state.magic_square[rule.row][i]
            column_sum += new_state.magic_square[i][rule.column]
            primary_diagonal_sum += new_state.magic_square[i][i]
            secondary_diagonal_sum += new_state.magic_square[i][new_state.magic_square_size - i - 1]

            row_count += 1 if new_state.magic_square[rule.row][i] is not 0 else 0
            column_count += 1 if new_state.magic_square[i][rule.column] is not 0 else 0
            primary_diagonal_count += 1 if new_state.magic_square[i][i] is not 0 else 0
            secondary_diagonal_count += 1 if new_state.magic_square[i][new_state.magic_square_size - i - 1] is not 0 else 0

        new_state.valid = not (
            row_count == 2 and row_sum < 6) or (
            column_count == 2 and column_sum < 6) or (
            row_count == 3 and row_sum != 15) or (
            column_count == 3 and column_sum != 15) or (
            primary_diagonal_count == 3 and primary_diagonal_sum != 15) or (
            secondary_diagonal_count == 3 and secondary_diagonal_sum != 15)

        return new_state

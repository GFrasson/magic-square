from __future__ import annotations

from MagicSquare.Square import Square
from MagicSquare.SearchRule import SearchRule


class State:
    instance_count = 0
    
    def __init__(self, magic_square: Square = None, parent: State = None) -> None:
        self.__children: list[State] = []
        self.__parent: State = parent
        self.__level = 0
        self.__horizontal_level = 0

        if self.__parent:
            self.__level = self.parent.level + 1
            self.__horizontal_level = self.parent.horizontal_level + len(self.parent.children)
            self.__parent.append_child(self)

        if magic_square:
            self.__magic_square: Square = Square(magic_square.square, magic_square.current_number)
        else:
            self.__magic_square: Square = Square()

        self.__magic_square_size = len(self.__magic_square.square[0])
        self.__current_rule_index = 0

        self.__instance_index = State.instance_count
        State.instance_count += 1

    @property
    def magic_square(self) -> Square:
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
    def children(self) -> list[State]:
        return self.__children

    @property
    def parent(self) -> State:
        return self.__parent

    @property
    def instance_index(self) -> int:
        return self.__instance_index

    @property
    def level(self) -> int:
        return self.__level
    
    @property
    def horizontal_level(self) -> int:
        return self.__horizontal_level

    @property
    def real_cost(self) -> int:
        return self.level + self.horizontal_level
    
    @property
    def heuristic_cost(self) -> int:
        cost = 0
        even_positions = [
            (0, 0),
            (0, 2),
            (2, 0),
            (2, 2)
        ]

        odd_positions = [
            (0, 1),
            (1, 0),
            (1, 2),
            (2, 1)
        ]

        for even_position in even_positions:
            magic_square_number = self.magic_square.square[even_position[0]][even_position[1]]

            if magic_square_number == 0:
                continue

            if magic_square_number % 2 != 0:
                cost += 10
        
        for odd_position in odd_positions:
            magic_square_number = self.magic_square.square[odd_position[0]][odd_position[1]]
            
            if magic_square_number == 0:
                continue

            if magic_square_number % 2 == 0:
                cost += 10
        
        magic_square_number_middle = self.magic_square.square[1][1]
        if magic_square_number_middle != 0 and magic_square_number_middle != 5:
            cost += 10

        return cost

    @property
    def evaluation_function_a_star(self) -> int:
        return self.real_cost + self.heuristic_cost

    def get_child(self, position: int) -> State | None:
        try:
            return self.children[position]
        except IndexError:
            return None

    def append_child(self, value: State) -> None:
        self.children.append(value)
    
    def __remove_last_child(self) -> None:
        if len(self.children):
            self.children.pop()

    def __update_current_rule_index(self) -> None:
        self.__current_rule_index += 1

    def visit_new_state(self, rule: SearchRule) -> State | None:
        self.__update_current_rule_index()

        new_state = State(self.magic_square, self)

        if new_state.magic_square.square[rule.row][rule.column] != 0:
            self.__remove_last_child()
            return None

        new_state.magic_square.insert_next_number(rule.row, rule.column)

        row_sum, column_sum, primary_diagonal_sum, secondary_diagonal_sum = [0, 0, 0, 0]
        row_count, column_count, primary_diagonal_count, secondary_diagonal_count = [0, 0, 0, 0]

        for i in range(0, new_state.magic_square_size):
            row_sum += new_state.magic_square.square[rule.row][i]
            column_sum += new_state.magic_square.square[i][rule.column]
            primary_diagonal_sum += new_state.magic_square.square[i][i]
            secondary_diagonal_sum += new_state.magic_square.square[i][new_state.magic_square_size - i - 1]

            row_count += 1 if new_state.magic_square.square[rule.row][i] != 0 else 0
            column_count += 1 if new_state.magic_square.square[i][rule.column] != 0 else 0
            primary_diagonal_count += 1 if new_state.magic_square.square[i][i] != 0 else 0
            secondary_diagonal_count += 1 if new_state.magic_square.square[i][new_state.magic_square_size - i - 1] != 0 else 0

        new_state_invalid = (
            row_count == 2 and row_sum < 6) or (
            column_count == 2 and column_sum < 6) or (
            primary_diagonal_count == 2 and primary_diagonal_sum < 6) or (
            secondary_diagonal_count == 2 and secondary_diagonal_sum < 6) or (
            row_count == 3 and row_sum != 15) or (
            column_count == 3 and column_sum != 15) or (
            primary_diagonal_count == 3 and primary_diagonal_sum != 15) or (
            secondary_diagonal_count == 3 and secondary_diagonal_sum != 15)

        if new_state_invalid:
            self.__remove_last_child()
            return None

        return new_state
    
    def is_objective(self) -> bool:
        for i in range(0, self.magic_square_size):
            row_sum = sum(self.magic_square.square[i])
            column_sum = sum([self.magic_square.square[j][i] for j in range(0, self.magic_square_size)])

            if row_sum != 15 or column_sum != 15:
                return False
        
        primary_diagonal_sum = sum([self.magic_square.square[i][i] for i in range(0, self.magic_square_size)])
        secondary_diagonal_sum = sum([self.magic_square.square[i][self.magic_square_size - i - 1] for i in range(0, self.magic_square_size)])
        
        if primary_diagonal_sum != 15 or secondary_diagonal_sum != 15:
            return False
        
        return True

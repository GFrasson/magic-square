from queue import Queue

from SearchRule import SearchRule
from SearchTree import SearchTree
from State import State


class Search:
    def __init__(self, magic_square_size=3, rules_desc=False) -> None:
        self.__tree = SearchTree()
        self.__rules: list[SearchRule] = list()

        for x in range(0, magic_square_size):
            for y in range(0, magic_square_size):
                self.__rules.append(SearchRule(x, y))
        
        if rules_desc:
            self.__rules = self.__rules[::-1]

    @property
    def tree(self) -> SearchTree:
        return self.__tree

    @property
    def rules(self) -> list[SearchRule]:
        return self.__rules

    def __get_next_rule(self, state: State) -> SearchRule:
        try:
            return self.rules[state.current_rule_index]
        except IndexError:
            return None

    def backtracking_search(self) -> State:
        current_state = self.tree.root
        new_state: State = None
        success = False

        while not success:
            while not new_state:
                next_rule = self.__get_next_rule(current_state)

                if next_rule:
                    new_state = current_state.visit_new_state(next_rule)
                else:
                    # Deadlock state
                    current_state = current_state.parent
                    new_state = None

            if new_state.is_objective():
                success = True
            else:
                current_state = new_state
                new_state = None

        return new_state

    def breadth_search(self) -> State:
        open_states_queue: Queue[State] = Queue()
        closed_states: list[State] = []
        
        open_states_queue.put(self.tree.root)

        new_state: State = None
        success = False

        while not success:
            current_state = open_states_queue.get()

            if current_state.is_objective():
                success = True
            else:
                while True:
                    next_rule = self.__get_next_rule(current_state)

                    if next_rule:
                        new_state = current_state.visit_new_state(next_rule)

                        if new_state:
                            open_states_queue.put(new_state)
                    else:
                        closed_states.append(current_state)
                        break

        return current_state

    def depth_search(self):
        pass

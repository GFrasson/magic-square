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
            next_rule = self.rules[state.current_rule_index]
            state.update_current_rule_index()
            
            return next_rule
        except IndexError:
            return None

    def backtracking_search(self):
        current_state = self.tree.root
        failure = False
        success = False

        while not failure or not success:
            pass

    def breadth_search(self):
        pass

    def depth_search(self):
        pass

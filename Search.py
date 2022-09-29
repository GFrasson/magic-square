from SearchRule import SearchRule
from SearchTree import SearchTree

class Search:
    def __init__(self, magic_square_size=3, rules_desc=False) -> None:
        self.__tree = SearchTree()
        self.__current_rule = 0
        self.__rules: list[SearchRule] = list()

        for x in range(0, magic_square_size):
            for y in range(0, magic_square_size):
                self.__rules.append(SearchRule(x, y))
        
        if rules_desc:
            self.__rules = self.__rules[::-1]

    @property
    def current_rule(self) -> int:
        return self.__current_rule

    @property
    def tree(self) -> SearchTree:
        return self.__tree

    @property
    def rules(self) -> list[SearchRule]:
        return self.__rules

    def __get_next_rule(self) -> SearchRule:
        try:        
            next_rule = self.rules[self.current_rule]
            self.__update_current_rule()
            
            return next_rule
        except IndexError:
            return None

    def __update_current_rule(self) -> None:
        self.current_rule += 1
        if self.current_rule >= len(self.__rules):
            self.current_rule = 0

    def backtracking_search(self):
        failure = False
        success = False

        while not failure or not success:
            pass

    def breadth_search(self):
        pass

    def depth_search(self):
        pass

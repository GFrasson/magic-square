import pydot
from queue import Queue
from os import path, mkdir

from MagicSquare.SearchRule import SearchRule
from MagicSquare.SearchTree import SearchTree
from MagicSquare.State import State


class Search:
    def __init__(self, magic_square_size=3, rules_desc=False) -> None:
        self.__graph = pydot.Dot("search_tree", graph_type="digraph")
        self.__output_dir_path = path.join(path.curdir, 'search_trees_output')

        if not path.exists(self.__output_dir_path):
            mkdir(self.__output_dir_path)

        self.__tree = SearchTree()
        self.__rules: list[SearchRule] = list()
        self.__rules_desc = rules_desc

        for x in range(0, magic_square_size):
            for y in range(0, magic_square_size):
                self.__rules.append(SearchRule(x, y))
        
        if self.__rules_desc:
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

                    if new_state:
                        self.__graph.add_node(pydot.Node(new_state.magic_square.__str__(), shape="box"))
                        self.__graph.add_edge(pydot.Edge(new_state.parent.magic_square.__str__(), new_state.magic_square.__str__()))
                else:
                    # Deadlock state
                    current_state = current_state.parent
                    new_state = None

            if new_state.is_objective():
                success = True
            else:
                current_state = new_state
                new_state = None

        file_path = path.join(self.__output_dir_path, f"backtracking-search-tree-{'desc' if self.__rules_desc else 'asc'}.png")
        self.__graph.write_png(file_path)
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
                            self.__graph.add_node(pydot.Node(new_state.magic_square.__str__(), shape="box"))
                            self.__graph.add_edge(pydot.Edge(new_state.parent.magic_square.__str__(), new_state.magic_square.__str__()))
                    else:
                        closed_states.append(current_state)
                        break

        file_path = path.join(self.__output_dir_path, f"breadth-search-tree-{'desc' if self.__rules_desc else 'asc'}.png")
        self.__graph.write_png(file_path)
        return current_state

    def depth_search(self):
        open_states_stack: list[State] = []
        closed_states: list[State] = []
        
        open_states_stack.append(self.tree.root)

        new_state: State = None
        success = False

        while not success:
            current_state = open_states_stack.pop()

            if current_state.is_objective():
                success = True
            else:
                while True:
                    next_rule = self.__get_next_rule(current_state)

                    if next_rule:
                        new_state = current_state.visit_new_state(next_rule)

                        if new_state:
                            open_states_stack.append(new_state)
                            self.__graph.add_node(pydot.Node(new_state.magic_square.__str__(), shape="box"))
                            self.__graph.add_edge(pydot.Edge(new_state.parent.magic_square.__str__(), new_state.magic_square.__str__()))
                    else:
                        closed_states.append(current_state)
                        break

        file_path = path.join(self.__output_dir_path, f"depth-search-tree-{'desc' if self.__rules_desc else 'asc'}.png")
        self.__graph.write_png(file_path)
        return current_state

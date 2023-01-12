from time import time
from enum import Enum
from os import path, mkdir

from MagicSquare.Search import Search


class SearchMethods(Enum):
    BACKTRACKING = 'Busca Backtracking'
    BREADTH = 'Busca em Largura'
    DEPTH = 'Busca em Profundidade'
    ORDERED = 'Busca Ordenada'
    GREEDY = 'Busca Gulosa'
    A_STAR = 'A Estrela'


class RuleOrder(Enum):
    ASC = 'Crescente'
    DESC = 'Decrescente'


def menu(possible_choices: list[str], title) -> int:
    choice: int = None

    while choice not in range(0, len(possible_choices)):
        print(title)

        for i, item in enumerate(possible_choices):
            print(f'[{i}] {item}')

        try:
            choice = int(input('Escolha: '))
        except ValueError:
            print(
                f'Digite um numero de 0 a {len(possible_choices) - 1} para escolher um metodo')

    return choice


def choose_method() -> SearchMethods:
    possible_choices: list[str] = [search_method.value for search_method in SearchMethods]
    choice = menu(possible_choices, 'Metodos de busca:')

    return SearchMethods(possible_choices[choice])


def choose_rules_order() -> RuleOrder:
    possible_choices: list[str] = [rule_order.value for rule_order in RuleOrder]
    choice = menu(possible_choices, 'Ordem de selecao de regras:')

    return RuleOrder(possible_choices[choice])


def get_output_string(open_states, closed_states) -> str:
    output_string = 'Lista de abertos:\n'
    for open_state in open_states:
        output_string += f'Custo: {open_state.priority}\n'
        output_string += f'{open_state.item.magic_square.__str__()}\n\n'
    
    output_string += '\n\nLista de fechados:\n'
    for closed_state in closed_states:
        output_string += f'Custo: {closed_state.priority}\n'
        output_string += f'{closed_state.item.magic_square.__str__()}\n\n'
    
    return output_string


def save_results(filename, content) -> None:
    output_dir = path.join(path.curdir, 'results')
    if not path.exists(output_dir):
        mkdir(output_dir)

    with open(path.join(output_dir, filename), 'w') as file:
        file.write(content)


if __name__ == '__main__':
    chosen_method = choose_method()
    chosen_rule_order = choose_rules_order()
    rules_desc = True if chosen_rule_order is RuleOrder.DESC else False

    search = Search(rules_desc=rules_desc)
    search_methods = {
        SearchMethods.BACKTRACKING: search.backtracking_search,
        SearchMethods.BREADTH: search.breadth_search,
        SearchMethods.DEPTH: search.depth_search,
        SearchMethods.ORDERED: search.ordered_search,
        SearchMethods.GREEDY: search.greedy_search,
        SearchMethods.A_STAR: search.a_star_search,
    }

    chosen_method_function = search_methods[chosen_method]

    start_time = time()
    solution_state, open_states, closed_states = chosen_method_function()
    end_time = time()

    print("Solucao:")
    print(solution_state.magic_square)
    print(f'Custo real: {solution_state.real_cost}')
    print(end_time - start_time, 'seconds')

    file_content = get_output_string(open_states, closed_states)
    save_results(f"{chosen_method.value}-results-{'desc' if rules_desc else 'asc'}.txt", file_content)

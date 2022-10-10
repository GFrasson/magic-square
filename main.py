from time import time

from Search import Search

if __name__ == '__main__':
    start_time = time()

    search = Search()
    solution = search.backtracking_search()
    # solution = search.breadth_search()
    # solution = search.depth_search()
    end_time = time()

    print(solution.magic_square)
    print(end_time - start_time, 'seconds')

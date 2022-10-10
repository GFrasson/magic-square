from Search import Search

if __name__ == '__main__':
    search = Search()
    # solution = search.backtracking_search()
    solution = search.breadth_search()
    # solution = search.depth_search()

    print(solution.magic_square)

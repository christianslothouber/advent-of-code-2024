def read_and_parse_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    grid = [list(line.strip()) for line in lines]

    return grid


def collect_frequencies(grid):
    flat_list = [char for row in grid for char in row if char != '.']

    return set(flat_list)


def collect_pairs(grid, frequency):
    pairs = []

    for x1 in range(len(grid)):
        for y1 in range(len(grid[0])):
            if grid[x1][y1] == frequency:
                for x2 in range(len(grid)):
                    for y2 in range(len(grid[0])):
                        if x1 == x2 and y1 == y2:
                            continue

                        if grid[x2][y2] == frequency:
                            pair = ((x1, y1), (x2, y2))

                            pairs.append(pair)

    return pairs


def calculate_anti_node(pair):
    (x1, y1), (x2, y2) = pair

    dx = x1 - x2
    dy = y1 - y2

    n1 = (x1 + dx, y1 + dy)
    n2 = (x2 - dx, y2 - dy)

    return [n1, n2]


def calculate_harmonic_anti_node(pair, grid):
    n1, n2 = pair
    nodes = [n1, n2]

    x1, y1 = n1
    x2, y2 = n2

    dx = x1 - x2
    dy = y1 - y2

    while is_in_grid(n1, grid) or is_in_grid(n2, grid):
        x1, y1 = n1
        x2, y2 = n2

        n1 = (x1 + dx, y1 + dy)
        n2 = (x2 - dx, y2 - dy)

        nodes.append(n1)
        nodes.append(n2)

    return nodes


def is_in_grid(node, grid):
    x, y = node

    if x < 0 or x >= len(grid):
        return False
    if y < 0 or y >= len(grid[0]):
        return False

    return True


def solve():
    grid = read_and_parse_file('input.txt')
    frequencies = collect_frequencies(grid)
    pair_lists = [collect_pairs(grid, frequency) for frequency in frequencies]
    all_pairs = [pair for row in pair_lists for pair in row]

    anti_nodes_lists = list(map(calculate_anti_node, all_pairs))
    all_anti_nodes = [node for row in anti_nodes_lists for node in row]
    valid_anti_nodes = set(filter(lambda node: is_in_grid(node, grid), all_anti_nodes))
    unique_anti_nodes = len(valid_anti_nodes)

    print(f'Total number of unique anti nodes is {unique_anti_nodes}')

    anti_nodes_lists = list(map(lambda node: calculate_harmonic_anti_node(node, grid), all_pairs))
    all_anti_nodes = [node for row in anti_nodes_lists for node in row]
    valid_anti_nodes = set(filter(lambda node: is_in_grid(node, grid), all_anti_nodes))
    unique_harmonic_anti_nodes = len(valid_anti_nodes)

    print(f'Total number of unique harmonic anti nodes is {unique_harmonic_anti_nodes}')


solve()

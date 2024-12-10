def read_and_parse_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    grid = [list(map(int, line.strip())) for line in lines]

    return grid


def is_in_grid(node, grid):
    x, y = node

    if x < 0 or x >= len(grid):
        return False
    if y < 0 or y >= len(grid[0]):
        return False

    return True


def calculate_targets(position):
    x, y = position

    north = (x, y + 1)
    south = (x, y - 1)
    east = (x + 1, y)
    west = (x - 1, y)

    return [north, south, east, west]


def traverse(position, height, grid, ends):
    if grid[position[0]][position[1]] != height:
        return

    if height == 9:
        if isinstance(ends, set):
            ends.add(position)

        if isinstance(ends, list):
            ends.append(position)

        return

    for target in calculate_targets(position):
        target_x, target_y = target

        if not is_in_grid(target, grid):
            continue

        target_height = grid[target_x][target_y]

        if target_height - height == 1:
            traverse(target, target_height, grid, ends)


def calculate_total_rating(grid):
    trail_rating_sum = 0

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            position = (x, y)
            ends = list()

            traverse(position, 0, grid, ends)

            trail_rating_sum += len(ends)

    return trail_rating_sum


def calculate_total_score(grid):
    trail_score_sum = 0

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            position = (x, y)
            ends = set()

            traverse(position, 0, grid, ends)

            trail_score_sum += len(ends)

    return trail_score_sum


def solve():
    grid = read_and_parse_file('input.txt')

    trail_score_sum = calculate_total_score(grid)

    print(f'Sum of the scores of all trailheads is {trail_score_sum}')

    trail_rating_sum = calculate_total_rating(grid)

    print(f'Sum of the ratings of all trailheads is {trail_rating_sum}')


solve()

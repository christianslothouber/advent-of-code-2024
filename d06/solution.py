def find_guard(grid):
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] in ['^', 'v', '<', '>']:
                direction = grid[x][y]
                grid[x][y] = 'X'

                return x, y, direction


def move_simple(path_grid, guard, target):
    x_guard, y_guard, direction = guard
    x_target, y_target = target

    if is_obstacle(path_grid, target):
        return turn(guard)
    else:
        return x_target, y_target, direction


def move_complex(path_grid, obstacle_grid, guard, target):
    x_guard, y_guard, direction = guard
    x_target, y_target = target

    if is_obstacle(path_grid, target):
        return turn(guard)
    else:
        if obstacle_grid[x_target][y_target] != 'O' and check_loop(path_grid, target, guard):
            print('Found a new obstacle')
            obstacle_grid[x_target][y_target] = 'O'

        path_grid[x_target][y_target] = 'X'

        return x_target, y_target, direction


def check_loop(grid, target, guard):
    x_target, y_target = target
    x_guard, y_guard, direction = guard

    new_grid = copy_grid(grid)
    new_grid[x_target][y_target] = '#'

    current_guard = (x_guard, y_guard, direction)
    current_target = (x_target, y_target)
    moves = []

    while is_valid_position(new_grid, current_target):
        current_guard = move_simple(new_grid, current_guard, current_target)
        current_target = calculate_target(current_guard)

        if current_guard in moves:
            return True

        moves.append(current_guard)

    return False


def turn(guard):
    (x_guard, y_guard, direction) = guard

    if direction == '^':
        return x_guard, y_guard, '>'

    if direction == 'v':
        return x_guard, y_guard, '<'

    if direction == '<':
        return x_guard, y_guard, '^'

    if direction == '>':
        return x_guard, y_guard, 'v'

    raise ValueError(f'Unknown direction of guard: {direction}')


def calculate_target(guard):
    x_guard, y_guard, direction = guard

    if direction == '^':
        return x_guard - 1, y_guard

    if direction == 'v':
        return x_guard + 1, y_guard

    if direction == '<':
        return x_guard, y_guard - 1

    if direction == '>':
        return x_guard, y_guard + 1

    raise ValueError(f'Unknown direction of guard: {direction}')


def is_obstacle(grid, position):
    x, y = position

    return grid[x][y] == '#'


def is_valid_position(grid, position):
    x = position[0]
    y = position[1]

    if x < 0 or x >= len(grid):
        return False
    if y < 0 or y >= len(grid[0]):
        return False

    return True


def copy_grid(grid):
    return [[cell for cell in row] for row in grid]


def copy_obstacle_grid(grid):
    return [['.' for _ in row] for row in grid]


def print_grid(grid):
    for row in grid:
        for cell in row:
            print(cell, end='')
        print()

    print()


def solve():
    with open('test.txt', 'r') as file:
        lines = file.readlines()

    input_grid = [list(line.strip()) for line in lines]

    path_grid = copy_grid(input_grid)
    obstacle_grid = copy_obstacle_grid(path_grid)
    guard = find_guard(path_grid)
    target = calculate_target(guard)

    while is_valid_position(path_grid, target):
        guard = move_complex(path_grid, obstacle_grid, guard, target)
        target = calculate_target(guard)

    visited_positions = sum(cell == 'X' for row in path_grid for cell in row)
    obstacle_positions = sum(cell == 'O' for row in obstacle_grid for cell in row)

    print(f'Visited positions before leaving is {visited_positions}')
    print(f'Found obstacle positions is {obstacle_positions}')


solve()

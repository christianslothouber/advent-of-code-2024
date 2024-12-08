def search_xmas_in_position(grid, position):
    occurrences = 0

    occurrences += search_in_direction(grid, 'XMAS', position, (-1, -1))
    occurrences += search_in_direction(grid, 'XMAS', position, (-1, 0))
    occurrences += search_in_direction(grid, 'XMAS', position, (-1, 1))
    occurrences += search_in_direction(grid, 'XMAS', position, (0, -1))
    occurrences += search_in_direction(grid, 'XMAS', position, (0, 1))
    occurrences += search_in_direction(grid, 'XMAS', position, (1, -1))
    occurrences += search_in_direction(grid, 'XMAS', position, (1, 0))
    occurrences += search_in_direction(grid, 'XMAS', position, (1, 1))

    return occurrences


def search_x_mas_in_position(grid, position):
    (x, y) = position

    p1 = (x - 1, y - 1)
    p2 = (x - 1, y + 1)
    p3 = (x + 1, y - 1)
    p4 = (x + 1, y + 1)

    occurrences = 0
    occurrences += search_in_direction(grid, 'MAS', p1, (1, 1))
    occurrences += search_in_direction(grid, 'MAS', p2, (1, -1))
    occurrences += search_in_direction(grid, 'MAS', p3, (-1, 1))
    occurrences += search_in_direction(grid, 'MAS', p4, (-1, -1))

    if occurrences == 2:
        return 1

    return 0


def search_in_direction(grid, word, position, direction):
    (x, y) = position
    (dx, dy) = direction

    if not is_valid_position(grid, position):
        return 0

    if word[0] != grid[x][y]:
        return 0

    if len(word) == 1:
        return 1

    remaining_word = word[1:]
    new_position = (x + dx, y + dy)

    return search_in_direction(grid, remaining_word, new_position, direction)


def is_valid_position(grid, position):
    (x, y) = position

    if x < 0 or x >= len(grid):
        return False
    if y < 0 or y >= len(grid[0]):
        return False

    return True


def solve():
    with open('input.txt', 'r') as file:
        lines = file.readlines()

    grid = [list(line.strip()) for line in lines]

    xmas_occurrences = 0

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            xmas_occurrences += search_xmas_in_position(grid, (x, y))

    print(f'Total occurrences of XMAS is {xmas_occurrences}')

    x_mas_occurrences = 0

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            x_mas_occurrences += search_x_mas_in_position(grid, (x, y))

    print(f'Total occurrences of X-MAS is {x_mas_occurrences}')


solve()

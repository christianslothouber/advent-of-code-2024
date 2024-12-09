def read_and_parse_file(file_path):
    with open(file_path, 'r') as file:
        disk = file.read()

    disk = list(map(int, disk))

    return disk


def extend_disk(disk):
    file_id = 0
    extended_disk = []

    for index, cell in enumerate(disk):
        if index % 2 == 0:
            extended_disk.extend([file_id] * cell)
            file_id += 1
        else:
            extended_disk.extend([-1] * cell)

    return extended_disk


def block_order_disk(disk):
    reordered_disk = disk.copy()

    for index in range(len(reordered_disk) - 1, -1, -1):
        cell = reordered_disk[index]

        if cell == -1:
            continue

        index_empty = reordered_disk.index(-1)

        if index_empty > index:
            break

        reordered_disk[index_empty] = cell
        reordered_disk[index] = -1

    return reordered_disk


def find_free_slot(disk, size):
    potential_index = 0
    accumulator = 0

    for i in range(len(disk)):
        if disk[i] == -1:
            if accumulator == 0:
                potential_index = i

            accumulator += 1
        else:
            accumulator = 0

        if accumulator >= size:
            return potential_index

    return -1


def move_file(disk, index, size, file_id):
    for i in range(index, index + size):
        disk[i] = file_id


def file_order_disk(disk):
    reordered_disk = disk.copy()
    index = len(reordered_disk) - 1

    while index >= 0:
        cell = reordered_disk[index]

        if cell == -1:
            index -= 1
            continue

        file_size = index - reordered_disk.index(cell) + 1
        free_index = find_free_slot(reordered_disk, file_size)

        if free_index == -1:
            index -= file_size
            continue

        if free_index > index:
            index -= file_size
            continue

        move_file(reordered_disk, free_index, file_size, cell)
        move_file(reordered_disk, index - file_size + 1, file_size, -1)

        index -= file_size

    return reordered_disk


def calculate_checksum(disk):
    checksum = 0

    for index, cell in enumerate(disk):
        if cell == -1:
            continue

        checksum += cell * index

    return checksum


def solve():
    disk = read_and_parse_file('input.txt')
    extended_disk = extend_disk(disk)

    reordered_disk = block_order_disk(extended_disk)
    checksum = calculate_checksum(reordered_disk)

    print(f'The block ordered checksum is {checksum}')

    reordered_disk = file_order_disk(extended_disk)
    checksum = calculate_checksum(reordered_disk)

    print(f'The file ordered checksum is {checksum}')


solve()

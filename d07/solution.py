def read_and_parse_file(file_path):
    parsed_list = []
    with open(file_path, 'r') as file:
        for line in file:
            key, values = line.split(":")
            key = int(key.strip())
            values_list = list(map(int, values.strip().split()))
            parsed_list.append((key, values_list))

    return parsed_list


def is_solvable(equation):
    answer, values = equation

    answers = solve_equation(values)

    return answer in answers


def solve_equation(values):
    if len(values) == 1:
        return values

    head = values[-1]
    tail = values[:-1]

    answers = solve_equation(tail)

    add_values = [head + a for a in answers]
    mul_values = [head * a for a in answers]

    return add_values + mul_values


def is_solvable_complex(equation):
    answer, values = equation

    answers = solve_equation_complex(values)

    return answer in answers


def solve_equation_complex(values):
    if len(values) == 1:
        return values

    head = values[-1]
    tail = values[:-1]

    answers = solve_equation_complex(tail)

    add_values = [a + head for a in answers]
    mul_values = [a * head for a in answers]
    concat_values = [int(str(a) + str(head)) for a in answers]

    return add_values + mul_values + concat_values


def solve():
    equations = read_and_parse_file('input.txt')
    solvable_equations = list(filter(is_solvable, equations))
    total_calibration_result = sum(eq[0] for eq in solvable_equations)

    print(f'Total calibration result is {total_calibration_result}')

    solvable_equations = list(filter(is_solvable_complex, equations))
    total_calibration_result = sum(eq[0] for eq in solvable_equations)

    print(f'Total complex calibration result is {total_calibration_result}')


solve()

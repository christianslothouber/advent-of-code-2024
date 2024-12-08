import re

mul_pattern = r'mul\(\d+,\d+\)'
val_pattern = r'\d+'
code_pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"


def solve_part_1():
    mul_statements = re.findall(mul_pattern, garbage)
    pairs = [re.findall(val_pattern, mul) for mul in mul_statements]
    multiplications = [int(x) * int(y) for x, y in pairs]
    total = sum(multiplications)

    return total


def solve_part_2():
    code_statements = re.findall(code_pattern, garbage)

    total = 0
    enabled = True

    for i in range(len(code_statements)):
        current_statement = code_statements[i]

        if current_statement == 'do()':
            enabled = True
        elif current_statement == "don't()":
            enabled = False
        elif not enabled:
            continue
        else:
            x, y = re.findall(val_pattern, current_statement)
            total += int(x) * int(y)

    return total


with open('input.txt', 'r') as file:
    garbage = file.read()

answer_1 = solve_part_1()

print(f'Sum of valid multiplications is {answer_1}')

answer_2 = solve_part_2()

print(f'Sum of enabled multiplications is {answer_2}')

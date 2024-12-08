import re


def read_file(file_name):
    with open(file_name, 'r') as file:
        blocks = file.read().split('\n\n')

    rule_strings = blocks[0].splitlines()
    rule_pattern = r'\d+|\d+'
    rule_pairs = [re.findall(rule_pattern, rule) for rule in rule_strings]
    rules = [(int(a), int(b)) for a, b in rule_pairs]

    update_strings = blocks[1].splitlines()
    updates = [list(map(int, update.split(','))) for update in update_strings]

    return rules, updates


def complies_with_rule(update, rules):
    for rule in rules:
        (a, b) = rule

        if a in update and b in update:
            index_a = update.index(a)
            index_b = update.index(b)

            if index_a > index_b:
                return False

    return True


def order_with_rules(update, rules):
    for rule in rules:
        (a, b) = rule

        if a in update and b in update:
            index_a = update.index(a)
            index_b = update.index(b)

            if index_a > index_b:
                update[index_a] = b
                update[index_b] = a

                return order_with_rules(update, rules)

    return update


def get_middle_page(update):
    num_of_pages = len(update)
    index_middle = num_of_pages // 2
    middle_page = update[index_middle]

    return middle_page


def solve():
    rules, updates = read_file('input.txt')

    correctly_ordered_updates = filter(lambda update: complies_with_rule(update, rules), updates)
    middle_pages = map(get_middle_page, correctly_ordered_updates)
    sum_of_middle_pages = sum(middle_pages)

    print(f'Sum of middle page numbers of initially correct updates is {sum_of_middle_pages}')

    incorrectly_ordered_updates = filter(lambda update: not complies_with_rule(update, rules), updates)
    fixed_updates = map(lambda update: order_with_rules(update, rules), incorrectly_ordered_updates)
    middle_pages = map(get_middle_page, fixed_updates)
    sum_of_middle_pages = sum(middle_pages)

    print(f'Sum of middle page numbers of initially incorrect updates is {sum_of_middle_pages}')


solve()

def is_safe_strict(report):
    if is_increasing(report) or is_decreasing(report):
        if is_gradual(report):
            return True

    return False


def is_safe_loose(report):
    report_variants = [report[:i] + report[i + 1:] for i in range(len(report))]

    for variant in report_variants:
        if is_safe_strict(variant):
            return True

    return False


def is_gradual(report):
    for i in range(1, len(report)):
        difference = abs(report[i - 1] - report[i])

        if not (1 <= difference <= 3):
            return False

    return True


def is_increasing(report):
    for i in range(1, len(report)):
        if report[i] < report[i - 1]:
            return False

    return True


def is_decreasing(report):
    for i in range(1, len(report)):
        if report[i] > report[i - 1]:
            return False

    return True


with open('input.txt', 'r') as file:
    reports = [list(map(int, line.split())) for line in file]

strict_results = [is_safe_strict(report) for report in reports]
amount_of_strict_safe_reports = sum(strict_results)

print(f'Number of strict safe reports is {amount_of_strict_safe_reports}')

loose_results = [is_safe_loose(report) for report in reports]
amount_of_loose_safe_reports = sum(loose_results)

print(f'Number of loose safe reports is {amount_of_loose_safe_reports}')

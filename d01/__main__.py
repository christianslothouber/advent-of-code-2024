with open('input.txt', 'r') as file:
    left_column = []
    right_column = []

    for line in file:
        left, right = map(int, line.split())

        left_column.append(left)
        right_column.append(right)

left_column_sorted = sorted(left_column)
right_column_sorted = sorted(right_column)

pairs = list(zip(left_column_sorted, right_column_sorted))
differences = [abs(pair[0] - pair[1]) for pair in pairs]

total_distance = sum(differences)

print(f'Total distance is {total_distance}')

buckets = {}

for value in right_column:
    if value not in buckets:
        buckets[value] = []

    buckets[value].append(value)

similarities = [len(buckets.get(value, [])) * value for value in left_column]

total_similarity = sum(similarities)

print(f'Total similarity is {total_similarity}')

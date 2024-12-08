from collections import Counter

with open('input.txt', 'r') as file:
    left_column, right_column = zip(*(map(int, line.split()) for line in file))

left_column_sorted = sorted(left_column)
right_column_sorted = sorted(right_column)
pairs = zip(left_column_sorted, right_column_sorted)
distances = [abs(left - right) for left, right in pairs]
total_distance = sum(distances)

print(f'Total distance is {total_distance}')

buckets = Counter(right_column)
similarities = [buckets[value] * value for value in left_column]
total_similarity = sum(similarities)

print(f'Total similarity is {total_similarity}')


def solve(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()

    items_greater = []
    items_lower = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    return solve(items_lower) + [pivot] + solve(items_greater)

print(solve([]))
sorted([1, 4, 1, 5])

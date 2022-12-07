from functools import reduce

points = {c: p for p, c in enumerate('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', start=1)}

def version_1():
    f = open('./input.txt', 'r')
    total = 0
    for line in f.readlines():
        line = line[:-1]
        half = len(line) // 2
        A, B = line[:half], line[half:]
        A, B = set(A), set(B)
        common = A.intersection(B)
        total += sum(points[item] for item in common)

def find_common_item(itemLists: list[str]):
    return reduce(lambda x, y: x.intersection(y), (set(itemList) for itemList in itemLists))

def version_2():
    f = open('./input.txt', 'r')
    buffer = []
    total = 0
    for line in f.readlines():
        line = line[:-1]
        buffer.append(line)
        if len(buffer) == 3:
            items = find_common_item(buffer)
            for item in items:
                total += points[item]
            buffer = []

    return total

total = version_2()
print(total)
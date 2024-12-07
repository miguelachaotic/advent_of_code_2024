data = [*map(int, open('day1/input.txt').read().split())]
A, B = sorted(data[0::2]), sorted(data[1::2])
print("Part 1:", sum(map(lambda a, b: abs(a-b), A, B)),
      "\nPart 2:", sum(map(lambda a: a * B.count(a), A)))
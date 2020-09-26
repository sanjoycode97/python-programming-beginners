pattern = [
    [1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0],
    [1, 1, 0, 0, 0],
    [1, 0, 0, 0, 0]
]
for row in range(len(pattern)):
    for col in range(len(pattern[row])):
        print(pattern[row][col],end=' ')
    print()

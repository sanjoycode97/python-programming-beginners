#matrix is 2d or multi dimensional lists
matrix=[
    [1,2],
    [2,4],
    [7,8]
]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j],end=" ")
    print()
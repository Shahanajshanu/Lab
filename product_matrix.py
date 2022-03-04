a = [
    [1, 3, 2],
    [3, 1, 1],
    [1, 2, 2]
]

b = [
    [2, 1, 1],
    [1, 0, 1],
    [1, 3, 1]
]

row1 = len(a)
col1 = len(a[0])

row2 = len(b)
col2 = len(b[0])

if (col1 != row2):
    print("Matrix cannot be multiplied")
else:
    prod = [[0] * row1 for i in range(col2)]

for i in range(0, row1):
    for j in range(0, col2):
        for k in range(0, row2):
            prod[i][j] =  prod[i][j] + a[i][k] * b[k][j]

print("Product of two matrices: ")
for i in range(0, row1):
    for j in range(0, col2):
        print(prod[i][j]),
        print(" ")                
# Write Python Program to Add Two Matrices

matrix_1 = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

matrix_2 = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

matrix_result = [[0, 0, 0],
                 [0, 0, 0],
                 [0, 0, 0]]

for rows in range(len(matrix_1)):
    for columns in range(len(matrix_2[rows])):
        matrix_result[rows][columns] = matrix_1[rows][columns] + matrix_2[rows][columns]

print("Addition of two matrices is")

for items in matrix_result:
    print(items)

# Output
# Addition of two matrices is
# [2, 4, 6]
# [8, 10, 12]
# [14, 16, 18]
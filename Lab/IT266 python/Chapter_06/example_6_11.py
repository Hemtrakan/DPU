# Write a Program to Find the Transpose of a Matrix

matrix = [[10, 20],
          [30, 40],
          [50, 60]]

matrix_transpose = [[0, 0, 0],
                    [0, 0, 0]]

def main():
    for rows in range(len(matrix)):
        print(rows)
        for columns in range(len(matrix[rows])):
            print(f"columns : {matrix[rows][columns]}")
            matrix_transpose[columns][rows] = matrix[rows][columns]
    
    print("Transposed Matrix is")
    
    for items in matrix_transpose:
        print(items)

if __name__ == "__main__":
    main()

# Output
# Transposed Matrix is
# [10, 30, 50]
# [20, 40, 60]
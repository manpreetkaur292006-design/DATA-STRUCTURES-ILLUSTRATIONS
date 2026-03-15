
# ARRAY 2D (MATRIX TRAVERSAL + OPERATIONS)

# PRACTISING 2D ARRAYS FOR REAL-WORLD TABULAR DATA AND UNDERSTAND TRAVERSAL COMPLEXITY.

# 2-D ARRAY : A two-dimensional (2D) array is an array of arrays, organizing data into rows and columns like
#             a table or matrix. Elements are accessed using two indices: one for the row and one for the column.

# ANSWER : 

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

def row_sums(matrix):
    print("\nRow Sums:")
    for i, row in enumerate(matrix):
        total = sum(row)
        print(f"Row {i}: {total}")

def column_sums(matrix):
    if not matrix or not matrix[0]:
        print("Empty matrix")
        return
    cols = len(matrix[0])
    print("\nColumn Sums:")
    for j in range(cols):
        total = sum(matrix[i][j] for i in range(len(matrix)))
        print(f"Col {j}: {total}")

def search_value(matrix, target):
    print(f"\nSearch for {target}:")
    found = False
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == target:
                print(f"Found at position ({i}, {j})")
                found = True
                return  # Stop after first match
    if not found:
        print("Not found")

def transpose(matrix):
    if not matrix or not matrix[0]:
        print("\nTranspose: Empty")
        return
    rows, cols = len(matrix), len(matrix[0])
    trans = [[matrix[i][j] for i in range(rows)] for j in range(cols)]
    print("\nTranspose Preview:")
    print_matrix(trans)

# Main demo matrix
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

print("Original Matrix:")
print_matrix(matrix)

row_sums(matrix)
column_sums(matrix)
search_value(matrix, 7)
transpose(matrix)

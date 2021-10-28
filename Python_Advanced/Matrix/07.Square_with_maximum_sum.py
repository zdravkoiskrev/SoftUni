(n, c) = [int(i) for i in input().split(", ")]

matrix = []

for _ in range(n):
    elements = [int(i) for i in input().split(", ")]
    matrix.append(elements)


def get_sum_of_submatrix(matrix, row_index, column_index, size):
    the_sum = 0
    for r in range(row_index, row_index + size):
        for s in range(column_index, column_index + size):
            the_sum += matrix[r][s]
    return the_sum


def get_best_submatrix_sum(matrix, submatrix_size):
    best_row_index = 0
    best_column_index = 0
    best_sum = get_sum_of_submatrix(matrix, 0, 0, submatrix_size)

    for row_index in range(len(matrix) - submatrix_size + 1):
        for col_index in range(len(matrix[row_index]) - submatrix_size + 1):
            current_sum = get_sum_of_submatrix(matrix, row_index, col_index, submatrix_size)
            if best_sum < current_sum:
                best_sum = current_sum
                best_row_index = row_index
                best_column_index = col_index

    return (best_row_index, best_column_index)


def print_result(coordinates, size):
    (row_index, col_index) = coordinates
    for r in range(row_index, row_index + size):
        row = []
        for c in range(col_index, col_index + size):
            row.append(matrix[r][c])
        print(" ".join(str(x) for x in row))
    print(get_sum_of_submatrix(matrix, row_index, col_index, size))


submatrix_size = 2
print_result(get_best_submatrix_sum(matrix, submatrix_size), submatrix_size)

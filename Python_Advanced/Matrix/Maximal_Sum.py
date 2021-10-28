(rows, columns) = [int(i) for i in input().split(" ")]

matrix = []

for _ in range(rows):
    row = [int(i) for i in input().split(" ")]
    matrix.append(row)

maximum_sum = 0

maximum_sum_elements = []
for i in range(rows - 2):
    for s in range(columns - 2):
        square_sum = matrix[i][s] + matrix[i][s + 1] +\
            matrix[i][s + 2] + matrix[i + 1][s] + matrix[i + 1][s + 1] +\
            matrix[i + 1][s + 2] + matrix[i + 2][s] + matrix[i + 2][s + 1] + matrix[i + 2][s + 2]
        if square_sum > maximum_sum:
            maximum_sum = square_sum
            maximum_sum_elements = [[matrix[i][s], matrix[i][s + 1], matrix[i][s + 2]],
                                    [matrix[i + 1][s], matrix[i + 1][s + 1],
                                    matrix[i + 1][s + 2]], [matrix[i + 2][s], matrix[i + 2][s + 1], matrix[i + 2][s + 2]]]

print(f"Sum = {maximum_sum}")
for p in maximum_sum_elements:
    line_to_print = [str(i) for i in p]
    line_to_print = " ".join(line_to_print)
    print(line_to_print)



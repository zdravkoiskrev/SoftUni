(rows, columns) = [int(i) for i in input().split(", ")]

new_matrix = []

for _ in range(rows):
    row_elements = [int(i) for i in input().split(" ")]
    new_matrix.append(row_elements)

for _ in range(columns):
    elements_column_sum = 0
    for i in range(rows):
        elements_column_sum += new_matrix[i][_]
    print(elements_column_sum)


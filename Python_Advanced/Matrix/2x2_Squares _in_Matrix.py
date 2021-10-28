(rows, columns) = [int(i) for i in input().split(" ")]

matrix = []

for _ in range(rows):
    row = [i for i in input().split(" ")]
    matrix.append(row)
counter = 0
for i in range(rows - 1):
    for s in range(columns - 1):
        if matrix[i][s] == matrix[i][s + 1] == matrix[i + 1][s] == matrix[i + 1][s + 1]:
            counter += 1

print(counter)


(rows, cols) = [int(i) for i in input().split()]

snake = input()
matrix = []

for row_index in range(rows):
        matrix.append([0 for el in range(cols)])

index_snake = 0
for row_index in range(rows):
    for col_index in range(cols):
        matrix[row_index][col_index] = snake[index_snake]
        index_snake += 1
        if index_snake == len(snake):
            index_snake = 0

for row_index in range(rows):
    if row_index % 2 == 1:
        matrix[row_index].reverse()
        print("".join(matrix[row_index]))
    else:
        print("".join(matrix[row_index]))


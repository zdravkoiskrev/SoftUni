matrix_sizes = input().split(", ")
rows = int(matrix_sizes[0])
columns = int(matrix_sizes[1])

sum_of_numbers = 0

matrix_itself = []

for _ in range(rows):
    columns_numbers = [int(i) for i in input().split(", ")]
    for i in range(columns):
        sum_of_numbers += columns_numbers[i]

    matrix_itself.append(columns_numbers)


print(sum_of_numbers)
print(matrix_itself)







rows = int(input())

matrix = []

for _ in range(rows):
    elements = [int(i) for i in input().split(", ")]
    matrix.append(elements)

p_diagonal = []
s_diagonal = []
for i in range(rows):
    p_diagonal.append(matrix[i][i])
    s_diagonal.append(matrix[i][rows - 1 - i])

p_diagonal_sum = sum(p_diagonal)
s_diagonal_sum = sum(s_diagonal)

p_diagonal = [str(i) for i in p_diagonal]
s_diagonal = [str(i) for i in s_diagonal]
p_diagonal = ", ".join(p_diagonal)
s_diagonal = ", ".join(s_diagonal)
print(f"Primary diagonal: {p_diagonal}. Sum: {p_diagonal_sum}")
print(f"Secondary diagonal: {s_diagonal}. Sum: {s_diagonal_sum}")
rows = int(input())

matrix = []

for r in range(rows):
    row = [int(i) for i in input().split(" ")]
    matrix.append(row)

command = input()

while not command == "END":
    token = command.split(" ")
    action = token[0]
    cord1 = int(token[1])
    cord2 = int(token[2])
    value = int(token[3])
    if 0 <= cord1 <= (len(matrix) - 1) and 0 <= cord2 <= (len(matrix) - 1):
        if action == "Add":
            matrix[cord1][cord2] += value
        elif action == "Subtract":
            matrix[cord1][cord2] -= value
    else:
        print("Invalid coordinates")
    command = input()

for i in matrix:
    print(*i)


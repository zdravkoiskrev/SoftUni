n = int(input())

square_matrix = []

for i in range(n):
    square_matrix.append(input())

symbol = input()

new_list = []
for i in square_matrix:
    for e in i:
        if symbol in e:
            index_1 = square_matrix.index(i)
            index_2 = i.index(e)
            new_list.append(index_1)
            new_list.append(index_2)

if new_list:
    new_list = [str(i) for i in new_list]
    new_list = ", ".join(new_list)
    print(f"({new_list})")
else:
    print(f"{symbol} does not occur in the matrix")

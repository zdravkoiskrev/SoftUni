n = 6
t = 3
matrix = []
for i in range(n):
    matrix.append([i for i in input().split(" ")])

trows = []

for i in range(t):
    token = input().split("(")
    new_t = token[1].split(")")
    new_tt = new_t[0].split(",")
    trow = int(new_tt[0])
    trow2 = int(new_tt[1])
    trow_coord = [trow, trow2]
    trows.append(trow_coord)

point_collected = 0


for i in trows:
    row = int(i[0])
    col = int(i[1])
    if row < n and col < n:
        if -1 < row and -1 < col:
            basket = matrix[row][col]
            if basket == "B":
                full_collumn = [r[col] for r in matrix]
                for w in full_collumn:
                    if not w == "B":
                        number = int(w)
                        point_collected += number
                matrix[row][col] = "O"

ball = "Football"
teddy = "Teddy Bear"
lego = "Lego Construction Set"


if point_collected < 100:
    points_needed = 100 - point_collected
    print(f"Sorry! You need {points_needed} points more to win a prize.")
elif 100 <= point_collected <= 199:
    print(f"Good job! You scored {point_collected} points, and you've won {ball}.")
elif 200 <= point_collected <= 299:
    print(f"Good job! You scored {point_collected} points, and you've won {teddy}.")
elif 300 <= point_collected:
    print(f"Good job! You scored {point_collected} points, and you've won {lego}.")





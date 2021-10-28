(r, c) = [int(i) for i in input().split()]

for _ in range(r):
    for i in range(c):
        print(f"{chr(97 + _)}{chr(97 + _ + i)}{chr(97 + _)}", end=" ")
    print()
data = input().split("|")

data.reverse()

new_data = []

for i in data:
    token = i.split()
    new_data.append(token)

flattened = [i for s in new_data for i in s]
print(*flattened)
# Input the total number of users.
users = int(input())

# Showing the number of users without duplicates.
actual_users = set()

# Adding the users to the set.
for _ in range(users):
    actual_users.add(input())

# Printing the set.
for person in actual_users:
    print(person)
    
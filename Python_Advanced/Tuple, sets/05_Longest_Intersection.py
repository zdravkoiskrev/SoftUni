n_lines = int(input())

intersections = []

for i in range(n_lines):
    token = input().split("-")
    first = token[0].split(",")
    second = token[1].split(",")
    first_start = int(first[0])
    first_end = int(first[1])
    second_start = int(second[0])
    second_end = int(second[1])
    first_set = set()
    second_set = set()
    for f in range(first_start, first_end + 1):
        first_set.add(str(f))
    for s in range(second_start, second_end + 1):
        second_set.add(str(s))
    third_set = first_set.intersection(second_set)
    intersections.append(third_set)

longest_intersection = max(intersections, key=len)
l_i_list = list(longest_intersection)
l_i_list = [int(i) for i in l_i_list]
l_i_list.sort()
print(f"Longest intersection is {l_i_list} with length {len(l_i_list)}")

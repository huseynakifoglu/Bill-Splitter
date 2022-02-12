# the list with classes; please, do not modify it
groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']

# your code here
groups_dict = dict.fromkeys(groups)

number_of_groups = int(input())
number_of_children = []
for i in range(number_of_groups):
    nums = int(input())
    groups_dict[groups[i]] = nums

if number_of_groups < 9:
    for _ in range(9 - number_of_groups):
        number_of_children.append(None)

print(groups_dict)

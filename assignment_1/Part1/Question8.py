my_set = {1, 3}
print(my_set)
my_set.add(2)
print(my_set)
my_set.update([2, 3, 4])
print(my_set)
my_set.update([4, 5], {1, 6, 8})
print(my_set)

# Out Put
{1, 3}
{1, 2, 3}
{1, 2, 3, 4}
{1, 2, 3, 4, 5, 6, 8}

# Take two lists, say for example these two:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a function that returns a list that contains only the elements that are common between
# the lists (without duplicates). Make sure your function works on two lists of different sizes.

import random
list_1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

common_list = []
for item in list_1:
    if item in list_2 and item not in common_list:
        common_list = [*common_list, item]

print("answer_3:", common_list)

# Extras:
# 3.1. Randomly generate two lists to test this.

list_1 = random.sample(range(0, 50), 20)
list_2 = random.sample(range(0, 50), 15)

common_list = []
for item in list_1:
    if item in list_2 and item not in common_list:
        common_list = [*common_list, item]

print("answer_3.1:", common_list)

# 3.2. Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll
# get to it soon)
list_1 = random.sample(range(0, 50), 20)
list_2 = random.sample(range(0, 50), 15)
common_list = []

[common_list.append(item)
 for item in list_1 if item in list_2 and item not in common_list]

print("answer_3.2:", common_list)

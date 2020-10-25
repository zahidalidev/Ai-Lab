# Take a list, say for example this one:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.

original_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for element in original_list:
    if element < 5:
        print(element)

# Extras:

# 1.1. Instead of printing the elements one by one, make a new list that has all the
# elements less than 5 from this list in it and print out this new list.
copy_list_1 = []
for element in original_list:
    if element < 5:
        copy_list_1.append(element)
print(copy_list_1)

# 1.2. Write this in one line of Python.
copy_list = [element for element in original_list if int(element) < 5]
print(copy_list)

# 1.3. Ask the user for a number and return a list that contains only elements from the
# original list a that are smaller than that number given by the user.
number = int(input('Enter Number: '))

print("\nSmaller Numbers Are:")
for element in original_list:
    if element < number:
        print(element)

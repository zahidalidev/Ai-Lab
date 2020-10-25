# 4.1-  Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)

input_string = input("enter string: ")
reverse_string = input_string[::-1]
if input_string == reverse_string:
    print("string is palindrome")
else:
    print("strign is NOT palindrome")

# 4.2- Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49,
# 64, 81, 100]. Write one line of Python that takes this list a and makes a new list that
# has only the even elements of this list in it.
original_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
even_list = [element for element in original_list if element % 2 == 0]
print("Even element list:", even_list)

# Write a Python program to print all unique values in a dictionary.

list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
        {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]

print("Original List: ", list)

# using set because set can have only uique values
unique_list = set(j for i in list for j in i.values())
print("Unique Values: ", unique_list)

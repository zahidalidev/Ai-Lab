# Write a list comprehension which, from a list, generates a lowercased version of each string
# that has length greater than five.

list = ["ZAHID", "ALI", "ZAHID ALI"]

lower_case_words = [word.lower() for word in list if len(word) > 5]

print(lower_case_words)

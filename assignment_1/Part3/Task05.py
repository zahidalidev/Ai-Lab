# Write a program (using functions!) that asks the user for a long string containing multiple
# words. Print back to the user the same string, except with the words in backwards order. For
# example, say I type the string:
# My name is Michele
# Then I would see the string:
# Michele is name My
# shown back to me.

def reverse_sentence(sentence):
    sentence_list = sentence.split(" ")  # split string on the bases of space
    sentence_list.reverse()  # reversing list
    return ' '.join(sentence_list)  # joining list with spaces


input_sentnce = input("Enter long string: ")
print(reverse_sentence(input_sentnce))

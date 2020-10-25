# Write a Python program to create and display all combinations of letters, selecting each
# letter from a different key in a dictionary. Go to the editor
# Sample data: {'1': ['a', 'b'], '2': ['c', 'd']}

import itertools

# method_1 using itertools

data = {'1': ['a', 'b'], '2': ['c', 'd']}
print("Method_1")
for word in itertools.product(*[data[key] for key in sorted(data.keys())]):
    print(''.join(word))

# method_2 using loops
data = {'1': ['a', 'b'], '2': ['c', 'd']}
list1 = data['1']
list2 = data['2']
print("\nMethod_2")
for j in range(2):
    for i in range(2):
        print(list1[i]+list2[j])

# Find the series of Fibonacci numbers using lambda function.

from functools import reduce

fib_number = int(input("Enter Number:"))
original_list = [0, 1]

any(map(lambda x: original_list.append(
    sum((original_list[-2:]))), range(2, fib_number)))
print("Fibnochi Series:", original_list)

# map in python 
# map()
# Definition: map() applies a given function to all items in an iterable (list, tuple, etc.) and returns a new iterable with the transformed values.
# Syntax: map(function, iterable)

# Question: Given a list of integers, use map() to convert all the 
# numbers into their string representations.
li=[1,2,3,4,5]
def string_convert(n):
    return str(n)

op=map(string_convert,li)
print(list(op))
# ['1', '2', '3', '4', '5']  output


# filter()
# Definition: filter() applies a function that returns True or False to an iterable and keeps only the elements that return True.
# Syntax: filter(function, iterable)

# Use filter() to keep only even numbers from a list of integers.
l = [1, 2, 3, 4, 5]

def is_even(n):
    return n % 2 == 0

result = filter(is_even, l)
print(list(result))  # Output: [2, 4]

# reduce() applies a function cumulatively to the elements in an iterable, reducing it to a single value.
# Syntax: reduce(function, iterable, initial_value)

from functools import reduce

li = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, li)
print(result)  # Output: 15


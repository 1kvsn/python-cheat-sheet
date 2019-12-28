from functools import reduce

# 1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']


def capitalize(item):
    return item.capitalize()


print(list(map(capitalize, my_pets)))

# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]

print(list(zip(my_strings, sorted(my_numbers))))


# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


def overFifty(score):
    return score > 50


print(list(filter(overFifty, scores)))


# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

def add(acc, item):
    return acc + item


print(my_numbers + scores)
print(reduce(add, my_numbers + scores))

# ==============================================

# lambda expressiona

# are one time anonymous functions which we don't need to run more than once

# lambda expression format

# lambda param: action(param)

print(list(map(lambda item: item*2, my_numbers)))

print(list(filter(lambda item: item % 2 != 0, my_numbers)))

print(reduce(lambda acc, item: acc + item, my_numbers))

# EXERCISE

# Use lambda expression and square the items in the list

print(list(map(lambda item: pow(item, 2), my_numbers)))

# List sorting based on second item in a tuple

a = [(0, 2), (4, 3), (9, 9), (10, -1), (4, 16)]

a.sort(key=lambda x: x[1])

# here, the lambda expression is iterating over the tuples and returning 2nd item in the tuple which eventually becomes the key for sort method

print(a)  # [(10, -1), (0, 2), (4, 3), (9, 9), (4, 16)]

# ==================================================================

# List Comprehensions

# are for list, set, dict
# used for quickly creating lists

my_list = [char for char in 'hello']

#          ^^^^char here is the item while for iteration

my_list2 = [num for num in range(0, 100)]
my_list3 = [num**2 for num in range(0, 100)]

#           ^^^^^is here is an expression

my_list4 = [num**2 for num in range(0, 100) if num % 2 == 0]

#                                           [^^^^^^^^^^^^^^ when statement is true]

print(my_list4)

# examples on Set
# remember, sets allows only unique items

your_list = {char for char in 'hello'}

your_list2 = {num for num in range(0, 100)}
your_list3 = {num**2 for num in range(0, 100)}

print(your_list3)

# examples on Dict

simple_dict = {
    'a': 1,
    'b': 2
}

my_dict = {key: value*2 for key, value in simple_dict.items()}

my_dict2 = {key: value*2 for key, value in simple_dict.items() if value %
            2 == 0}

print(my_dict2)

another_dict = {num: num*2 for num in [1, 2, 3]}

#               ^^^^^^^^^makes a key:value

print(another_dict)  # {1: 2, 2: 4, 3: 6}

# EXERCISE

# find duplicates and show them in list

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = list(
    set([char for char in some_list if some_list.count(char) > 1]))

# when result was made in a list, it had duplicate values appearing twice. # ['b', 'b', 'n', 'n']
# wrap it with set() # {'n', 'b'}
# wrap it with list() # ['b', 'n']

print(duplicates)  # ['b', 'n']

# =================================================================

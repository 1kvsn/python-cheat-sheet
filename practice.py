# Fundamental Data Types

# int
# float
# complex
# str
# bool
# list
# tuple
# set
# dict

# ==========================

# print(type(2 + 4)) # int
# print(type(2.5)) # float

# print(2 ** 3) # 2 raised 3.
# print(5 / 4) # 1.25
# print(5 // 4) # floors the return value

# # Math functions (comes from Math module)
# print(round(3.9)) # gets rounded to 4
# print(abs(-20)) # returns absolute value. Means no negative numbers.

# ===========================

# Operator Precedence
# ()
# **
# * /
# + -

# print((5 + 4) * 10 / 2) #45

# print(((5 + 4) * 10) / 2) #45

# print((5 + 4) * (10 / 2)) #45

# print(5 + (4 * 10) / 2) #25

# print(5 + 4 * 10 // 2) #25

# bin returns binary representation of a number.

# print(bin(450))
# print(int('0b111000010', 2)) # converts binary into integer with base 2

# =============================

# rapid assignment of values to variable.
# a, b, c = 1, 2, 3

# print(a)
# print(b)
# print(c)

# ===========================

# Expression Vs Statement

iq = 100  # is a statement
user_age = iq / 5  # is another statement

# here, iq/5 is an expression as it is calculating something.

# However, the whole line user_age = iq / 5 is called a statement as the result of the calculation is being saved into a variable.

# ==============================

# Strings

# triple quotes enables multi-line strings
full_name = """
THIS IS FUN
THIS IS ALSO FUN
"""

# print(full_name);

# ==============================

# Type Conversion

# convert into string
# print(str(100))

# Formatted Strings

name = 'Sasikant'
# print(f'hi {name}')

# using .format() after string

# print('hey {}'.format('Sasikant Nair'))
# print('hey {}'.format(name))

# change name inside .format and then print new name using variable inside {}

# print('hi {new_name}'.format(new_name='Sri Sri'))


# String Manipulation

selfish = 'sasikant'

# reverse a string
# [start:stop:stepover]
# print(selfish[::-2])

# userName = input('Enter User Name ')
# password = input('Enter Password ')
# length = len(password)

# hashed = '*' * length

# print(f'hey {userName}, your password {hashed} is {length} letters long!!')

# Conditional Logic
isOld = 'yes'
isWhite = False

# if isOld and isWhite:
#   print('this is good and true to soul !')
# else:
#   print('this is all fake')

# Ternary operator
# print('Hello there') if isWhite else print('is not white')


# if isOld and isWhite:
#   print('either one is true')
# elif isOld:
#   print('this is elif printed..')


isExpert = False
isMagician = True

# if isMagician and not isExpert:
#   print('you are a magician but not an expert yet!')

# print(True == 1) # True
# print('' == 1) # False
# print([] == 1) # False
# print(10 == 10.0) # True
# print([] == []) # True

# ===============================

# For Loops

# for teddybears in 'Zero To Mastery':
#   print(teddybears);

# here 'Zero To Mastery' is 'ITERABLE

# for item in (1, 2, 3, 4, 5):
#   for x in ['a', 'b', 'c']:
#     print(item, x)

# ITERABLE means a collection or an object which can be iterated over.

# It can be a list, dict, tuple, set, string.

# Looping over objects (Dicts)

user = {
    'name': 'Golem',
    'age': 5030,
    'can_swim': False
}

# gets keys in Dict
# for item in user:
#   print(item)

# for item in user.keys():
#   print(item)


# gets both keys and values in a form of a TUPLE
# for item in user.items():
#   print(item)

# for item in user.items():
#   key, value = item
#   print(key, value)

# OR

# for key, value in user.items():
#   print(key, value)


# for item in user.values():
#   print(item)

# ==================================

# myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# result = 0
# for item in myList:
#   result += item
# print('The total sum is:', result)

# ====================================

# When we don't need the variable, we can use the underscore and access the iterated item

# (start -> stop -> stepover)
# stepover default = 1

# for _ in range(0, 10, 2):
#   print(_)

# reverse range
# for _ in range(10, 0, -1):
#   print(_)

# ================================

# Create a List using range()

# for _ in range(2):
#   print(list(range(10)))

# ================================

# ENUMERATE

# get index and item of enumerated object
# for i, char in enumerate('Hello'):
#   print(i, char)

# enumerate() takes => strings, lists, tuple.

# EXCERCISE

# get index of number 55 in range(100)

# for i, char in enumerate(list(range(100))):
#   if char == 55:
#     print('the index of 55 is:', i)

# ===================================

# WHILE LOOPS

# i = 0
# while i < 10:
#   print(i)
#   i += 1
# break
# we can also have an else condition which runs only when there is NO BREAK. BREAK causes the complete WHILE ELSE BLOCK TO BE SKIPPED...
# else:
#   print('done with while loop')

# =================================

# Exercise!
# Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
# picture = [
#   [0,0,0,1,0,0,0],
#   [0,0,1,1,1,0,0],
#   [0,1,1,1,1,1,0],
#   [1,1,1,1,1,1,1],
#   [0,0,0,1,0,0,0],
#   [0,0,0,1,0,0,0]
# ]

# for row in picture:
#   for pixel in row:
#     if pixel:
#       print("*", end="")
#     else:
#       print(" ", end="")
#   print('')

# ====================================

# EXERCISE
# Check for duplicates in the list:
some_list = ['a', 'b', 'b', 'c', 'm', 'n', 'm']

# duplicates = []
# for item in some_list:
#   if some_list.count(item) > 1 and not item in duplicates:
#     duplicates.append(item)

# print(duplicates)

# =========================

# Functions

# parameters => when we define the function
# arguments => when we call the function

# EXERCISE


def checkDriverAge(age=0):
    # age = input("What is your age?: ")

    if int(age) < 18:
        print("Sorry, you are too young to drive this car. Powering off")
    elif int(age) > 18:
        print("Powering On. Enjoy the ride!")
    elif int(age) == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")

# checkDriverAge(92)

# 1. Wrap the above code in a function called checkDriverAge(). Whenever you call this function, you will get prompted for age.
# Notice the benefit in having checkDriverAge() instead of copying and pasting the function everytime?

# 2 Instead of using the input(). Now, make the checkDriverAge() function accept an argument of age, so that if you enter:
# checkDriverAge(92);
# it returns "Powering On. Enjoy the ride!"
# also make it so that the default age is set to 0 if no argument is given.

# ===============================

# DOC STRINGS: used to document the function


def test(a):
    '''
    Info: This function is useless func!!
    '''
    print(a)

# test('erere')

# print(test.__doc__)

# ================================

# *args **kwargs


def superFunc(*args):
    print(*args)  # returns a tuple when * is removed
    return sum(args)

# print(superFunc(1,2,3,4,5))


def anotherSuperFunc(*args, **kwargs):
    print(kwargs)  # returns a dict when * is removed
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total

# print(anotherSuperFunc(1,2,3,4,5, num1=5, num2=10))

# Rule: params, *args, default params, **kwargs

# =================================


def highestEven(li):
    result = 0
    for item in li:
        if item % 2 == 0 and item > result:
            result = item
    return result


# print(highestEven([10, 2, 3, 4, 6, 11, 13, 22, 43]))

# ========================================

# global keyword can be used inside a function to give it access to the global variable without declaring a new variable for reassignment within the function

# instead of using global keyword, we can use the below technique

total = 0


def count(total):
    total += 1
    return total

# print(count(count(count(0))));

# =====================================

# nonlocal

# def outer():
#   x = "local"
#   def inner():
#     nonlocal x
#     x = 'nonlocal'
#     print('inner:', x)

#   inner()
#   print('outer:', x)

# outer()

# ====================================

from functools import reduce

# 1. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line.

def find_divisible_by_7(start_num, end_num):
    # no particular reason to use set here
    my_set = set()
    for num in range(start_num, end_num + 1):
        if num % 7 == 0 and num % 5 != 0:
            my_set.add(num)
    return print(my_set)

find_divisible_by_7(1, 70)

# using lambda expression

print(list(filter(lambda item: item % 7 == 0 and item % 5 != 0, list(range(1, 70)))))

# another solution

for i in range(1, 70):
    if i % 7 == 0 and i % 5 != 0:
        print(i, end=',')
print("\b")  # for ending the prompt in a new line

# =====================================================================

# 2. Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated sequence on a single line. Suppose the following input is supplied to the program: 8  Then, the output should be: 40320


def find_factorial(n):
    temp = 1
    for i in range(1, n+1):
        temp *= i

    return print(temp)

find_factorial(8)

# using lambda expression

print(reduce(lambda acc, item: acc * item, list(range(1, 9))))

# using recursion

n = int(input())

def fact(x): return 1 if x <= 1 else x*fact(x-1)

print(fact(n))

# ==========================================================================

# 3. With a given integral number n, write a program to generate a dictionary that contains (i, i * i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.Suppose the following input is supplied to the program: 8

# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

# using comprehensions

my_dict = {item: item * item for item in list(range(1, 10))}
print(my_dict)

# ==========================================================================

# 4. Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.Suppose the following input is supplied to the program:

# 34, 67, 55, 33, 12, 98
# Then, the output should be:

# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

def some_func(*args):
    print(str(args))
    print(list(args))

some_func(1, 2, 3)

# ====================================================================================

# 5 Define a class which has at least two methods:
    # getString: to get a string from console input
    # printString: to print the string in upper case.

class some_class:
    def __init__(self):
        pass

    def getString(self):
        self.user_name = input('Enter your name: ')
        
    def printString(self):
        return print(self.user_name.upper())


obj = some_class() # makes a new object using some_class()
# help(obj)
obj.getString()
obj.printString()

# ================================================================================
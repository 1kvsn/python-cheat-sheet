# Decorators

# Functions are first class citizens in Python.

# They act like variables which can be returned from a function and passed as arguments to a function.

# Higher Order Functions are functions which accepts a function as a parameter or returns a function

from time import time


def hello():
    print('hellloooo')


greet = hello  # assigns function to greet variable

del hello  # this deletes the function name from the memory not the function itself. The function is still assigned to another variable greet. So, when we call greet, the function is executed.

# hello is not defined. This error appears because the function name has been deleted.
hello()

print(greet())  # 'hellloooo'

# here we're passing a function and calling that function inside


def say_something(func):
    func()


def say_hello():
    print('hey hello.....')


a = say_something(say_hello)

print(a)  # 'hey hello.....'

# These features make the decorators possible in Python

# =================================================================

# Steps to make a decorator
# 1. define a function which takes a function.
# 2. make a wrapper function which calls the function taken as parameter by decorater function
# Optional: you can add functionality within the wrapper function
# 3. return the wrapper function


def my_decorator(func):
    def wrapper_func():
        print('***********')  # optional functionality
        func()               # calls the function passed as param
        print('***********')
    return wrapper_func


def hello():
    print('helllooooo...')


# =================================
# in layman terms, the above means

a = my_decorator(hello)  # a equals the wrapper function here
a()  # wrapper function gets called here

# ==================================

# or it also means

my_decorator(hello)()
# ^^^^^^^^^^^^^^^^^^first my_decorator(hello) is called. It returns wrapper function which is called again.

# =================================

# or it also means


def my_decorator(func):
    def wrapper_func(*args, **kwargs):
        print('*****')
        func(*args, **kwargs)
        print('*****')
    return wrapper_func


@my_decorator  # hello gets automatically wrapped here when we used @my_decorator
def hello(greeting, emoji=':('):  # default kwarg passed
    print(greeting, emoji)


# just call hello and the @my_decorator will run the wrapper function and it's functionalities along with any params passed into it.
hello('heyaaaaa!!!!')

# If we want our hello() to accept arguments, then there needs to be a way for the wrapper function to accept those arguments and pass it onto the inner function which needs it.

# here comes the use of *args and **kwargs

# we just need to pass *args and **kwargs into wrapper function and inner function which needs it.

# This is called Decorator Pattern

# ==========================================================================

# Lets make our own decorator


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()  # starts the time
        result = fn(*args, **kwargs)
        t2 = time()  # ends calculating time here
        print(f'took {t2 - t1} s')
        return result
    return wrapper


@performance
def long_time_function():
    for i in range(1000000):
        i*5


long_time_function()

# ================================================

# Create an @authenticated decorator that only allows the function to run if user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    # changing this will either run or not run the message_friends function.
    'valid': True
}


def authenticated(fn):
    def wrapper(*args, **kwargs):
        # args gives tuple object
        # access the object using index
        # then access the key 'valid'
        # print(args[0]['valid'])
        if args[0]['valid']:
            return fn(*args, **kwargs)
    return wrapper


@authenticated
def message_friends(user):
    print('message has been sent')


message_friends(user1)

# ========================================================================

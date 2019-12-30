# Error Handling in Python

# Some errors are:

# Type error
# Syntax error
# Name error
# Index error
# Key error
# Value error
# Zero division error

# Find more about these in:
https: // docs.python.org/3/library/exceptions.html

while True:
    try:
        age = int(input('what is your age?'))
        print(age)
        10/age
    # if entered value is not an integer

    except ValueError:
        print('please enter a number')
        continue  # will run the while loop again
    # if we do something with age and it causes zero division error

    except ZeroDivisionError:
        print('please enter age higher than 0')
        break  # will not enter else block

    # runs if try block succeeds
    else:
        print('thank you!')
        # break # breaks out of the while loop after running finally.

    # runs at last no matter what
    finally:
        print('ok, I am finally done')

    print('I am not within try except finally block')

# ===========================================

# Error message should be descriptive
# Error should be caught using their defined type such as TypeError, ValueError etc


def sum(num1, num2):
    try:
        return num1 + num2
    except TypeError as err:
        print(err)


print(sum('1', 2))  # causes TypeError


def sum(num1, num2):
    try:
        return num1/num2
        # club type of errors together
    except (TypeError, ZeroDivisionError) as err:
        print(err)


print(sum('1', 2))  # causes TypeError

# =======================================================================

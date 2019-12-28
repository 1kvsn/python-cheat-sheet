# Generators


def generator_func(num):
    for i in range(num):
        # after yielding i, it pauses and remembers the last yield
        yield i


g = generator_func(10)

# when next(g) is called, the generator_func will pick up from last yield and yields next value until it reaches the last index of range

# when the end is reached, StopIteration error occurs.

# The range() function is a generator and when the range ends, the for loop detects the StopIteration error and stops the loop accordingly. This functionality is hidden away under the hood of for loop

next(g)  # 0
next(g)  # 1

print(next(g))  # 2

# ============================================================

# Print Fibonacci sequence upto n number

# using generator function ( uses less memory as the numbers are yeilded one by one. Only one number is stored in the memory at a time.)


def fib(num):
    a = 0
    b = 1
    for i in range(num):
        yield a
        temp = a
        a = b
        b = temp + a


for x in fib(20):
    print(x)

# =============================================================

# using list (uses more memory as all the output numbers are stored in memory)


def fib2(num):
    a = 0
    b = 1
    result = []
    for i in range(num):
        result.append(a)
        temp = a
        a = b
        b = temp + a
    return result


# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]
print(fib2(20))

# ===============================================================

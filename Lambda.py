# x = lambda a : a + 10
# print(x(5))

# x = lambda a, b : a * b
# print(x(5,6))

# x = lambda a,b,c: a + b + c
# print(x(5,6,2))

# def my_func(n):
#     return lambda a: a * n
# my_doubler = my_func(2)
# print(my_doubler(11))

# def my_func(n):
#     return lambda a: a*n
# my_tripler = my_func(3)
# print(my_tripler(11))


def my_func(n):
    return lambda a: a * n
my_doubler = my_func(2)
my_tripler = my_func(3)
print(my_doubler(11))
print(my_tripler(11))



















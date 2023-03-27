# def square(a):
#     return a * a

# f = lambda a : a * a

# result = square(5)
# result = f(5)

# print(result)


# ####################
# def is_even(n):
#     return n % 2 == 0

from functools import reduce

nums = [3, 2 ,6, 8, 4, 6 , 2, 9]

evens = list(filter(lambda n : n % 2 == 0, nums))

doubles = list(map(lambda n : n * 2, evens))

sum = reduce(lambda a, b: a + b, doubles)

print(evens)
print(doubles)
print(sum)

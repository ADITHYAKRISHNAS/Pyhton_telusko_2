from numpy import *

# arr = array([1, 2, 3, 4, 5.0], int)
# arr = array([1, 2, 3, 4, 5.0], float)
# print(arr)
# print(arr.dtype)


# arr = linspace(0,15,16)
# arr = linspace(0, 9, 10)

# arr = arange(0, 10, 2)

# arr = logspace(1, 40, 5)


# print(arr)

# print('%.2f' %arr[0])
# print('%.2f' %arr[4])

# arr = zeros(5, int)
# arr = ones(5, int)

# print(arr)

# arr = array([1, 2, 3, 4, 5])
# arr2 = array([6, 1, 9, 3, 2])

# arr = arr + 5
# arr3 = arr + arr2

# print(arr)
# print(arr3)
# arr = array([1, 2, 3, 4, 5])
# arr2 = array([6, 1, 9, 3, 2])

# print(sin(arr))
# print(cos(arr))
# print(log(arr))
# print(sqrt(arr))
# print(sum(arr))
# print(min(arr))
# print(max(arr))

# print(concatenate([arr,arr2]))


# arr1 = array([2, 6, 8, 1, 3])

# arr2 = arr1.view()

# arr1[1] = 7

# print(arr1)
# print(arr2)

# print()


# write a code to add 2 arrays using for loop.

# arr = [1, 2, 3, 4, 5] 
# arr2 = [6, 7, 8, 9, 10]
# arr3 = arr([])
# for i in range(len(arr)):
#     arr3[i] = arr[i] + arr2[i]

# print(arr3)

###########################################################

# Matrix

# arr1 = array([
#              [1, 2, 3, 6, 2, 9],
#              [4, 5, 6, 7, 5, 3]

# ])

# arr2 = arr1.flatten()

# arr3 = arr1.reshape(3, 4)
# arr3 = arr1.reshape(2, 2, 3)

# print(arr1)
# print(arr2)
# print(arr3)

# print(arr1.dtype)
# print(arr1.ndim)
# print(arr1.shape)
# print(arr1.size)

##################################################

arr1 = array([
    [1, 2, 3, 6],
    [4, 5, 6, 7],
])

# m = matrix(arr1)
# m = matrix('1 2 3 6 ; 4 5 6 7')
# m = matrix('1 2 ; 3 6 ; 4 5  ; 6 7')
m = matrix('1 2 3; 6 4 5; 1 6 7')
m2 = matrix('1 2 3; 6 8 5; 2 6 7')

print(m)
print(diagonal(m))
print(m.min())
print(m.max())

m3 = m * m2

print(m3)
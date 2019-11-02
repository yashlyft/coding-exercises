# return the index of a character starting from the rightmost character
# note it still returns the index according to the left-to-right order
astring  ='abcdcdba'
astring.index('b')
astring.rindex('b')


# range(0) returns an empty list
list(range(0))  # returns an empty list
list(range(1,2))  # returns 1
list(range(1))  # returns 0

# this construct traverse through the lower left diagonal half of a square without touching the diagonal line
def updateHalf(arr, n):
    for i in range(len(arr)):
        for j in range(i):
            arr[i,j] = n


import numpy as np
test_arr = np.identity(5)
updateHalf(test_arr, 3)
print(test_arr)


# this expression traverse from the end to front
test_list = [1,2,3,4]
test_list[::-1]
list(reversed(test_list))  # same effect as reversed

testArr = [[1,2,3], [4,5,6], [7,8,9]]  # works only on the out most layer
testArr[::-1]


# integer division operator // in Python3 uses floor division where the result is rounded down
-3//2  # gives -2
3//2  # gives 1


# Single * operator means any number of positional arguments
# double ** operator means keyword arguments. Using the keyword as keys of a dictionary
def foo(**kwargs):
    for key in kwargs:
        print(kwargs[key])


foo(arg1=1, arg2=3)

myDict = {'a':1, 'b':2}
foo(**myDict)  # ** helps unpack a dictionary


def bar(*args):
    for a in args:
        print(a)


bar(*test_list)  # * helps unpack a list/tuple

# This will create unintended behavior: if you change [i][j], the value on the other rows will change too.
n = 5
new_arr = [[0] * n] * n
new_arr
new_arr[2][3] = 1
print(new_arr)

# better to use list comprehension
new_arr = [[0 for x in range(n)] for x in range(n)]
new_arr
new_arr[2][3] = 1
print(new_arr)
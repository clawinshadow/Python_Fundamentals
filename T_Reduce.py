from functools import reduce

'''
demos about reduce: functools.reduce(function, iterable[, initializer])
Apply function of two arguments cumulatively to the items of sequence, from left to right,
so as to reduce the sequence to a single value.
For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates ((((1+2)+3)+4)+5)
initializer param indicates whether there is a default value to beginning reduce.

Roughly equivalent to:
def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value
'''

def Sum(x):
    return reduce(lambda x, y: x + y, x)

def Factorial(x):
    return reduce(lambda x, y: x * y, x)

a = range(10)[1:]
print('a: ', list(a))
print('Sum(a): ', Sum(a))
print('Factorial(a): ', Factorial(a))
print('reduce(lambda x, y: x * y, x, initializer=0): ', reduce(lambda x, y: x * y, a, 0))

'''
map(function, iterable, ...)
Return an iterator that applies function to every item of iterable, yielding the results.
If additional iterable arguments are passed, function must take that many arguments
and is applied to the items from all iterables in parallel.
With multiple iterables, the iterator stops when the shortest iterable is exhausted.
'''

a = range(5)
b = range(10)[5:]

print('a: ', list(a))
print('b: ', list(b))
am = map(lambda x: x**2, a)
print('map(lambda x: x**2, a): ', list(am))

# 后面有几个iterable就需要有几个参数在lambda表达式里面
abm = map(lambda x, y: x**2 + y**2, a, b)
print('map(lambda x, y: x**2 + y**2, a, b): ', list(abm))

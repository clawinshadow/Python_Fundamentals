def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element


nested = [[1, 2, 3], [4, 5], [6]]
for e in flatten(nested):
    print(e)

g = (x ** 3 for x in range(1, 10))
print(next(g))
print(next(g))
print(next(g))
print(next(g))


def foo():
    print("begin")
    for i in range(3):
        print("before yield", i)
        yield i
        print("after yield", i)
    print("end")


f = foo()
next(f)
next(f)
next(f)
next(f)

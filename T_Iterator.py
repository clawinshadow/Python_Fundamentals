class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a

    def __iter__(self):
        return self


f = Fibs()
for number in f:
    if number > 1000:
        print(number)
        break

it = iter([1, 2, 3, 4, 5])
print(next(it))
print(next(it))


class LimitedIterator:
    value = 0

    def __next__(self):
        self.value += 1
        if self.value > 10:
            raise StopIteration
        else:
            return self.value

    def __iter__(self):
        return self


li = LimitedIterator()
print(list(li))

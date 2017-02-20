# return a real number between 0 and 1
from random import *

print(random())

print(getrandbits(5))

# return a real number between a and b
print(uniform(10, 20))


# return an integer in range(start, stop, step)
print(randrange(20, 40, 3))


seq = [1, 2, 3, 4, 5, 6]

# return a random element in sequence
print(choice(seq))

# shuffle the sequence in place
print(shuffle(seq))

# return n elements from the sequence
print(sample(seq, 3))

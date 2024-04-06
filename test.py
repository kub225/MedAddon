# test via 'def'
from random import randint

a = randint(0, 7)
b = randint(0, 8)


def count():
    print(a + b)


print(count())

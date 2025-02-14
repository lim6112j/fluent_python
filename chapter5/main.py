from functools import reduce
from operator import add
val = reduce(add, range(100))
print(val)
fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry']
sortval = sorted(fruits, key=lambda word: word[::-1])
print(sortval)
def factorial(n):
    """returns n!"""
    return 1 if n < 2 else n * factorial(n-1)

print(factorial(10))
print([callable(obj) for obj in (abs, str, 13)])
import random
class BingoCage:
    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self, self._items)
    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')
    def __call__(self):
        return self.pick()
    def __len__(self):
        return len(self._items)
bingo = BingoCage(range(3))
bingo.pick()
bingo()

from functools import reduce
from operator import add
val = reduce(add, range(100))
print(val)
fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry']
sortval = sorted(fruits, key=lambda word: word[::-1])
print(sortval)

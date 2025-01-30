import array
#array of sequence
symbols = ['A','T','C','G']
codes = []
for symbol in symbols:
    codes.append(ord(symbol))
# list comprehension
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
# generator expression
aTuple = tuple(ord(symbol) for symbol in symbols)
aArray = array.array('I', (ord(symbol) for symbol in symbols))
# tuples used as records
lax_coordinates = (33.9425, -118.407056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.68, 8014)
traveler_ids = [('USA', '31195855'),('BAA', 'CE342567'), ('ESP', 'XDA205856')]
for passport in sorted(traveler_ids):
    print('%s/%s' % passport)
for country, _ in traveler_ids:
    print(country)
# named tuple
from collections import namedtuple
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))

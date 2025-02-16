registry = []
def register(func):
    print('running register(%s)' % func)
    registry.append(func)
    return func
@register
def f1():
    print('running f1()')
@register
def f2():
    print('running f2()')
def f3():
    print('running f3()')
def main():
    print('running main()')
    print('registry ->', registry)
    f1()
    f2()
    f3()
# closure
class Averager():
    def __init__(self):
        self.series = []
    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total/len(self.series)
# higher order function averager
def make_averager():
    series = []
    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total/len(series)
    return averager
def make_averager2():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total # makes vars not local
        count += 1
        total += new_value
        return total / count
    return averager

# simple clock
import time
from clockdeco import clock

@clock
def snooze(seconds):
    time.sleep(seconds)
@clock
def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)

if __name__ == '__main__':
    main()
    print('*' * 40, 'Calling snooze(.123)')
    snooze(.123)
    print('*' * 40, 'Calling factorial(6)')
    print('6! = ', factorial(6))

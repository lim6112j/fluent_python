registry = []
def register_old(func):
    print('running register(%s)' % func)
    registry.append(func)
    return func

@register_old
def f1():
    print('running f1()')

print('running main()')
print('registry ->',registry)
f1()

registry_new = set()
def register(active=True):
    def decorate(func):
        print("running register(active=%s)->decorate(%s)" % (active, func))
        if active:
            registry_new.add(func)
        else:
            registry_new.discard(func)
        return func
    return decorate

@register(active=False)
def f1():
    print('running f1()')
@register()
def f2():
    print("running f2()")
def f3():
    print("running f3()")

f1()
f2()
f3()
print('registry ->',registry_new)

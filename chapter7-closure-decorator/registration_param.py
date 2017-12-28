"""
为了接受参数，新的 register 装饰器必须作为函数调用
"""


registry = set()


def register(active=True):

    def decorate(func):
        print('running register(active=%s)->decorate(%s)' % (active, func))
        if active:
            registry.add(func)
        else:
            registry.discard(func)
        return func

    return decorate


@register(active=False)
def f1():
    print('running f1()')


@register()
def f2():
    print('running f2()')


def f3():
    print('running f3()')


def main():
    print(registry)
    f1()
    f2()
    f3()
    print(registry)
    register()(f3)()
    print(registry)
    register(active=False)(f2)
    print(registry)

if __name__ == '__main__':
    main()

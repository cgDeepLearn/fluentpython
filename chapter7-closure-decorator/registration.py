# -*- coding: utf-8 -*-
"""
装饰器特性其一：能把被装饰的函数替换成其他函数
其二：在被装饰的函数定义之后立即运行。这通常在Python在加载模块时
"""

registry = []


def register(func):
    print('running register(%s)' % func)
    registry.append(func)
    return func


@register
def func1():
    print('running func1()')


@register
def func2():
    print('running func2()')


def func3():
    print('running func3()')


def main():
    print('running main()')
    print('registry - >', registry)
    func1()
    func2()
    func3()


if __name__ == '__main__':
    main()

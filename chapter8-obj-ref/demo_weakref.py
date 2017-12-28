"""
为了演示对象生命结束时的情形，使用 weakref.finalize 注册一个回调函
数，在销毁对象时调用。
"""


import weakref


def bye():
    print('Gone with the wind...')


def main():
    s1 = {1, 2, 3}
    s2 = s1
    ender = weakref.finalize(s1, bye)
    print(ender.alive)
    del s1
    print(ender.alive)
    s2 = 'spam'
    print(ender.alive)

if __name__ == '__main__':
    main()
# -*- coding: utf-8 -*-
"""
自定义的可调用类型
date:2017/10/19
"""


import random


class BingoCage():
    """
    从打乱的列表中取出一个元素
    """

    def __init__(self, items):
        """用可迭代对象初始化_items"""
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        """弹出一个打乱后的元素"""

        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        return self.pick()  # bingo.pick的 快捷方式是bingo()

if __name__ == '__main__':
    bingo = BingoCage(range(5))
    print(bingo.pick())
    print(bingo())
    print(callable(bingo))

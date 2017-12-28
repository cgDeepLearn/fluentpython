# -*- coding: utf-8 -*-
"""
lotto.py: LotteryBlower是Tombola的具体子类
覆盖了继承的inspect和loaded方法
"""


import random
from tombola import Tombola


class LotteryBlower(Tombola):

    def __init__(self, iterable):
        self._balls = list(iterable)  # 1

    def load(self, iterable):
        self._balls.extend(iterable)

    def pick(self):
        try:
            position = random.randrange((len(self._balls)))  # 2
        except ValueError:
            raise LookupError('pick from empty LotteryBlower')
        return self._balls.pop(position)  # 3

    def loaded(self):  # 4
        return bool(self._balls)

    def inspect(self):  # 5
        return tuple(sorted(self._balls))

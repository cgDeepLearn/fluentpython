# -*- coding: utf-8 -*-
"""
bingo.py
BingoCage是Tombola的具体子类
"""


import random
from tombola import Tombola


class Bingocage(Tombola):
    """Tombola的子类"""

    def __init__(self, items):  # 1
        self._randomizer = random.SystemRandom()  # 2
        self._items = []
        self.load(items)  # 3

    def load(self, items):
        self._items.extend(items)
        self._randomizer.shuffle(self._items)  # 4

    def pick(self):  # 5
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('Pick from empty BingoCage')

    def __call__(self):  # 6
        self.pick()

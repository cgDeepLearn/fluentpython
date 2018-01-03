# -*- coding: utf-8 -*-
"""
Arithmetic Progression等差数列version 0
"""


class ArithmeticProgression:

    def __init__(self, begin, step, end=None):
        self.begin = begin
        self.step = step
        self.end = end  # None ->无穷数列

    def __iter__(self):
        result = type(self.begin + self.step)(self.begin)
        forever = self.end is None
        index = 0
        while forever or result < self.end:
            yield result
            # result += self.step
            index += 1
            result = self.begin + self.step * index

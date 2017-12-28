# -*- coding:utf-8 -*-
"""
vector
"""


from math import hypot


class Vector():
    """vector"""

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        # 或者 return bool(self.x or self.y)
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + self.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


if __name__ == '__main__':

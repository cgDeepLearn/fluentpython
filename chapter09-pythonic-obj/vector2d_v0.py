# -*- coding: utf-8 -*-
"""

A 2-dimensional vector class
# BEGIN VECTOR2D_V0_DEMO
    >>> v1 = Vector2d(3, 4)
    >>> print(v1.x, v1.y)  # <1>
    3.0 4.0
    >>> x, y = v1  # <2>
    >>> x, y
    (3.0, 4.0)
    >>> v1  # <3>
    Vector2d(3.0, 4.0)
    >>> v1_clone = copy.copy(v1)  # <4>
    >>> v1 == v1_clone  # <5>
    True
    >>> print(v1)  # <6>
    (3.0, 4.0)
    >>> octets = bytes(v1)  # <7>
    >>> octets
    b'd\\x00\\x00\\x00\\x00\\x00\\x00\\x08@\\x00\\x00\\x00\\x00\\x00\\x00\\x10@'
    >>> abs(v1)  # <8>
    5.0
    >>> bool(v1), bool(Vector2d(0, 0))  # <9>
    (True, False)

# END VECTOR2D_V0_DEMO
"""


from array import array
import copy
import math


class Vector2d():
    """
    Vector2d类
    """

    typecode = 'd'

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return bytes([ord(self.typecode)]) + bytes(array(self.typecode, self))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    # begin v2
    def angle(self):
        """极坐标"""
        return math.atan2(self.y, self.x)
    """
    简单版__format__
    def __format__(self, fmt_spec=''):
        components = (format(c, fmt_spec) for c in self)
        return '({}, {})'format(*components)
    """

    def __format__(self, fmt_spec=''):
        """加上极坐标的__format__ : p"""
        if fmt_spec.endswith('p'):
            fmt_spec = fmt_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = '<{}, {}>'
        else:
            coords = self
            outer_fmt = '({}, {})'
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(*components)
    # end v2

    # begin vectored_v1
    @classmethod  # 类方法使用classmethod装饰器
    def frombytes(cls, octets):  # 不传入self参数：相反，要通过cls传入类本身
        typecode = chr(octets[0])  # 从第一个字节中读取typecode
        # 使用传入的octets字节序列穿件一个memoryview，然后使用typecoe转换
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)  # 拆包转换后的memryview，得到构造方法所需要的一对参数
    # end vectored_v1


def main():
    v1 = Vector2d(3, 4)
    print(v1.x, v1.y)
    x, y = v1
    print(x, y)
    print(v1)
    v1_clone = copy.copy(v1)
    print(v1_clone == v1)
    octets = bytes(v1)
    print(octets)
    print(abs(v1))
    print(bool(v1), bool(Vector2d(0, 0)))
    # v1
    v1_clone = Vector2d.frombytes(bytes(v1))
    print(repr(v1_clone))
    print(v1_clone == v1)
    # v2
    print(format(Vector2d(1, 1), 'p'))
    print(format(Vector2d(1, 1), '.3ep'))
    print(format(Vector2d(1, 1), '0.5fp'))


if __name__ == '__main__':
    main()

# -* coding: utf-8 -*-
"""
预激协程的装饰器
"""


from functools import wraps


def coroutine(func):
    """装饰器：向前执行到第一个`yield`表达式，预激`func`"""
    @wraps(func)
    def primer(*args, **kwargs):  # 1
        gen = func(*args, **kwargs)  # 2
        next(gen)  # 3
        return gen  # 4
    return primer

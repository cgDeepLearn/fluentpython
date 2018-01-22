# -*- coding: utf-8 -*-

def averager():
    """使用协程计算移动平均值"""
    total = 0.0
    count = 0
    average = None
    while True:  # 1
        term = yield average  # 2
        total += term
        count += 1
        average = total/count
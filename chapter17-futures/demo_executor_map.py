# -*- coding: utf-8 -*-
"""简单演示ThreadPoolExecutor类的map方法"""


from time import sleep, strftime
from concurrent import futures


def display(*args):  # 1
    """打印时间戳"""
    print(strftime('[%H:%M:%S]'), end=' ')
    print(*args)

def loiter(n):  # 2
    """只是在开始时显示一个消息，然后休眠 n 秒，最后在结束时
    再显示一个消息；消息使用制表符缩进，缩进的量由 n 的值确定。
    """
    msg = '{}loiter({}): doing nothing for {}s...'
    display(msg.format('\t'*n, n, n))
    sleep(n)
    msg = '{}loiter({}): done.'
    display(msg.format('\t'*n, n))
    return n * 10  # 3

def main():
    display('Script starting.')
    executor = futures.ThreadPoolExecutor(max_workers=3)  # 4
    results = executor.map(loiter, range(5))  # 5
    display('results:', results)  # 6
    display('waiting for individual results:')
    for i, result in enumerate(results):  # 7
        display('result {}: {}'.format(i, result))

main()
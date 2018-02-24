# -*- coding: utf-8 -*-
"""
spinner_thread.py
通过线程以动画形式显示文本式旋转指
"""


import threading
import itertools
import time
import sys


class Singal():
    go = True


def spin(msg, signal):
    """spin"""
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status))  # 退格
        time.sleep(.1)
        if not signal.go:
            break
    # 使用空格清除状态消息，把光标移回开头。
    write(' ' * len(status) + '\x08' * len(status))


def slow_function():
    # 模拟等待I/O一段时间
    time.sleep(3)
    return 42


def supervisor():
    signal = Singal()
    spinner = threading.Thread(target=spin, args=('thinking!', signal))
    print('spinner object:', spinner)
    spinner.start()
    result = slow_function()
    signal.go = False
    spinner.join()
    return result


def main():
    result = supervisor()
    print('Answer:', result)

if __name__ == '__main__':
    main()

# -*- coding: utf-8 -*-
"""
spinner_asyncio.py
通过协程以动画形式显示文本式旋转指针
"""


import sys
import itertools
import asyncio


# 打算交给 asyncio 处理的协程要使用 @asyncio.coroutine 装饰。
# 这不是强制要求，但是强烈建议这么做。
@asyncio.coroutine
def spin(msg):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status))
        try:
            # 使用 yield from asyncio.sleep(.1) 代替 time.sleep(.1)
            # 这样的休眠不会阻塞事件循环。
            yield from asyncio.sleep(.1)
        except asyncio.CancelledError:
            break
    write(' ' * len(status) + '\x08' * len(status))


@asyncio.coroutine
def slow_function():
    # 现在， slow_function 函数是协程，在用休眠假装进行 I/O 操作时，
    # 使用 yield from 继续执行事件循环。
    yield from asyncio.sleep(3)
    # yield from asyncio.sleep(3) 表达式把控制权交给主循环，在休眠结束后恢复这个协程。
    return 42


@asyncio.coroutine
def supervisor():
    """现在， supervisor 函数也是协程"""
    # asyncio.async(...) 函数排定 spin 协程的运行时间，
    # 使用一个 Task 对象包装spin 协程，并立即返回。
    spinner = asyncio.async(spin('thinking!'))
    # 显示 Task 对象
    print('spinner object:', spinner)
    # 驱动 slow_function() 函数。结束后，获取返回值。同时，事件循环继续运行，
    # 因为slow_function 函数最后使用 yield from asyncio.sleep(3) 表达式把控制权交回给了主循环。
    result = yield from slow_function()
    # Task 对象可以取消；取消后会在协程当前暂停的 yield 处抛出
    # asyncio.CancelledError 异常。协程可以捕获这个异常，也可以延迟取消，甚至拒绝取消。
    spinner.cancel()
    return result


def main():
    loop = asyncio.get_event_loop()  # 获取事件循环的引用
    # 驱动 supervisor 协程，让它运行完毕；这个协程的返回值是这次调用的返回值
    result = loop.run_until_complete(supervisor())
    loop.close()
    print('Answer:', result)


if __name__ == '__main__':
    main()

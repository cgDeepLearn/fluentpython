"""
参数化clock装饰器
"""


import time


DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) ->{result}'


def clock(fmt=DEFAULT_FMT):  # 参数化装饰器工厂函数
    def decorate(func):  # 真正的装饰器
        def clocked(*_args):  # 包装被装饰的函数
            t0 = time.time()
            _result = func(*_args)  # 被装饰的函数返回额真正结果
            elapsed = time.time() - t0
            name = func.__name__
            args = ', '.join(repr(arg)
                             for arg in _args)  # _args是clocked的参数,args是显示用的字符串
            result = repr(_result)  # 字符串表示用于显示
            # 使用**locals(0是为了在fmt中引用clocked的局部变量)
            print(fmt.format(**locals()))
            return _result
        return clocked
    return decorate


def main():
    @clock()
    def snooze(seconds):
        time.sleep(seconds)

    @clock('{name}: {elapsed}s')
    def snooze1(seconds):
        time.sleep(seconds)

    @clock('{name}({args} dt={elapsed:0.3f}s)')
    def snooze2(seconds):
        time.sleep(seconds)

    for _ in range(3):
        snooze(.123)
        snooze1(.456)
        snooze2(.789)

if __name__ == '__main__':
    main()

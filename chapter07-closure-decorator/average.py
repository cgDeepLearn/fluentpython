"""
7-9 函数式实现使用高阶函数mke_averager计算移动平均值
"""


def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)

    return averager


def main():
    avg = make_averager()
    print(avg(10))
    print(avg(11))
    print(avg(12))

if __name__ == '__main__':
    main()
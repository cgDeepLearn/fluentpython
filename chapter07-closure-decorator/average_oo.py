"""
7-8 计算移动平均值的类
"""


class Averager():

    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total / len(self.series)


def main():
    avg = Averager()
    print(avg(10))
    print(avg(11))

if __name__ == '__main__':
    main()

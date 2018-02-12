"""
计算移动平均值，不保存所有历史(使用nonlocal修正)
"""


def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count

    return averager


def main():
    avg = make_averager()
    print(avg(10))
    print(avg(11))

if __name__ == '__main__':
    main()

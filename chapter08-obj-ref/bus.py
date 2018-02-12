# -*- coding:utf-8 -*-
"""
深复制和浅复制
"""

import copy


class Bus():

    def __init__(self, passsengers=None):
        if passsengers is None:
            self.passsengers = []
        else:
            self.passsengers = list(passsengers)

    def pick(self, name):
        self.passsengers.append(name)

    def drop(self, name):
        self.passsengers.remove(name)


def main():
    bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
    bus2 = copy.copy(bus1)
    bus3 = copy.deepcopy(bus1)
    print("id: ", id(bus1), id(bus2), id(bus3))
    bus1.drop('Bill')
    print(bus2.passsengers)
    print(id(bus1.passsengers), id(bus2.passsengers), id(bus3.passsengers))
    print(bus3.passsengers)

if __name__ == '__main__':
    main()

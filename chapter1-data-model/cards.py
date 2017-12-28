# -*- coding:utf-8 -*-
"""
python style data model
"""


import collections
from random import choice


Card = collections.namedtuple('Card', ['rank', 'color'])
color_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


class FrenchDeck():
    """cards"""
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    colors = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, color)
                       for color in FrenchDeck.colors
                       for rank in FrenchDeck.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


def spades_high(card):
    """按照黑桃最大返回卡牌相应rank值"""
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(color_values) + color_values[card.color]


if __name__ == '__main__':
    deck = FrenchDeck()
    for card in sorted(deck, key=spades_high):
        print(card)
    

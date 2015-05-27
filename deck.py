#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import shuffle


class Deck:

    def __init__(self, decks=1):
        """Initialize the deck of cards. Defaults to single deck."""

        if decks < 1:
            raise ValueError('Number of decks must be greater than or equal to 1')

        self.deck = list()

        self.suits = [
            { 'id': 'S', 'name': 'Spades', 'symbol': u'\u2660' },
            { 'id': 'D', 'name': 'Diamonds', 'symbol': u'\u2666' },
            { 'id': 'C', 'name': 'Clubs', 'symbol': u'\u2663' },
            { 'id': 'H', 'name': 'Hearts', 'symbol': u'\u2665' }
        ]

        self.ranks = [
            { 'id': 'A', 'name': 'Ace' },
            { 'id': '2', 'name': 'Two' },
            { 'id': '3', 'name': 'Three' },
            { 'id': '4', 'name': 'Four' },
            { 'id': '5', 'name': 'Five' },
            { 'id': '6', 'name': 'Six' },
            { 'id': '7', 'name': 'Seven' },
            { 'id': '8', 'name': 'Eight' },
            { 'id': '9', 'name': 'Nine' },
            { 'id': '10', 'name': 'Ten' },
            { 'id': 'J', 'name': 'Jack' },
            { 'id': 'Q', 'name': 'Queen' },
            { 'id': 'K', 'name': 'King' }
        ]

        for i in range(0, decks):
            for suit in self.suits:
                for rank in self.ranks:
                    self.deck.append({
                        'id': '{}{}'.format(rank['id'], suit['id']),
                        'face': u'{}{}'.format(rank['id'], suit['symbol']),
                        'name': '{} of {}'.format(rank['name'], suit['name']),
                        'suit': suit['id'],
                        'suit_name': suit['name'],
                        'suit_symbol': suit['symbol'],
                        'rank': rank['id'],
                        'rank_name': rank['name']
                    })


    def shuffle(self, itterations=3):
        """Randomize the order of cards in the deck"""

        for i in range(0, itterations):
            shuffle(self.deck)

        return self.deck


    def draw(self, position=0):
        """Draw the card at 'position' from the deck"""

        return self.deck.pop(position)

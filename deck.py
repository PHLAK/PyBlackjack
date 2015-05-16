#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Deck:

    def __init__(self):

        self.suits = [
            { 'id': 'S', 'name': 'Spades', 'symbol': u'\u2660' },
            { 'id': 'D', 'name': 'Diamonds', 'symbol': u'\u2666' },
            { 'id': 'C', 'name': 'Clubs', 'symbol': u'\u2663' },
            { 'id': 'H', 'name': 'Hearts', 'symbol': u'\u2665' }
        ]

        self.values = [
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


    def create(self):

        deck = list()

        for suit in self.suits:
            for value in self.values:
                deck.append({
                    'id': '{}{}'.format(value['id'], suit['id']),
                    'face': u'{}{}'.format(value['id'], suit['symbol']),
                    'name': '{} of {}'.format(value['name'], suit['name'])
                })

        return deck

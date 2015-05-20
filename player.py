#!/usr/bin/env python
# -*- coding: utf-8 -*-

from hand import Hand

class Player:

    def __init__(self, name):

        self.name = str(name)

        self.hands = [
            Hand()
        ]


    def add_hand(self):
        """Add a Hand object to the players hands"""

        # Add a hand object
        self.hands.append(Hand())

        # Get the index of the newly created hand object
        hand_index = self.hands.index(self.hands[-1])

        return hand_index

        print('Double action')


    def split(self):
        """Player split action"""

        print('Spit action')

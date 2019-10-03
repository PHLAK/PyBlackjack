#!/usr/bin/env python
# -*- coding: utf-8 -*-

from hand import Hand


class Player:

    def __init__(self, name):

        self.player_name = str(name)
        self.player_hands = list()
        self.add_hand()


    def name(self):
        """Returns the player's name"""

        return self.player_name


    def add_hand(self):
        """Add an empty Hand object to the players list of hands"""

        hand = Hand()
        self.player_hands.append(hand)

        return hand

    def hands(self):
        """Returns an ordered list of player hands"""

        return self.player_hands

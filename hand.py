#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re


class Hand:

    def __init__(self, *args):

        self.cards = list()

        if len(args) > 0:
            for arg in list(args):
                self.cards.append(arg)

        self.soft = False


    def add_card(self, card):
        """Add a card to the hand"""

        # Set hand soft status
        if card['rank'] == 'A':
            if (self.score() + 11) <= 21:
                self.set_soft(True)
            else:
                self.set_soft(False)

        # Append card to list
        self.cards.append(card)

        return self.cards


    def remove_card(self, card):
        """Remove a card from the hand"""

        # Remove card from list
        self.cards.remove(card)

        return self.cards


    def str(self):
        """Returns hand as a string"""

        hand_str = str()

        for card in self.cards:
            hand_str += card['face'] + '  '

        return hand_str.rstrip()


    def is_soft(self):
        """Returns True if hand is soft, otherwise returns False"""

        return self.soft


    def set_soft(self, boolean):
        """Set hand soft boolean"""

        self.soft = True


    def score(self):
        """Calculate the score of the hand"""

        # Return 0 if no cards in hand
        if len(self.cards) == 0:
            return 0

        cards = list()

        # Move Aces to the end of the list
        for index, card in enumerate(self.cards):

            if card['rank'] is 'A':
                cards.append(self.cards[index])
            else:
                cards.insert(0, self.cards[index])

        hand_score = int()

        for card in cards:

            if card['rank'] is 'A':

                if hand_score + 11 > 21:
                    hand_score += 1
                else:
                    hand_score += 11

            elif re.match(r'[JQK]', card['rank']):

                hand_score += 10

            else:

                hand_score += int(card['rank'])

        return hand_score

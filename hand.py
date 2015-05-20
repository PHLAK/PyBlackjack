#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re


class Hand:

    def __init__(self, *args):

        self.cards = list()

        if len(args) > 0:
            for arg in list(args):
                self.cards.append(arg)

        self.hard = True


    def add_card(self, card):
        """Add a card to the hand"""

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

                # TODO: Improve this

                if hand_score + 11 > 21:
                    hand_score += 1
                else:
                    hand_score += 11

            elif re.match(r'[JQK]', card['rank']):

                hand_score += 10

            else:

                hand_score += int(card['rank'])

        return hand_score

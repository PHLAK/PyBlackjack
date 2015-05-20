#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from deck import Deck
from player import Player
from random import shuffle

import re
import sys


# Initialize the deck
deck = Deck().create()

# Shuffle the deck
shuffle(deck)


def deal(players, deck):
    """Deal hands to 'players' from 'deck'"""

    for i in range(0, 2):

        index = 0

        for player in players:

            if len(player.hands) == 0:
                index = player.add_hand()

            player.hands[index].add_card(deck.pop(0))


# def blackjack(player):
#   """"Checks if a players hand is a blackjack"""
#     # Check if player has a blackjack


def hit(hand):
    """Hand hit action"""

    print('Hit action')


def stand(hand):
    """Hand stand action"""

    print('Stand action')


def double(hand):
    """Hand double action"""

    print('Double action')


def split(hand):
    """Hand split action"""

    print('Spit action')


def play_hand(player, hand):
    """Run the main gameplay loop for palyers hand"""

    stand = False

    while stand is False:

        # Show player their hand
        print(u'{player}: {hand}'.format(player=player.name, hand=hand.str()))

        # Prompt user for action
        action = raw_input('[H]it | [S]tand | [D]ouble | Split [/]: ')

        if re.match(r'[Hh]', action):

            hit(hand)

        elif re.match(r'[Ss]', action):

            stand = True

        elif re.match(r'[Dd]', action):

            double(hand)

        elif re.match(r'[/]', action):

            double(hand)

        else:

            print('Invalid option: {}'.format(action))


def dealer_play(player, hand):

    print('Dealer play...')


def main(num_players):
    """Main execution function"""

    # Initialize players list
    players = list()

    # Add players to players list
    for i in range(1, num_players + 1):

        players.append(Player('Player{}'.format(i)))

    # Add the dealer to the players list
    players.append(Player('Dealer'))

    # Deal the cards
    deal(players, deck)

    # Show dealers card
    print(u'Dealer showing: {}'.format(players[-1].hands[0].cards[0]['face']))

    # Run player loop
    for player in players:
        for hand in player.hands:

            if player.name is not 'Dealer':
                play_hand(player, hand)

    dealer_play(player, hand)

if __name__ == '__main__':

    if len(sys.argv) < 2:

        num_players = 1

    else:

        num_players = int(sys.argv[1])

        if num_players > 5 or num_players < 1:
            print('ERROR: Number of players must be 1-5', file=sys.stderr)
            exit(1)

    main(num_players)

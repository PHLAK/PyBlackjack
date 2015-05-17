#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from deck import Deck
from random import shuffle

import re
import sys


def initialize_players(number_of_players=1):
    """Initialize player objects"""

    players = list()

    # Add players
    for i in range(1, number_of_players + 1):

        players.append({
            'name': 'Player {}'.format(i),
            'hand': list()
        })

    # Add dealer to players
    players.append({
        'name': 'Dealer',
        'hand': list()
    })

    return players


def initialize_hands():
    """Initialize hands"""

    hands = {
        'cards': list(),
        'status': 'hard'
    }

    return hands


def deal(players, deck):
    """Deal hands to 'players' from 'deck'"""

    for i in range(0, 2):
        for player in players:
            player['hand'].append(deck.pop(0))


def get_player_hand(player):
    """Returns a string of the cards in a players hand"""

    hand = str()

    for card in player['hand']:
        hand += card['face'] + '  '

    return hand


# def blackjack(player):
#   """"Checks if a players hand is a blackjack"""
#     # Check if player has a blackjack


# def hit(player):
#     """Player hit action"""
#     # Hit actions...


# def stand(player):
#     """Player stand action"""
#     # Stand


# def double(player):
#     """Player double action"""
#     # Double actions


# def split(player):
#     """Player split action"""
#     # Split actions


def player_loop(player):
    """Run the main gameplay loop for 'player'"""

    print(u'{}: {}'.format(player['name'], get_player_hand(player)))

    print('[H]it | [S]tand | [D]ouble | Split [/]: ')


def main(num_players):
    """Main execution function"""

    # Initialize the deck
    deck = Deck().create()

    # Shuffle the deck
    shuffle(deck)

    # Initialize the players
    players = initialize_players(num_players)

    # Deal the cards
    deal(players, deck)

    # Run player loop
    for player in players:
        player_loop(player)


if __name__ == '__main__':

    if len(sys.argv) < 2:

        num_players = 1

    else:

        num_players = int(sys.argv[1])

        if num_players > 5:
            print('ERROR: Number of players cannot exceed 5', file=sys.stderr)
            exit(1)

    main(num_players)

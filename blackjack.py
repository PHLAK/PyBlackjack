#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from deck import Deck
from random import shuffle

import re
import sys


def initialize_players(number_of_players=1):

    players = list()

    # Add players
    for i in range(1, number_of_players + 1):

        players.append({
            'name': 'player{}'.format(i),
            'hand': list()
        })

    # Add dealer to players
    players.append({
        'name': 'dealer',
        'hand': list()
    })

    return players


def initialize_hands():

    hands = {
        'cards': list(),
        'status': 'hard'
    }

    return hands


def deal(players, deck):

    for i in range(0, 2):
        for player in players:
            player['hand'].append(deck.pop(0))


# def blackjack(player):
#     # Check if player has a blackjack


# def hit(player):
#     # Hit actions...


# def stand(player):
#     # Stand


# def double(player):
#     # Double actions


# def split(player):
#     # Split actions


def main(num_players):

    # Initialize the deck
    deck = Deck().create()

    # Shuffle the deck
    shuffle(deck)

    print(u'Deck: {}'.format(deck))
    print()

    # Initialize the players
    players = initialize_players(num_players)

    # Deal the cards
    deal(players, deck)

    print('Players: {}'.format(players))
    print()

    for player in players:

        player_hand = str()

        for card in player['hand']:
            player_hand += card['face'] + '  '

        print(player['name'] + ': ' + player_hand)


if __name__ == '__main__':

    if len(sys.argv) < 2:
        num_players = 1
    else:
        num_players = int(sys.argv[1])

    main(num_players)

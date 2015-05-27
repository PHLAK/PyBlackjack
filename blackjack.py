#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from deck import Deck
from player import Player
from random import shuffle

import argparse
import re
import sys


# Initialize the deck
deck = Deck()

# Shuffle the deck
deck.shuffle()


def deal(players, deck):
    """Deal hands to 'players' from 'deck'"""

    for i in range(0, 2):

        index = 0

        for player in players:

            if len(player.hands) == 0:
                index = player.add_hand()

            player.hands[index].add_card(deck.draw())


def show_hand(player, hand):
    """Show player hand and score"""

    hand_str = u'{player}: {hand}  [{score}]'.format(
        player=player.name(), hand=hand.str(), score=hand.score()
    )

    return hand_str


def hit(hand):
    """Draw a card from the deck and add it to the player's hand"""

    hand.add_card(deck.draw())


def split(hand):
    """Hand split action"""

    print('Spit action')


def play_hand(player, hand):
    """Run the main gameplay loop for palyers hand"""

    # Is hand a blackjack?
    if hand.score() == 21:
        blackjack = True
    else:
        blackjack = False

    while True:

        # Show player their hand
        print(show_hand(player, hand))

        if blackjack:
            print('--> {player} has blackjack!'.format(player=player.name()))
            break

        if hand.score() > 21:
            print('--> {player} busts!'.format(player=player.name()))
            break

        # Prompt user for action
        action = raw_input('[H]it | [S]tand | Split [/]: ')

        if re.match(r'[Hh]', action):

            print('--> {player} hits...'.format(player=player.name()))
            hit(hand)

        elif re.match(r'[Ss]', action):
            print('--> {player} stands.'.format(player=player.name()))
            break

        elif re.match(r'[/]', action):
            split(hand)

        else:
            print('Invalid option: {}'.format(action))


def dealer_play(player, hand):

    while True:

        # Show the dealer's hand
        print(show_hand(player, hand))

        if hand.score() > 21:

            print('--> {player} busts!'.format(player=player.name()))
            break

        if hand.score() < 17 or hand.score() == 17 and hand.is_soft() is True:

            print('--> {player} hits...'.format(player=player.name()))
            hit(hand)

        else:

            print('--> {player} stands.'.format(player=player.name()))
            break


def main(num_players):
    """Main execution function"""

    # Initialize players list
    players = list()

    # Add players to players list
    for i in range(1, num_players + 1):
        players.append(Player('Player{}'.format(i)))

    # Add the dealer to the players list
    players.append(Player('Dealer'))

    print(players)

    # Deal the cards
    deal(players, deck)

    # Show dealers card
    print(u'Dealer showing: {}'.format(players[-1].hands[0].cards[0]['face']))

    # Run player loop
    for player in players:
        for hand in player.hands:

            if player.name() is not 'Dealer':
                play_hand(player, hand)

    dealer_play(player, hand)


if __name__ == '__main__':

    # Initialize argument parser
    parser = argparse.ArgumentParser(description='Play Blackjack for teh lulz')

    # Add arguments
    parser.add_argument('-d', '--decks', help='Number of decks (minimum 1)')
    parser.add_argument('-p', '--players', help='Number of non-dealer players (must be 1-5)')

    # Parse passed arguments
    args = parser.parse_args()

    if args.decks:
        num_decks = int(arg.decks)
    else:
        num_decks = 1

    if args.players:
        num_players = int(args.players)
        if num_players > 5 or num_players < 1:
            raise ValueError('Number of players must be 1-5')
    else:
        num_players = 1

    # Run main function
    main(num_players)

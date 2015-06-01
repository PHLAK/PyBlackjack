#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from deck import Deck
from player import Player

import argparse
import re
import sys


def deal(players, deck):
    """Deal hands to 'players' from 'deck'"""

    for i in range(0, 2):
        for player in players:
            for hand in player.hands():
                hand.add_card(deck.draw_one())


def show_hand(player, hand):
    """Show player hand and score"""

    hand_str = u'{player}: {hand}  [{score}]'.format(
        player=player.name(), hand=hand.str(), score=hand.score()
    )

    return hand_str


def hit(hand, deck):
    """Draw a card from the 'deck' and add it to the player's 'hand'"""

    hand.add_card(deck.draw_one())


def is_blackjack(hand):
    """Returns True if hand is a blackjack, otherwise False"""

    if hand.size() == 2 and hand.score() == 21:
        return True

    return False


def split_allowed(hand):
    """Returns True if the hand can be split, otherwise False"""

    if hand.size() == 2 and hand.peek(0)['rank'] == hand.peek(1)['rank']:
        return True

    return False


def play_hand(player, hand, deck):
    """Run the main gameplay loop for palyers hand"""

    # Show player their hand
    print(show_hand(player, hand))

    while True:

        if is_blackjack(hand):
            print('  --> {player} has blackjack!'.format(player=player.name()))
            break

        elif hand.score() > 21:
            print('  --> {player} busts!'.format(player=player.name()))
            break

        prompt = u'  --> [H]it | [S]tand: '

        if split_allowed(hand):
            prompt = u'  --> [H]it | [S]tand | Split [/]: '

        # Prompt user for action
        action = raw_input(prompt)

        if re.match(r'[Hh]', action):

            hit(hand, deck)
            print(u'  --> {player} hits: {hand}  [{score}]'.format(
                player=player.name(),
                hand=hand.str(),
                score=hand.score()
            ))

        elif re.match(r'[Ss]', action):

            print('  --> {player} stands with {score}'.format(
                player=player.name(),
                score=hand.score()
            ))

            break

        elif re.match(r'[/]', action) and split_allowed(hand):

            print('  --> {player} splits hand'.format(
                player=player.name()
            ))

            # Create second player hand
            new_hand = player.add_hand()

            # Move one card into the new hand
            new_hand.add_card(hand.remove_card(-1))

            # Deal new cards to split hands
            for split_hand in player.hands():
                split_hand.add_card(deck.draw_one())

            # Show player their hand
            print(show_hand(player, hand))

        else:
            print('  --> Invalid option')


def dealer_play(player, hand, deck):
    """Run the dealers gameplay loop"""

    # Show the dealer's hand
    print(show_hand(player, hand))

    while True:

        if is_blackjack(hand):
            print('  --> {player} has blackjack!'.format(player=player.name()))
            break

        elif hand.score() > 21:

            print('  --> {player} busts!'.format(player=player.name()))
            break

        elif hand.score() < 17 or hand.score() == 17 and hand.is_soft() is True:

            hit(hand, deck)
            print(u'  --> {player} hits: {hand}  [{score}]'.format(
                player=player.name(),
                hand=hand.str(),
                score=hand.score()
            ))

        else:

            print('  --> {player} stands with {score}'.format(
                player=player.name(),
                score=hand.score()
            ))
            break


def main(num_players, num_decks):
    """Main execution function"""

    # Initialize and shuffle the deck
    deck = Deck(num_decks).shuffle()

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
    print(u'Dealer showing: {}'.format(players[-1].hands()[0].peek(0)['face']))

    # Run player loop
    for player in players:
        for hand in player.hands():

            if player.name() is 'Dealer':
                dealer_play(player, hand, deck)
            else:
                play_hand(player, hand, deck)


    # Calculate and output results
    # results()


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
            print('ERROR: Number of players must be 1-5', file=sys.stderr)
            sys.exit(1)
    else:
        num_players = 1

    # Run main function
    main(num_players, num_decks)

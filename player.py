#!/usr/bin/env python
# -*- coding: utf-8 -*-

from hand import Hand

class Player:

    def __init__(self, name):

        self.name = str(name)

        self.hands = [
            Hand()
        ]


    def hit(self):
        """Player hit action"""

        print('Hit action')


    def double(self):
        """Player double action"""

        print('Double action')


    def split(self):
        """Player split action"""

        print('Spit action')

#!/usr/bin/env python3

import re

from collections import Counter
from enum import IntEnum
from itertools import combinations_with_replacement


class HandType(IntEnum):
    ''' Enum for the kinds of Hand we can have.
        In increasing order of value.'''
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7  # Multiple decks??


class Hand():
    ''' Hand class, parses and calculates the value of a particular hand'''
        
    def __init__(self, hand_str, bid_value, allow_jokers=False):
        # Store hand information
        self.original_hand_str = hand_str
        self.bid = bid_value
        self.hand = hand_str
        
        # Here we'll use _ to pad the string so that the positions
        # of a value remain the same.  That way we can compare the
        # value of the card just by comparing its index in the string.
        if not allow_jokers:
            card_order = '_23456789TJQKA'
        else:
            card_order = 'J23456789T_QKA'
        # Store the individual card values
        self.values = [card_order.index(x) for x in self.hand]

        # Work out the card distribution, eg 'KKK88' -> {'K': 3, '8': 2}
        self._distrib = Counter(self.hand)

        # Now work out our Hand type from the card distribution                        
        values = self._distrib.values()
        if 5 in values:
            self.kind = HandType.FIVE_OF_A_KIND
        elif 4 in values:
            self.kind = HandType.FOUR_OF_A_KIND
        elif 2 in values and 3 in values:
            self.kind = HandType.FULL_HOUSE
        elif 3 in values:
            self.kind = HandType.THREE_OF_A_KIND
        elif len([x for x in values if x == 2]) == 2:
            self.kind = HandType.TWO_PAIR
        elif 2 in values:
            self.kind = HandType.ONE_PAIR
        else:
            self.kind = HandType.HIGH_CARD
            
        if allow_jokers and 'J' in self.hand:
            # Need to work out what the best Joker combo is.
            # Do this by replacing the jokers with other cards,
            # creating a new Hand, and seeing if it's better
            # than this one.
            # Try all combinations of cards by using the itertools
            # cominations_with_replacement() function
            for alt in combinations_with_replacement(card_order, self.hand.count('J')):
                trial_hand_str = self.original_hand_str
                for swap in alt:
                    trial_hand_str = trial_hand_str.replace('J', swap, 1)
                new_hand = Hand(trial_hand_str, self.bid)
                if new_hand > self:
                    # We just created a better hand, copy it to ourself and carry on
                    self.hand = new_hand.hand
                    self.kind = new_hand.kind
            
    def __gt__(self, other):
        ''' Comparison operator so we can just use sort() to
            order a list of Hands in ascending order'''
        if self.kind > other.kind:
            # Our Hand kind is better than the other one
            is_greater = True
        elif self.kind == other.kind:
            # Our Hand kind is the same as the other one,
            # so check the individual card values
            is_greater = self.values > other.values
        else:
            # The other Hand is of a better kind than ours.
            is_greater = False
            
        return is_greater        
        
    def __repr__(self):
        ''' Pretty-print a Hand for debugging '''
        return f'"{self.hand}"={HandType(self.kind).name} was {self.original_hand_str}{"*" if "J" in self.original_hand_str else ""}'


def run(allow_jokers):
    ''' Read all the lines from the input, creating Hand instances
        as we go.  Can then simply sort the Hands and calculate the total.'''
    hands = []
    with open('input.txt', 'r') as f:
        for line in f:
            m = re.match(r'([\dATJQK]+) (\d+)', line)
            hand_str, bid_value  = m.group(1), int(m.group(2))
            hands.append(Hand(hand_str, bid_value, allow_jokers=allow_jokers))
        
    # Rank hands        
    hands.sort()
        
    total = 0
    for index, hand in enumerate(hands):
        total += (index + 1) * hand.bid
    print(f'Total = {total}')
    

# Part 1
run(False)

# Part 2
run(True)
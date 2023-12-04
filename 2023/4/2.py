import re

class Card():
    ''' An object representing a card.
    Contains a count of copies we have, and the number of winning number matches
    '''
    def __init__(self, info: str):
        m = re.match(r'Card +(\d+): ([\d ]+) \| ([\d ]+)', line)
        winning = [int(x) for x in m.group(2).split()]
        mine = [int(x) for x in m.group(3).split()]
        intersection = list(set(winning) & set(mine))
        self._matches = len(intersection)
        self._count = 1     # Initially we have one of this card

    @property
    def matches(self):
        ''' The number of winning matches for this card '''
        return self._matches

    @property
    def count(self):
        ''' The number of copies of this card '''
        return self._count
    
    def add(self):
        ''' Add another copy of this card to our hand '''
        self._count += 1
    

cards: list[Card] = []

# Read in and parse the initial set of cards.
# At this point we have one copy of each.
with open('input.txt', 'r') as f:
    for line in [x.strip() for x in f.readlines()]:
        cards.append(Card(line))
        
# Now iterate through the cards, adding duplicates
# as per the rules according the the number of matches
# found.  As all additional cards are added after the
# one we're processing, we'll automatically get to
# them in subsequent iterations.
for index, card in enumerate(cards):
    # Iterate through all copies of this card
    for count in range(1, card.count + 1):
        # Add cards as per the rules
        for additional in range(0, card.matches):
            cards[index + additional + 1].add()
            
# Now just total the card counts
total = sum([x.count for x in cards])
print(f'Total cards = {total}')

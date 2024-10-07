

def create_deck():
    ''' Program a simple function in the language of your choice to represent a deck of cards with operations to shuffle the deck and to deal one card.
'''
    suits = ['hearts', 'diamonds', 'clubs', 'spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append(f'{rank} of {suit}')
        return deck







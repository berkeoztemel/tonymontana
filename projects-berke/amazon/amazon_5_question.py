import random
class DealCard():

    def create_deck():
        ''' Program a simple function in the language of your choice to represent a deck of cards with operations to shuffle the deck and to deal one card.
    '''
        suits = ['hearts', 'diamonds', 'clubs', 'spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        deck = []
        for suit in suits:
            for rank in ranks:
                deck.append(f'{rank} of {suit}') #combine each rank and suit and add end of the list(deck)
        return deck

    def shuffle_deck(deck):
        ''' Shuffle the deck. '''
        random.shuffle(deck)

    def deal_card(deck):
        if len(deck) > 0:
            return deck.pop() #default value is -1 (last index of list). removing rest of list and printing only -1 index










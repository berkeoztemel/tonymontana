#Program in any language to arrange a deck of cards in below order.
# - Based on Color: Spade, Heart, Diamond, Club.
# - Based on number: Ace>King>Queen>Jack>Higher number >lower numbers.'''

def create_deck():
    ''' Program a simple function in the language of your choice to represent a deck of cards with operations to shuffle the deck and to deal one card.
'''
    suits = ['Spade', 'Club', 'Heart', 'Diamond']
    ranks = ['Ace', 'King', 'Queen', 'Jack', '10', '9', '8', '7', '6', '5', '4', '3', '2']
    deck = []

    for suit in suits:
        for rank in ranks:
            deck.append((rank, suit))
    return deck

def suit_value(suit):
    '''Function to manually determine the value of a suit based on its order'''
    if suit == "Spade":
        return 1
    elif suit == "Heart":
        return 2
    elif suit == "Diamond":
        return 3
    elif suit == "Club":
        return 4

def rank_value(rank):
    '''Function to manually determine the value of a rank based on its order'''
    if rank == "Ace":
        return 1
    elif rank == "King":
        return 2
    elif rank == "Queen":
        return 3
    elif rank == "Jack":
        return 4
    else:
        return 14 - int(rank)

def arrange_deck(deck):
    '''Function to arrange the deck by suit and rank without using library functions'''
    n = len(deck)

    for i in range(n):
        for j in range(0, n-i-1):
            #compare suit value first
            suit_value1 = suit_value(deck[j][1])
            suit_value2 = suit_value(deck[j+1][1])

            if suit_value1 > suit_value2:
                deck[j], deck[j+1] = deck[j+1], deck[j]

            elif suit_value1 == suit_value2:
                rank_value1 = rank_value(deck[j][0])
                rank_value2 = rank_value(deck[j+1][0])

                if rank_value1 > rank_value2:
                    deck[j], deck[j+1] = deck[j+1], deck[j]
    return deck

#call function
deck = create_deck()
sorted_deck = arrange_deck(deck)
for card in sorted_deck:
    print(f'{card[0]} of {card[1]}')






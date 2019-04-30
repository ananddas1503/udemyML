## welcome to blackjack game in python using OOP

'''
PSEUDO CODE 
To play a hand of Blackjack the following steps must be followed:
Create a deck of 52 cards
Shuffle the deck
Ask the Player for their bet
Make sure that the Player's bet does not exceed their available chips
Deal two cards to the Dealer and two cards to the Player
Show only one of the Dealer's cards, the other remains hidden
Show both of the Player's cards
Ask the Player if they wish to Hit, and take another card
If the Player's hand doesn't Bust (go over 21), ask if they'd like to Hit again.
If a Player Stands, play the Dealer's hand. The dealer will always Hit until the Dealer's value meets or exceeds 17
Determine the winner and adjust the Player's chips accordingly
Ask the Player if they'd like to play again
'''

# 1. DEFINE global variables 

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True


# 2. define card class

class Card:

	def __init__(self,suit,rank):
		self.suit = suit
		self.rank = rank

	def __str__(self):
		return self.rank + 'of' + self.suit




# 3. define deck class that consists of different Card objects 

class Deck:
	def __init__(self):
		self.deck = []
		for suit in suits:
			for rank in ranks:
				self.deck.append(Card(suit,rank)) # build card objects and add them to the list seld.deck


	def __str__(self):
		deck_str=''
		for x in self.deck:
            deck_str += '\n '+x.__str__() # add each Card object's print string
        return 'The deck has:' + deck_str


    def shuffle(self):
    	random.shuffle(self.deck)

    def deal(self):
    	single_card = self.deck.pop()
    	return single_card



# 4. Create a Hand Class. In addition to holding Card objects dealt from the Deck, \n 
#the Hand class may be used to calculate the value of those cards using the values dictionary defined above. 
# It may also need to adjust for the value of Aces when appropriate. 



	
class Hand:
    
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1  # add to self.aces
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1 
		











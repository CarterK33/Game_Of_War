#card class
#deck class
#player class
#game logic
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 
'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}


class Card():
	def __init__(self,suit,rank):
		self.suit = suit
		self.rank = rank
		self.value = values[rank]
 
	def __str__(self): 
		return self.rank + " of " + self.suit 



class Deck(): 
	def __init__(self):
		self.all_cards = []

		for suit in suits: 
			for rank in ranks: 
				created_card = Card(suit, rank)
				self.all_cards.append(created_card)

	def shuffle(self): 
		random.shuffle(self.all_cards)

	def deal_one(self):
		return self.all_cards.pop()

class Player(): 
	def __init__(self, name):
		self.name = name
		self.all_cards = []

	def remove_one(self):
		return self.all_cards.pop(0)

	def add_cards(self, new_cards): 
		if type(new_cards) == type([]):
			self.all_cards.extend(new_cards)
		else:
			self.all_cards.append(new_cards)

	def __str__(self):
		return f"Player {self.name} has {len(self.all_cards)} cards" 




#game set_up
player_1 = Player("P1")
player_2 = Player("P2")

new_deck = Deck()
new_deck.shuffle()

for x in range(26):
	player_1.add_cards(new_deck.deal_one())
	player_2.add_cards(new_deck.deal_one())

game_on = True
round_num = 0

while game_on:
	round_num += 1
	print(f"Round {round_num}")

	if len(player_1.all_cards) == 0: 
		print('Player One, out of cards! Player Two Wins!')
		game_on = False
		break 

	if len(player_2.all_cards) == 0:
		print('Player One, out of cards! Player One Wins!')
		game_on = False
		break

	player_1_cards = []
	player_1_cards.append(player_1.remove_one())


	player_2_cards = []
	player_2_cards.append(player_2.remove_one())

	at_war = True

	while at_war: 
		if player_1_cards[-1].value > player_2_cards[-1].value: 
			player_1.add_cards(player_1_cards)
			player_1.add_cards(player_2_cards)

			at_war = False 

		elif player_2_cards[-1].value > player_1_cards[-1].value: 
			player_2.add_cards(player_1_cards)
			player_2.add_cards(player_2_cards)

			at_war = False

		else: 
			print("War!!!")

			if len(player_1.all_cards) < 3: 
				print("Player One unable to declare war")
				print("Player Two Wins!")
				game_on = False  
				break

			elif len(player_2.all_cards) > 3: 
				print("Player Two unable to declare war")
				print("Player One wins")
				game_on = False 
				break 

			else: 
				for num in range(3):
					player_1_cards.append(player_1.remove_one())
					player_2_cards.append(player_2.remove_one())


















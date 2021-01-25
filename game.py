'''
Game main file
'''

from deck import Deck
from player import Player


# GAME SETUP
player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle_deck()

for x in range(26):
	player_one.add_cards(new_deck.deal_one())
	player_two.add_cards(new_deck.deal_one())

game_on = True
round_num = 0

# while game_on
while game_on:
	round_num += 1
	print(f'Round {round_num}')

	if len(player_one.all_cards) == 0:
		print('Player One, out of cards! Player Two Wins!')
		game_on = False
		break
	if len(player_two.all_cards) == 0:
		print('Player Two, out of cards! Player One Wins!')
		game_on = False
		break

	# START A NEW ROUND
	player_one_cards = []
	player_one.shuffle_cards()
	player_one_cards.append(player_one.remove_one())

	player_two_cards = []
	player_two.shuffle_cards()
	player_two_cards.append(player_two.remove_one())

	# while at_war
	at_war = True
	while at_war:
		if player_one_cards[-1].value > player_two_cards[-1].value:
			player_one.add_cards(player_one_cards)
			player_one.add_cards(player_two_cards)
			at_war = False
		elif player_one_cards[-1].value < player_two_cards[-1].value:
			player_two.add_cards(player_one_cards)
			player_two.add_cards(player_two_cards)
			at_war = False
		else:
			print('WAR!')

			if len(player_one.all_cards) < 10:
				print("Player One unable to declare war")
				print("PLAYER TWO WINS!")
				game_on = False
				break
			elif len(player_two.all_cards) < 10:
				print("Player Two unable to declare war")
				print("PLAYER ONE WINS!")
				game_on = False
				break
			else:
				for x in range(10):
					player_one_cards.append(player_one.remove_one())
					player_two_cards.append(player_two.remove_one())

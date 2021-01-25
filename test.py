from card import Card
from deck import Deck
from player import Player

two_hearts = Card("Hearts","Two")
three_of_clubs = Card("Clubs","Three")

new_deck = Deck()

# for card_object in new_deck.all_cards:
# 	print(card_object)

new_deck.shuffle()

# for card_object in new_deck.all_cards:
# 	print(card_object)

# print(len(new_deck.all_cards))
# bot_card = new_deck.deal_one()
# print(bot_card)
# print(len(new_deck.all_cards))

new_player = Player("Jose")
print(new_player)

new_player.add_cards(new_deck.deal_one())
print(new_player)
for card_object in new_player.all_cards:
	print(card_object)

new_player.add_cards([two_hearts,two_hearts,two_hearts])
print(new_player)
for card_object in new_player.all_cards:
	print(card_object)

new_player.remove_one()
print(new_player)
for card_object in new_player.all_cards:
	print(card_object)
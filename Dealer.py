from Player import Player
from random import randrange


class Dealer(Player):
	def __init__(self, name, deck, bet=None):
		super().__init__(name, bet)

		self.deck = deck

		self.cards = []
		self.has_standed = False

	def HitOrStand(self):
		if self.has_standed:
			return

		value = self.CardsValue()
		if value <= randrange(14, 18):
			#hitting
			print(f"{self.name} hit another card!")
			self.cards.append(self.deck.NewCard())
		else:
			#standing
			self.Stand()
			return


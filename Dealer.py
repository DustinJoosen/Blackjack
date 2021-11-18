from Player import Player
from random import randrange


class Dealer(Player):
	def __init__(self, name, deck):
		super().__init__(name)
		self.__deck = deck

	def HitOrStand(self):
		if self.has_standed:
			return

		value = self.CardsValue()
		if value <= randrange(14, 18):
			#hitting
			print(f"{self.name} hit another card!")
			self.cards.append(self.__deck.NewCard())
		else:
			#standing
			self.Stand()
			return


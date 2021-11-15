from Player import Player


class Dealer(Player):
	def __init__(self, name, deck, bet=None):
		super().__init__(name, bet)

		self.deck = deck

		self.cards = []
		self.has_standed = False

	def HitOrStand(self):
		value = self.CardsValue()
		if value <= 15:
			#hitting
			print(f"{self.name} hit another card!")
			self.cards.append(self.deck.NewCard())
		else:
			#standing
			print(f"{self.name} stands down!")
			self.has_standed = True
			return


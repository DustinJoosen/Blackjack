from Deck import values


class Player:
	def __init__(self, name, bet=None):
		self.name = name
		self.bet = bet

		self.has_standed = False
		self.cards = []

	def ShowOpenCards(self):
		print(f"Open cards of {self.name}:")
		for card in self.cards:
			print(f"\t-{card}")

	def CardsValue(self):
		value = 0

		for card in self.cards:
			value += int(values[card.value])

		return value

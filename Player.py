from Deck import values as card_values


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
			value += int(card_values[card.value])

		return value

	def Stand(self):
		print(f"{self.name} stands down!\n")
		self.has_standed = True

	def CheckValue(self):
		total_val = self.CardsValue()

		if total_val == 21:
			self.has_standed = True
			print(f"{self.name} has Blackjack!\n")
		elif total_val > 21:
			self.has_standed = True
			print(f"{self.name} is Bust!\n")

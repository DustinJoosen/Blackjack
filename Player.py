from Deck import values as card_values


class Player:
	def __init__(self, name):
		self.name = name

		self.has_standed = False
		self.cards = []

		self.total_credits = 100

		self.ace_used = False

	def PrepForNewRound(self):
		self.has_standed = False
		self.ace_used = False

		self.cards = []

	def ShowOpenCards(self):
		print(f"Open cards of {self.name}:")
		for card in self.cards:
			print(f"\t-{card}")

	def CardsValue(self):
		value = 0

		for card in self.cards:
			value += int(card_values[card.value])

			if card.value == 'Ace' and not self.ace_used:
				value += 10

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

			#first check if there actually is an ace in the cards
			has_ace = False
			for card in self.cards:
				if card.value == 'Ace':
					has_ace = True

			if has_ace and not self.ace_used:
				self.ace_used = True
			else:
				self.has_standed = True
				print(f"{self.name} is Bust!\n")

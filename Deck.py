from random import shuffle

values = {
	"Ace": 1,
	"2": 2,
	"3": 3,
	"4": 4,
	"5": 5,
	"6": 6,
	"7": 7,
	"8": 8,
	"9": 9,
	"10": 10,
	"Jack": 10,
	"Queen": 10,
	"King": 10,
}

variants = [
	"Hearths",
	"Clubs",
	"Diamonds",
	"Spades"
]


class Card:
	def __init__(self, value, variant):
		self.value = value
		self.variant = variant

		self.is_open = False

	def __str__(self):
		if not self.value == 'Ace':
			return f"{self.variant} {self.value} ({values[self.value]})"
		else:	
			return f"{self.variant} {self.value} (1/11)"


#the cards that come out of the box, shuffled by the dealer
class Deck:

	def __init__(self):
		self._deck = []

		for variant in variants:
			for value in values:
				self._deck.append(Card(value=value, variant=variant))

		shuffle(self._deck)

	def NewCard(self):
		return self._deck.pop()

	def DeckCount(self):
		return len(self._deck)

	def PrintDeck(self):
		for card in self._deck:
			print(card)

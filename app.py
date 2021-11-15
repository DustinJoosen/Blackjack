from Deck import Deck
from Player import Player
from Dealer import Dealer


def game():
	bet = input("How much are you going to bet this round?\n>>>")
	deck = Deck()

	dealer = Dealer("Dealer", deck)
	player = Player("Dustin", bet)

	print("\nDealer dealt two cards to player:")
	player.cards.append(deck.NewCard())
	player.cards.append(deck.NewCard())
	player.ShowOpenCards()

	print("\nDealer dealt two cards to themself:")
	dealer.cards.append(deck.NewCard())
	dealer.cards.append(deck.NewCard())
	dealer.ShowOpenCards()

	going = True
	while going:
		if not player.has_standed:

			total_val = player.CardsValue()
			print(f"\nYour cards currently have a value of {total_val}")

			choice = input("Do you want to hit or stand? (H/S)\n>>>")
			if choice == "H":
				print("Dealer dealt new card.")
				new_card = deck.NewCard()
				player.cards.append(new_card)
				print(str(new_card) + "\n")
			elif choice == "S":
				print(f"{player.name} stands down!\n")
				player.has_standed = True

		dealer.HitOrStand()

		if player.has_standed and dealer.has_standed:
			going = False

	print("\nBoth teams are done!")
	print(f"player points:{player.CardsValue()}\ndealer points:{dealer.CardsValue()}")


if __name__ == "__main__":
	# game()
	deck = Deck()
	deck.PrintDeck()

from Deck import Deck
from Player import Player
from Dealer import Dealer
import time


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

	playing = True
	while playing:
		if not player.has_standed:

			total_val = player.CardsValue()
			print(f"\nYour cards currently have a value of {total_val}")

			choice = input("Do you want to hit or stand? (H/S)\n>>>")
			if choice == "H":
				print("Dealer dealt new card.")
				new_card = deck.NewCard()
				player.cards.append(new_card)
				print(str(new_card) + "\n")

				player.CheckValue()

			elif choice == "S":
				player.Stand()

		if not dealer.has_standed:
			dealer.HitOrStand()
			dealer.CheckValue()

		if player.has_standed and dealer.has_standed:
			playing = False

	print("\nBoth teams are done!")

	#check who won
	player_val = player.CardsValue()
	dealer_val = dealer.CardsValue()

	winner = None
	#if either had busted
	if dealer_val > 21 or player_val > 21:
		if dealer_val > 21:
			winner = player
		if player_val > 21:
			winner = dealer
	else:
		if dealer_val > player_val:
			winner = dealer

	#let the user know who won
	time.sleep(2)
	print("And the winner is....")
	time.sleep(2)
	print(f"{winner}!")

	print(f"Player cards value:\t{player_val}")
	print(f"Dealer cards value:\t{dealer_val}")


if __name__ == "__main__":
	game()

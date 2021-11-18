from Deck import Deck
from Player import Player
from Dealer import Dealer
import time


def get_bet():
	try:
		bet = int(input("How much are you going to bet this round?\n>>>"))
		return bet
	except ValueError:
		print("Only numeric values are allowed")
		return get_bet()


def play_round(player, dealer, deck):
	bet = get_bet()
	player.total_credits -= bet

	print("\nDealer dealt two cards to player:")
	player.cards.append(deck.NewCard())
	player.cards.append(deck.NewCard())
	player.ShowOpenCards()
	player.CheckValue()

	print("\nDealer dealt two cards to themself:")
	dealer.cards.append(deck.NewCard())
	dealer.cards.append(deck.NewCard())
	dealer.ShowOpenCards()
	dealer.CheckValue()

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
		if dealer_val < player_val:
			winner = player
		else:
			winner = dealer

	#let the user know who won
	time.sleep(2)
	print("And the winner is....")
	time.sleep(2)
	print(f"{winner.name}!")

	print(f"{player.name} cards value:\t{player_val}")
	print(f"{dealer.name} cards value:\t{dealer_val}\n")

	#handle the bet
	if winner == player:
		if player_val == 21:
			player.total_credits += bet * 3
			print(f"You got {bet * 3} credits. Your total is now {player.total_credits}")
		else:
			player.total_credits += bet * 2
			print(f"You got {bet * 2} credits. Your total is now {player.total_credits}")
	else:
		if player_val < 21:
			player.total_credits += int(bet / 2)
			print(f"You lost {int(bet / 2)} credits. Your total is now {player.total_credits}")
		else:
			print(f"You lost your bet, {bet} credits. Your total is now {player.total_credits}")


if __name__ == "__main__":
	print("Welcome to Blackjack!")
	name = input("What do you wish to be called this session?\n>>>")
	print(f"\nWelcome {name}. You will start out the session with 100 credits")

	deck = Deck()

	dealer = Dealer("Dealer", deck)
	player = Player(name)

	round_num = 0
	playing = True
	while playing:
		round_num += 1

		player.PrepForNewRound()
		dealer.PrepForNewRound()

		print(f"\nRound {round_num}")

		play_round(player, dealer, deck)
		print("___________________________")

		#handling stopping the game
		continue_playing = input("Do you want to play another round? (Y/N)\n>>>")
		if continue_playing != "Y":
			playing = False

	print("\nThanks for playing blackjack!")
	#print the results of the session here, like a table of your results

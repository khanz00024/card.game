import random
import time

# Define the ranks and suits
ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
suits = ("hearts", "diamonds", "clubs", "spades")

# Create and shuffle the deck
deck = [(rank, suit) for rank in ranks for suit in suits]
random.shuffle(deck)

# Split the deck into two hands
mid = len(deck) // 2
player1_hand = deck[:mid]
player2_hand = deck[mid:]


def card_comparison(p1_card, p2_card):
    if ranks.index(p1_card[0]) > ranks.index(p2_card[0]):
        return 1
    elif ranks.index(p1_card[0]) < ranks.index(p2_card[0]):
        return 2
    else:
        return 0


def play_round(player1_hand, player2_hand):
    if player1_hand and player2_hand:
        p1_card = player1_hand.pop(0)
        p2_card = player2_hand.pop(0)
        print(f"Player 1 plays {p1_card}, Player 2 plays {p2_card}")

        time.sleep(0.01)

        result = card_comparison(p1_card, p2_card)
        if result == 1:
            print("Player 1 wins the round!")
            player1_hand.extend([p1_card, p2_card])
        elif result == 2:
            print("Player 2 wins the round!")
            player2_hand.extend([p1_card, p2_card])
        else:
            print("It's a tie! War starts!")
            time.sleep(0.01)
            war(player1_hand, player2_hand)


def war(player1_hand, player2_hand):
    # Check if either player can't continue with war
    if len(player1_hand) < 4:
        print("Player 1 doesn't have enough cards for war! Player 2 wins!")
        player2_hand.extend(player1_hand)
        player1_hand.clear()
        return
    if len(player2_hand) < 4:
        print("Player 2 doesn't have enough cards for war! Player 1 wins!")
        player1_hand.extend(player2_hand)
        player2_hand.clear()
        return

    # War: each player puts down 3 cards and reveals the fourth
    p1_war_cards = [player1_hand.pop(0) for _ in range(3)]
    p2_war_cards = [player2_hand.pop(0) for _ in range(3)]
    p1_war_card = player1_hand.pop(0)
    p2_war_card = player2_hand.pop(0)
    print(f"War! Player 1's card: {p1_war_card}, Player 2's card: {p2_war_card}")

    time.sleep(0.01)

    result = card_comparison(p1_war_card, p2_war_card)
    if result == 1:
        print("Player 1 wins the war!")
        player1_hand.extend([*p1_war_cards, p1_war_card, *p2_war_cards, p2_war_card])
    elif result == 2:
        print("Player 2 wins the war!")
        player2_hand.extend([*p1_war_cards, p1_war_card, *p2_war_cards, p2_war_card])
    else:
        print("It's another tie! War continues!")
        time.sleep(0.01)
        war(player1_hand, player2_hand)


def play_game():
    round_count = 1
    while player1_hand and player2_hand:
        print(f"Round {round_count}:")
        play_round(player1_hand, player2_hand)
        print(f"Player 1 has {len(player1_hand)} cards, Player 2 has {len(player2_hand)} cards\n")
        time.sleep(0.01)
        round_count += 1

    if player1_hand:
        print("Player 1 wins the game!")
    else:
        print("Player 2 wins the game!")

    # Display final card counts
    print(f"Final card count - Player 1: {len(player1_hand)}, Player 2: {len(player2_hand)}")


# Start the game
play_game()

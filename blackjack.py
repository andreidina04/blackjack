import random

# Function to deal a random card
def deal_card():
    cards = [2,3,4,5,6,7,8,9,10,10,10,10,11]  # 11 represents Ace
    card = random.choice(cards)
    return card

# Function to calculate the score of a hand
def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    # Check for a Blackjack (a hand with only 2 cards: Ace + 10)
    if 11 in cards and 10 in cards and len(cards) == 2:
        return 0
    # Replace Ace (11) with 1 if total score exceeds 21
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

# Function to compare user score with computer score
def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw!"
    elif c_score == 0:
        return "Lose, opponent has Blackjack."
    elif u_score == 0:
        return "Win with a Blackjack"
    elif u_score > 21:
        return "You went over. You lose."
    elif c_score > 21:
        return "Computer went over. You win."
    elif u_score > c_score:
        return "You win."
    else:
        return "You lose."

def main():
    # Initialize persistent score counters
    user_wins = 0
    computer_wins = 0
    draw = 0

    while True:
        # Start a new round
        user_cards = []
        computer_cards = []
        computer_score = -1
        user_score = -1
        is_game_over = False

        # Deal two initial cards to user and computer
        for _ in range(2):
            computer_cards.append(deal_card())
            user_cards.append(deal_card())

        # User's turn
        while not is_game_over:
            user_score = calculate_score(user_cards)
            computer_score = calculate_score(computer_cards)
            print(f"Your cards: {user_cards}, current score: {user_score}")
            print(f"Computer's first card: {computer_cards[0]}")

            # Check if game should end
            if user_score == 0 or computer_score == 0 or user_score > 21:
                is_game_over = True
            else:
                user_deal = input("Type 'y' to get another card, type 'n' to pass: ")
                if user_deal.lower() == "y":
                    user_cards.append(deal_card())
                else:
                    is_game_over = True

        # Computer's turn, must draw until score >= 17
        while computer_score != 0 and computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)

        # Show final hands and round result
        print(f"Your final hand: {user_cards}, final score: {user_score}")
        print(f"Computer final hand: {computer_cards}, final score: {computer_score}")
        result = compare(user_score, computer_score)
        print(result)

        # Update general score counters
        if result in (
            "You win.",
            "Win with a Blackjack",
            "Computer went over. You win."
        ):
            user_wins += 1
        elif result in (
            "You lose.",
            "You went over. You lose.",
            "Lose, opponent has Blackjack."
        ):
            computer_wins += 1
        else:
            draw += 1

        print("------General Score------")
        print(f"Computer Wins - {computer_wins}")
        print(f"Player Wins - {user_wins}")
        print(f"Draws - {draw}")

        # Ask user if they want to play again
        user_play = input("Wanna play again? 'y' for yes, 'n' for closing ")
        if user_play.lower() != "y":
            print("Closing the program...")
            print("Bye...")
            break

if __name__ == "__main__":
    main()

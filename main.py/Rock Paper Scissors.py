import random

choices = ["rock", "paper", "scissors"]

# Fixed computer choices for testing
test_choices = ["scissors", "rock", "paper"]

# True = Test mode, False = Random mode
TEST_MODE = True


def find_winner(player, computer):

    if player == computer:
        return "draw"

    elif player == "rock" and computer == "scissors":
        return "player"

    elif player == "paper" and computer == "rock":
        return "player"

    elif player == "scissors" and computer == "paper":
        return "player"

    else:
        return "computer"


def play_game():

    player_score = 0
    computer_score = 0
    draws = 0

    print("\n===== ROCK PAPER SCISSORS =====")
    print("Best of 3 Rounds!")
    
    for round_num in range(3):

        while True:
            player = input(
                f"\nRound {round_num + 1} - Enter rock, paper or scissors: "
            ).lower().strip()

            if player in choices:
                break

            print("Invalid choice. Enter rock, paper or scissors.")

        # Computer choice
        if TEST_MODE:
            computer = test_choices[round_num]
        else:
            computer = random.choice(choices)

        print("Computer chose:", computer)

        # Find round winner
        winner = find_winner(player, computer)

        if winner == "player":
            print(f"Round {round_num + 1}: You win")
            player_score += 1

        elif winner == "computer":
            print(f"Round {round_num + 1}: Computer wins")
            computer_score += 1

        else:
            print(f"Round {round_num + 1}: Draw")
            draws += 1

    # Final score
    print("\n===== FINAL SCORE =====")
    print("You:", player_score)
    print("Computer:", computer_score)
    print("Draws:", draws)

    # Final result
    if player_score > computer_score:
        print("Result: You win the match!")

    elif computer_score > player_score:
        print("Result: Computer wins the match.")

    else:
        print("Result: Match draw.")

    # Play again
    while True:
        again = input("\nPlay again? (y/n): ").lower().strip()

        if again == "y":
            play_game()
            return

        elif again == "n":
            print("Thanks for playing!")
            return

        else:
            print("Please enter y or n.")


play_game()

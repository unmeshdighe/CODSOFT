import random

def get_user_choice():
    while True:
        user_input = input("Choose rock, paper, or scissors: ").strip().lower()
        if user_input in ["rock", "paper", "scissors"]:
            return user_input
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def display_result(user_choice, computer_choice, result):
    print(f"\nYour choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")
    if result == "tie":
        print("It's a tie!")
    elif result == "user":
        print("You win!")
    else:
        print("You lose!")

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        print("\n--- Rock-Paper-Scissors Game ---")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)

        display_result(user_choice, computer_choice, result)

        # Update scores
        if result == "user":
            user_score += 1
        elif result == "computer":
            computer_score += 1

        print(f"\nScore: You {user_score} - {computer_score} Computer")

        # Ask if the user wants to play again
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("\nThanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    play_game()
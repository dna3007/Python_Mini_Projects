import random

def play_rock_paper_scissors():
    print("Welcome to Rock-Paper-Scissors!")
    print("Let's play!")

    choices = ["rock", "paper", "scissors"]

    while True:
        # Prompt the user for their choice
        user_choice = input("Choose your move (rock, paper, or scissors): ").lower()

        # Validate the user's input
        if user_choice not in choices:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
            continue

        # Generate a random choice for the computer
        computer_choice = random.choice(choices)

        # Display the computer's choice
        print("The computer chose:", computer_choice)

        # Determine the winner
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (
            (user_choice == "rock" and computer_choice == "scissors")
            or (user_choice == "paper" and computer_choice == "rock")
            or (user_choice == "scissors" and computer_choice == "paper")
        ):
            print("Congratulations! You win!")
        else:
            print("Sorry, you lose!")

        # Ask the user if they want to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

    print("Thank you for playing Rock-Paper-Scissors!")

# Start the game
play_rock_paper_scissors()

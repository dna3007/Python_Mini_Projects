import random


def number_guesser():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guesser Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        # Prompt the user to guess the number
        guess = input("Take a guess: ")

        # Check if the user wants to quit
        if guess.lower() == "quit":
            print("Game over. The number was", secret_number)
            break

        # Validate the user's input
        try:
            guess = int(guess)
        except ValueError:
            print("Invalid input. Please enter a valid number or type 'quit' to exit.")
            continue

        # Increase the number of attempts
        attempts += 1

        # Compare the user's guess with the secret number
        if guess < secret_number:
            print("Too low! Try guessing higher.")
        elif guess > secret_number:
            print("Too high! Try guessing lower.")
        else:
            print("Congratulations! You guessed the number", secret_number, "in", attempts, "attempts.")
            break


# Start the game
number_guesser()

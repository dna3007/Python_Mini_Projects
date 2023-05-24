def play_adventure_game():
    print("Welcome to the Choose Your Own Adventure game!")
    print("You find yourself standing in front of two doors.")
    print("Which door do you choose? (1 or 2)")

    choice = input("> ")

    if choice == "1":
        print("You enter through door 1 and find yourself in a dark room.")
        print("In the corner of the room, you see a small key.")
        print("What do you do?")
        print("1. Take the key.")
        print("2. Ignore the key and search for another way out.")

        choice = input("> ")

        if choice == "1":
            print("You take the key and carefully continue exploring the room.")
            print("After some time, you find a hidden door.")
            print("Using the key, you unlock the door and escape to safety.")
            print("Congratulations! You have successfully completed the adventure!")
        elif choice == "2":
            print("You decide to search for another way out without taking the key.")
            print("Unfortunately, you are unable to find any other exit.")
            print("You are trapped in the dark room forever. Game over!")
        else:
            print("Invalid choice. Game over!")

    elif choice == "2":
        print("You open door 2 and step into a vast garden filled with beautiful flowers.")
        print("At the center of the garden, you see a treasure chest.")
        print("What do you do?")
        print("1. Open the treasure chest.")
        print("2. Explore the garden some more before opening the chest.")

        choice = input("> ")

        if choice == "1":
            print("You cautiously open the treasure chest.")
            print("Inside, you find a pile of gold coins and precious gems.")
            print("Congratulations! You are now rich and have successfully completed the adventure!")
        elif choice == "2":
            print("You spend more time exploring the garden, enjoying the beauty around you.")
            print("However, as you delay, the garden magically disappears.")
            print("You are left standing in an empty void. Game over!")
        else:
            print("Invalid choice. Game over!")

    else:
        print("Invalid choice. Game over!")


# Start the game
play_again = "yes"
while play_again.lower() == "yes":
    play_adventure_game()
    play_again = input("Do you want to play again? (yes/no) ")
play_adventure_game()

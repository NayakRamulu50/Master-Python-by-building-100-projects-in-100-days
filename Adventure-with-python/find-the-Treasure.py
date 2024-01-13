import time

def introduction():
    print("Welcome to the Treasure Island Adventure Game!")
    print("You find yourself on an island in search of hidden treasure.")
    print("Your choices will determine your fate. Choose wisely!\n")

def make_choice(question, option1, option2):
    print(question)
    print("1. " + option1)
    print("2. " + option2)
    return input("Enter your choice (1 or 2): ")

def game_over(reason):
    print("\n" + reason)
    print("Game Over. Better luck next time!")

def find_treasure():
    print("\nCongratulations! You found the hidden treasure!")
    print("You are now rich beyond your wildest dreams. Well done!")

def treasure_island_game():
    introduction()

    # Stage 1
    choice1 = make_choice("You come across a fork in the path. Which way do you go?",
                          "Left", "Right")

    if choice1 == "1":
        # Stage 2a
        choice2a = make_choice("You reach a river. Do you swim across or search for a bridge?",
                               "Swim across", "Search for a bridge")

        if choice2a == "1":
            # Stage 3a
            choice3a = make_choice("As you swim across, you encounter a group of hungry sharks. What do you do?",
                                   "Try to outswim them", "Punch a shark in the nose")

            if choice3a == "1":
                game_over("The sharks are faster than you. They catch up and it's game over.")
            elif choice3a == "2":
                find_treasure()
            else:
                game_over("Invalid choice. Game over.")

        elif choice2a == "2":
            # Stage 3b
            choice3b = make_choice("You find a sturdy bridge. As you cross it, you notice a troll demanding a toll. What do you do?",
                                   "Pay the toll", "Ignore the troll and keep walking")

            if choice3b == "1":
                find_treasure()
            elif choice3b == "2":
                game_over("The troll gets angry and attacks you. Game over.")
            else:
                game_over("Invalid choice. Game over.")

        else:
            game_over("Invalid choice. Game over.")

    elif choice1 == "2":
        # Stage 2b
        choice2b = make_choice("You come across a dark cave. Do you enter the cave or continue along the path?",
                               "Enter the cave", "Continue along the path")

        if choice2b == "1":
            # Stage 3c
            choice3c = make_choice("Inside the cave, you find a treasure chest. What do you do?",
                                   "Open the chest", "Leave the cave")

            if choice3c == "1":
                find_treasure()
            elif choice3c == "2":
                game_over("You leave the cave empty-handed. Game over.")
            else:
                game_over("Invalid choice. Game over.")

        elif choice2b == "2":
            game_over("You continue along the path but get lost in the dense jungle. Game over.")
        else:
            game_over("Invalid choice. Game over.")

    else:
        game_over("Invalid choice. Game over.")


treasure_island_game()

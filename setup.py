from config import *


# Ask user to choose a resolution
# Return a tuple (width, height)
def select_resolution():
    while True:
        try:
            print("Select a resolution:")
            for i, res in enumerate(RESOLUTIONS):
                print(f"{i + 1}: {res[0]}x{res[1]}")
            choice = int(input("Enter resolution's number: ")) - 1

            return RESOLUTIONS[choice]
        except (ValueError, IndexError) as e:
            print("Please enter a valid input")


# Ask user to choose between single player and multiplayer mode
# Return true if multiplayer is chosen
def is_multiplayer():
    while True:
        print("Select between single player mode (S) or multiplayer mode (M)")
        choice = input("Enter your choice: ")

        if choice.casefold() == "s":
            return False
        elif choice.casefold() == "m":
            return True
        else:
            print("Please enter a valid input")

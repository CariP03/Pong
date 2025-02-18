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

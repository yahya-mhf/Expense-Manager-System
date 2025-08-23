from enum import Enum

class Menu(Enum):
    START = 1
    SETTINGS = 2
    EXIT = 3

def main():
    print("Choose an option:")
    print("1. Start Game")
    print("2. Settings")
    print("3. Exit")

    try:
        choice = int(input("Enter your choice: "))
        match Menu(choice):
            case Menu.START:
                print("Starting the game...")
            case Menu.SETTINGS:
                print("Opening settings...")
            case Menu.EXIT:
                print("Exiting program...")
            case _:
                print("Invalid choice!")
    except ValueError:
        print("Please enter a number.")
    except Exception:
        print("Invalid choice (not in menu).")

if __name__ == "__main__":
    main()

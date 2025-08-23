import os
import string
import random
import time
from datetime import datetime
from tabulate import tabulate
import csv

FILE_NAME = "data.csv"

def generate_id():
    # take current time in seconds (last 5 digits to keep it short)
    timestamp = str(int(time.time()))[-5:]
    # random 3 uppercase letters/digits
    rand_part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=3))
    return timestamp + rand_part

def screen():
    return f"""
    +-----------------+
    | Expense Tracker |
    +-----------------+
    (0) Exit.
    (1) Create Expense.
    (2) Read Expense.
    (3) Update Expense.
    (4) Delete Expense
    """

def screen_create_expense(table):
    return f"""
    +-----------------+
    | Expense Tracker |     << Create Expense >>
    +-----------------+

{table}
    """

def screen_read_expense(table):
    return f"""
    +-----------------+
    | Expense Tracker |     << Read Expense >>
    +-----------------+
    
{table}
    """

def screen_update_expense():
    return """
    +-----------------+
    | Expense Tracker |     << Update Expense >>
    +-----------------+
    
    """

def screen_delete_expense():
    return """
    +-----------------+
    | Expense Tracker |     << Delete Expense >>
    +-----------------+
    
    """

# to FCT : int get_choice () 
def get_int_choice(message, error_message = "please enter a valid integer [choice]", valid_numbers = None):
    try:
        choice = int(input(message))
        if valid_numbers and choice not in valid_numbers: # Handle choice input
            raise ValueError
    except ValueError:
        print(error_message)
        return
    else: # break if the choice is valid
        return choice

def get_float(message, error_message = "please enter a float!"):
    try:
        value = float(input(message))
    except:
        print(error_message)
        return
    else:
        return value
    

def view_all_expenses (data):
    return tabulate([[i] + row[:] for i, row in enumerate(data[1:])],["index"] + data[0], tablefmt="grid")

def main():
    while True: # App Loop
        os.system('cls' if os.name == "nt" else 'clear')

        # default data
        data = [
            ['ID', 'Categorie', 'Date', 'Amount', 'Description'],
            ['000-000', 'food', '8-22-2025 12:26', 100, 'this is a description']
        ]

        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, 'r') as file:
                content = csv.reader(file)
                data = list(content)

        # view screen
        print(screen())

        # get choice
        choice = None
        while choice is None:
            choice = get_int_choice("Choice : ", "please enter a valid choice!", {0, 1, 2, 3, 4})

        # redirect to choice
        if choice == 0: # exit
            os.system('cls' if os.name == "nt" else 'clear')
            break

        elif choice == 1: # Create Expense.
            # table cretion
            os.system('cls' if os.name == "nt" else 'clear') ###
            headers = ['ID', 'Categorie', 'Date', 'Amount', 'Description']
            line = [[generate_id(), '...', 'when you done creating', 0.0, '...']]
            table = tabulate(line, headers, tablefmt="grid")
            print(screen_create_expense(table))

            # Get Categorie
            line[0][1] = input("Expense Categorie : ").lower()
            os.system('cls' if os.name == "nt" else 'clear') ###
            table = tabulate(line, headers, tablefmt="grid")
            print(screen_create_expense(table))

            # Get Amount 
            amount = None
            while amount is None:
                amount = get_float("Expense Amount : ", "float expected")

            line[0][3] = amount

            os.system('cls' if os.name == "nt" else 'clear') ###
            table = tabulate(line, headers, tablefmt="grid")
            print(screen_create_expense(table))

            # Get Description
            line[0][4] = input("Expense Description : ")
            os.system('cls' if os.name == "nt" else 'clear') ###
            table = tabulate(line, headers, tablefmt="grid")
            print(screen_create_expense(table))

            # Get Date
            line[0][2] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            os.system('cls' if os.name == "nt" else 'clear') ###
            table = tabulate(line, headers, tablefmt="grid")
            print(screen_create_expense(table))

            # Save or Cancel
            print("To save press enter (or any key other than the cancel words)")
            save = input("To Cancel type 'cancel' or 'cl' : ")
            if save.lower() in {'cancel', 'cl'}:
                continue

            # TODO save 
            data.append(line[0])

            input("type anything to save and go back")

        elif choice == 2: # Read Expense.
            # TODO add an index to reading for make it easy to delete or update #DONE
            table = view_all_expenses (data)
            print(screen_read_expense(table))
            input("type anything to save and go back")

        elif choice == 3: # Update Expense.
            print(screen_update_expense())
           
            index_of_row = None
            valid_indexes = set(range(len(data) - 1))

            while index_of_row is None:
                index_of_row = get_int_choice(
                    "Select expense by index (indexes start with 0): ",
                    "Expense not found (Index out of range)",
                    valid_indexes
                )

            table = tabulate([data[index_of_row + 1]], data[0], tablefmt="grid")
            print(table)
            sure = input("Are you sure of Updating this expense (yes, no): ")
            if sure.lower() in ('y', 'yes'):
                # default value of table
                ID = data[index_of_row + 1][0]
                categorie = data[index_of_row + 1][1]
                date = data[index_of_row + 1][2]
                amount = data[index_of_row + 1][3]
                description = data[index_of_row + 1][4]

                # table cretion
                os.system('cls' if os.name == "nt" else 'clear') ###
                # headers = ['ID', 'Categorie', 'Date', 'Amount', 'Description']
                line = [[ID, categorie, date, amount, description]]
                table = tabulate(line, data[0], tablefmt="grid")

                print(table)

                # Get Categorie
                line[0][1] = input("Updated Expense Categorie : ").lower()
                os.system('cls' if os.name == "nt" else 'clear') ###
                table = tabulate(line, data[0], tablefmt="grid")
                print(table)

                # Get Amount 
                amount = None
                while amount is None:
                    amount = get_float("Updated Expense Amount : ", "float expected")

                line[0][3] = amount

                os.system('cls' if os.name == "nt" else 'clear') ###
                table = tabulate(line, data[0], tablefmt="grid")
                print(table)

                # Get Description
                line[0][4] = input("Updated Expense Description : ")
                os.system('cls' if os.name == "nt" else 'clear') ###
                table = tabulate(line, data[0], tablefmt="grid")
                print(table)

                # Get Date
                line[0][2] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                os.system('cls' if os.name == "nt" else 'clear') ###
                table = tabulate(line, data[0], tablefmt="grid")
                print(table)

                # Save or Cancel
                print("To save press enter (or any key other than the cancel words)")
                save = input("To Cancel type 'cancel' or 'cl' : ")
                if save.lower() in {'cancel', 'cl'}:
                    continue

                # TODO save 
                data[index_of_row + 1] = line[0]

            input("type anything to save and go back")

        elif choice == 4: # Delete Expense
            print(screen_delete_expense())

            index_of_row = None
            valid_indexes = set(range(len(data) - 1))

            while index_of_row is None:
                index_of_row = get_int_choice(
                    "Select expense by index (indexes start with 0): ",
                    "Expense not found (Index out of range)",
                    valid_indexes
                )

            table = tabulate([data[index_of_row + 1]], data[0], tablefmt="grid")
            print(table) # wished delete
            # Make sure delete or not
            sure = input("Are you sure of deleting this expense (yes, no): ")
            if sure.lower() in ('y', 'yes'):
                del data[index_of_row + 1]
            input("type anything to save and go back")

        # save to csv file
        with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(data)  # writerows writes all rows at once

if __name__=="__main__":
    main()

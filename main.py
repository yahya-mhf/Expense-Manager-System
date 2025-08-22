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
    
    +-----------------------------------------------+
    | ID | Categorie | date | amount  | description |
 -->|auto|    ...    | auto |   ...   |     ...     |<--
    +-----------------------------------------------+
    """

def screen_delete_expense():
    return """
    +-----------------+
    | Expense Tracker |     << Delete Expense >>
    +-----------------+
    
    +-----------------------------------------------+
    | ID | Categorie | date | amount  | description |
 -->|auto|    ...    | auto |   ...   |     ...     |<--
    +-----------------------------------------------+
    """

def main():
    while True: # App Loop
        os.system('cls' if os.name == "nt" else 'clear')

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
        while True:
            try:
                choice = int(input("Choice : "))
                if choice not in {0, 1, 2, 3, 4}: # Handle choice input
                    raise ValueError
            except ValueError:
                print("please enter a valid choice")
            else: # break if the choice is valid
                break

        # redirect to choice
        if choice == 0: # exit
            os.system('cls' if os.name == "nt" else 'clear')
            break

        elif choice == 1: # Create Expense.
            # default value of table
            ID = generate_id()
            categorie = '...'
            date = 'when you done creating'
            amount = 0
            description = '...'

            # table cretion
            os.system('cls' if os.name == "nt" else 'clear') ###
            headers = ['ID', 'Categorie', 'Date', 'Amount', 'Description']
            line = [[ID, categorie, date, amount, description]]
            table = tabulate(line, headers, tablefmt="grid")
            
            print(screen_create_expense(table))

            # Get Categorie
            line[0][1] = input("Expense Categorie : ")
            os.system('cls' if os.name == "nt" else 'clear') ###
            table = tabulate(line, headers, tablefmt="grid")
            print(screen_create_expense(table))

            # Get Amount 
            line[0][3] = int(input("Expense Amount : "))
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
            # add an index to reading for make it easy to delete or update
            table = tabulate(data[1:], data[0], tablefmt="grid")
            print(screen_read_expense(table))
            input("type anything to save and go back")

        elif choice == 3: # Update Expense.
            print(screen_update_expense())
            input("type anything to save and go back")

        elif choice == 4: # Delete Expense
            print(screen_delete_expense())
            input("type anything to save and go back")

        with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(data)  # writerows writes all rows at once

if __name__=="__main__":
    main()

from tabulate import tabulate

# TODO :
# 1. Take safe input from user
# 2. print dynamic screen
# 3. return a str table
# 4. Create expense : insert categorie, amount ...

## 1. Take safe input from user
# possible input : string, int, float, bool, list, dict, tuple
def get_choice(valid_numbers = None):
    try:
        choice = int(input("Choice : "))
        if not valid_numbers and choice not in valid_numbers: # Handle choice input
            raise ValueError
    except ValueError:
        print("please enter a valid choice")
        return
    else: # break if the choice is valid
        return choice

## 3. return a str table
def str_table(table, headers):
    return tabulate(table, headers, tablefmt="grid") # table:list[list], headers:list
# handle input choices. #DONE

# list[list] filter(data: list[list], filter_by: enum, filter_what)

# list[list] group(data: list[list])

# list[list] sort(data: list[list], sort_by: enum)
from tabulate import tabulate
from enum import Enum 
# +---------+----------+---------------+---------------------+----------+----------------------------------+
# |   index | ID       | Categorie     | Date                |   Amount | Description                      |
# +=========+==========+===============+=====================+==========+==================================+
# |       0 | 62987EXL | 0             | 2025-08-22 12:46:21 |     0    | 0                                |
# +---------+----------+---------------+---------------------+----------+----------------------------------+


## list[list] filter(data: list[list], filter_by: enum)
class Header(Enum):
    ID = 0
    CATEGORIE = 1
    DATE = 2
    AMOUNT = 3
    DESCRIPTION = 4



# default data
data = [
    ['ID', 'Categorie', 'Date', 'Amount', 'Description'],
    ['000-000', 'food', '8-22-2025 12:26', 100, 'this is a food 0 description'],
    ['000-001', 'travel', '8-22-2025 12:26', 200, 'this is a travel 0 description'],
    ['000-002', 'education', '8-22-2025 12:26', 300, 'this is an education description'],
    ['000-003', 'food', '8-22-2025 12:26', 40, 'this is a food 1 description'],
    ['000-004', 'travel', '8-22-2025 12:26', 204, 'this is a travel 1 description'],
    ['000-005', 'travel', '8-22-2025 12:26', 240, 'this is a travel 2 description'],
    ['000-006', 'travel', '8-22-2025 12:26', 250, 'this is a travel 3 description']
]

# filter(data: list[list], 2, "food")
def filter(data, filter_by_headers_index, filter_what):
    filtred_data = []
    for row in data:
        if row[filter_by_headers_index].lower() == filter_what.lower():
            filtred_data.append(row)
    return filtred_data

# filtred_data = filter(data, Header.CATEGORIE.value, "food")
# table = tabulate(filtred_data, data[0], tablefmt="grid")
# print(table)

print("filter by : ")
print("0. ID")
print("1. Categorie.")
print("2. Date.")
print("3. Amount.")

choice = int(input("Choice : "))
match Header(choice):
    case Header.ID:
        filter_what = input("ID : ")
        filtred_data = filter(data, Header.ID.value, filter_what)
        table = tabulate(filtred_data, data[0], tablefmt="grid")
        print(table)
    case Header.CATEGORIE:
        pass
    case Header.DATE:
        pass
    case Header.AMOUNT:
        pass
        
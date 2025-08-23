# handle input choices. #DONE

# list[list] filter(data: list[list], filter_by: enum, filter_what)

# list[list] group(data: list[list])

# list[list] sort(data: list[list], sort_by: enum)
from tabulate import tabulate
# +---------+----------+---------------+---------------------+----------+----------------------------------+
# |   index | ID       | Categorie     | Date                |   Amount | Description                      |
# +=========+==========+===============+=====================+==========+==================================+
# |       0 | 62987EXL | 0             | 2025-08-22 12:46:21 |     0    | 0                                |
# +---------+----------+---------------+---------------------+----------+----------------------------------+


## list[list] filter(data: list[list], filter_by: enum)

# default data
data = [
    ['ID', 'Categorie', 'Date', 'Amount', 'Description'],
    ['000-000', 'food', '8-22-2025 12:26', 100, 'this is a food 0 description'],
    ['000-001', 'travel', '8-22-2025 12:26', 200, 'this is a travel description'],
    ['000-002', 'education', '8-22-2025 12:26', 300, 'this is an education description'],
    ['000-003', 'food', '8-22-2025 12:26', 40, 'this is a food 1 description']
]

# filter(data: list[list], 2, "food")
def filter(data, filter_by_index, filter_what):
    filtred_data = []
    for row in data:
        if row[filter_by_index] == filter_what:
            filtred_data.append(row)
    return filtred_data

filtred_data = filter(data, 1, "food")
table = tabulate(filtred_data, data[0], tablefmt="grid")
print(table)

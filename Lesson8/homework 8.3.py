import json
dict_name = {
    '123456': ('Austen', 25),
    '123457': ('Eva', 27),
    '123458': ('Sophia', 31),
    '123459': ('Harry', 37),
    '123461': ('Felix', 30)}
with open('data.json', 'w') as file:
    json.dump(dict_name, file, indent=4)


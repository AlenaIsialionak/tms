import json
import csv
with open("data.json", "r") as r_file:
    data = json.load(r_file)
with open('data.csv', 'w', encoding='utf-8') as csv_file:
    fieldnames = ['id', 'name', 'age', 'phone']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter='\t')
    writer.writeheader()
    for key, value in data.items():
        writer.writerow({'id': key, 'name': value[0], 'age': value[1], 'phone': '090-46-41'})


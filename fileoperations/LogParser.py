import json

# file_name = "log.txt"
file_name = "fileoperations/log.txt"
file = open(file_name, "r")
data = []
order = ["date", "url", "type", "message"]

for line in file.readlines():
    details = line.split("|")
    details = [x.strip() for x in details]
    structure = {key: value for key, value in zip(order, details)}
    data.append(structure)

for entry in data:
    print(json.dumps(entry, indent=4))
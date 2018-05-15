import csv
import json

DATA = {
    "nodes": [],
    "links": []
}
nodes = set()
with open('data/result.csv', 'r') as csvfile:
    fieldnames = ("source","target","value")
    reader = csv.DictReader(csvfile)
    for line in reader:
        source = line["source"]
        target = line["target"]
        value = line["value"]
        nodes.add(source)
        nodes.add(target)
        DATA['links'].append(line)

for node in nodes:
    DATA['nodes'].append({"id": node , "group": int(node) % 3})

with open('data/result.json', 'w') as jsonfile:
    json_data = json.dumps(DATA)
    jsonfile.write(json_data)

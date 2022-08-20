import json
import csv

def tsv_to_json(tsvfile,jsonfile):

    data = {}

    tsvfile = open(tsvfile)
    tsvReader = csv.DictReader(tsvfile, delimiter="\t")
    for row in tsvReader:
        first = row['lesson']
        data[first] = row
            
    jsonfile = open(jsonfile, 'w') 
    jsonfile.write(json.dumps(data, indent=3))
    
tsv_to_json("TSVtoJSON.tsv","TSVtoJSON.json")   
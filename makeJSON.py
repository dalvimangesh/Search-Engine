import csv
import json

import sys

csv.field_size_limit(sys.maxsize)

f = csv.DictReader(open('marvel_wiki.csv'))

res = list()

for i in f:
    temp = dict()
    temp['id'] = str(int(i[''])+1)
    temp['Title'] = i['Title']
    temp['Summary'] = i['Summary']
    temp['Text'] = i['Text']
    temp['URL'] = i['URL']
    res.append(temp)

with open("dataset.json", "w") as outfile:
    json.dump(res, outfile)

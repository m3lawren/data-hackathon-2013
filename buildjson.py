#!/usr/bin/python

import codecs
import csv
import re
import json

def unicode_csv_reader(unicode_csv_data, dialect=csv.excel, **kwargs):
  # csv.py doesn't do Unicode; encode temporarily as UTF-8:
  csv_reader = csv.reader(utf_8_encoder(unicode_csv_data),
                            dialect=dialect, **kwargs)
  for row in csv_reader:
    # decode UTF-8 back to Unicode, cell by cell:
    yield [unicode(cell, 'utf-8') for cell in row]

def utf_8_encoder(unicode_csv_data):
  for line in unicode_csv_data:
      yield line.encode('utf-8') 

results = []

with codecs.open('speedtest-export-allmobilewithgps.csv', 'r', encoding='utf-8') as f:
  csvreader = unicode_csv_reader(f, delimiter=',', quotechar='"')
  for row in csvreader:
    if row[0] != "Score":
      jDict = {
        "score": int(row[0]),
        "latency": float(row[1]),
        "download": float(row[2]),
        "upload": float(row[3]),
        "browser": float(row[4]),
        "datetime": row[5],
        "latitude": float(row[6]),
        "longitude": float(row[7]),
        "time": int(row[8]),
        "carrier": row[9],
      }
      results.append(jDict)

print json.dumps(results)


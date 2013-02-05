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
    if row[1] != "Score":
      try:
        jDict = {
          "score": int(row[1]),
          "latency": float(row[2]),
          "download": float(row[3]),
          "upload": float(row[4]),
          "browser": float(row[5]),
          "datetime": row[6],
          "latitude": float(row[7]),
          "longitude": float(row[8]),
          "time": int(row[9]),
          "carrier": row[0],
        }
        results.append(jDict)
      except:
        print row
        raise 

print json.dumps(results)


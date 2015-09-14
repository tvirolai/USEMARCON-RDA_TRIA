#!/usr/bin/env python
# -*- coding: utf-8 -*

from pymarc import MARCReader
import sys


def read(inputfile):
  outputfile = "OUTPUTFILE.mrc"
  with open(inputfile, 'rb') as f:
    reader = MARCReader(f)
    for files in reader:
      try:
        record = next(reader)
        process(record)
        with open(outputfile, 'wb') as f2:
          f2.write(record.as_marc())
      except Exception as e:
        print(e)

def process(record):
  nimio = record.leader
  otsikko = record.title()
  record['245']['a'] = otsikko.upper()
  print("=000  " + nimio)
  for row in record:
    print(row)
  print("\n===================\n")


if __name__ == '__main__':
  if (len(sys.argv) == 2):
    inputfile = sys.argv[1]
  else:
    print(
        'Arguments: 1) inputfile')
    sys.exit()
  read(inputfile)

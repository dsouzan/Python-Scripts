#!/usr/bin/env python

import csv
filename = '/home/nelson/src/python/files/devices.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	print(header_row)




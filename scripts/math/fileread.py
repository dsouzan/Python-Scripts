#!/usr/bin/env python

import csv
file = open('/home/nelson/src/python/files/devices.csv')

print file.read()

exampleReader = csv.reader(file)
exampleData = list(exampleReader)
for row in exampleReader:
	print('Row #' + str(exampleReader.line_num) + '' + str(row))



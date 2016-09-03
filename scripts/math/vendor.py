#!/usr/bin/env python

import json

filename = '/home/nelson/src/python/files/vendor.json'
with open(filename) as f:
	load_data = json.load(f)
	
for vendor in load_data:
	if vendor['Value'] == '45':
		manufacturer = vendor['Manufacturer']
		device_type = vendor['Type']
		print(manufacturer + ": " + device_type)



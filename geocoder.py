#!/usr/bin/env python

import json
import urllib
import ConfigParser

config = ConfigParser.ConfigParser()
config.read('geocoder.cfg')
apikey = config.get('GMap API', 'key')
inputfile = config.get('Data', 'input')

for line in open(inputfile, 'r'):
	params = urllib.urlencode({
		'q': line.strip(),
		'output': 'json',
		'sensor': 'false',
		'key': apikey
	})
	f = urllib.urlopen("http://maps.google.com/maps/geo?%s" % params)
	s = f.read()
	j = json.loads(s)
	print j['Placemark'][0]['address']
	if j['Status']['code'] == 200:
		coords = j['Placemark'][0]['Point']['coordinates']
		print ', '.join([`num` for num in coords[0:2]])
	else:
		print 'could not find it'
	print ""

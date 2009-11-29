#!/usr/bin/env python

# Copyright 2009 Andrew Morton <drewish@katherinehouse.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

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

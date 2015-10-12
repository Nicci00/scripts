#!/usr/bin/env python

from sys import stdout
from time import sleep
from ConfigParser import SafeConfigParser
from xml.dom import minidom

import json
import requests

parser = SafeConfigParser()
parser.read('config.ini')

def fetch_XML():
	ice_user = parser.get('server', 'icecast_username')
	ice_pass = parser.get('server', 'icecast_password')
	ice_url = parser.get('server', 'xml_url')
	
	get = requests.get(ice_url, auth=(ice_user, ice_pass))
	return minidom.parseString(get.text)

def getArtist():
	return unicode(fetch_XML().getElementsByTagName('artist')[0].firstChild.data)

def getTitle():
	return unicode(fetch_XML().getElementsByTagName('title')[1].firstChild.data)

def getListeners(): 
	return int(fetch_XML().getElementsByTagName('listeners')[0].firstChild.data)

artist = getArtist()
title = getTitle()
listeners = getListeners()

def send_data():
	print(json.dumps({
		'artist' : artist,
		'title' : title,
		'listeners' : listeners
		}))

	stdout.flush()

send_data()

while True:
	sleep(2)

	rf_artist = getArtist()
	rf_title = getTitle()
	rf_listeners = getListeners()

	if (artist != rf_artist) or (title != rf_title) or (listeners != rf_listeners):

		artist = rf_artist
		title = rf_title
		listeners = rf_listeners

		send_data()

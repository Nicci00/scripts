#!/usr/bin/env python

from sys import stdout
from time import sleep
from ConfigParser import SafeConfigParser
import xml.etree.ElementTree as ET 
import json
import requests

parser = SafeConfigParser()
parser.read('config.ini')

def get_tree():
	ice_user = parser.get('server', 'icecast_username')
	ice_pass = parser.get('server', 'icecast_password')
	ice_url = parser.get('server', 'xml_url')

	get = requests.get(ice_url, auth=(ice_user, ice_pass))
	
	if get.status_code != 200:
		raise Exception("status code %s" % get.status_code)
	else:
		return ET.ElementTree(ET.fromstring(get.text))

def getArtist():
	return unicode(get_tree().find(".//artist").text)

def getTitle():
	return unicode(get_tree().findall(".//title")[1].text)

def getListeners(): 
	return int(get_tree().find(".//listeners").text)

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

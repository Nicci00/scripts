#!/usr/bin/env python

from time import sleep
from ConfigParser import SafeConfigParser
import xml.etree.ElementTree as ET
import sys
import json
import requests
import threading

parser = SafeConfigParser()
parser.read('config.ini')

data = None

def getTree():
	ice_user = parser.get('server', 'icecast_username')
	ice_pass = parser.get('server', 'icecast_password')
	ice_url = parser.get('server', 'xml_url')

	get = requests.get(ice_url, auth=(ice_user, ice_pass))

	if get.status_code != 200:
		raise Exception("Icecast Server status code %s" % get.status_code)
	else:
		return ET.ElementTree(ET.fromstring(get.text))


def getData():
	xmlTree = getTree()
	nodes = xmlTree.findall(".//listeners")

	return {
		"artist" : unicode(xmlTree.find(".//artist").text),
		"title" : unicode(xmlTree.findall(".//title")[1].text),
		"listeners" : int(nodes[1].text) + int(nodes[2].text)
	}


def send_data():
	print(json.dumps(data))
	sys.stdout.flush()


def send_tunein_data():
	req = requests.get("http://air.radiotime.com/Playing.ashx?partnerId={0}&partnerKey={1}&id={2}&title{3}&artist={4}".format(
			parser.get('tunein', 'partnerId'),
			parser.get('tunein', 'partnerKey'),
			parser.get('tunein', 'radioId'),
			data['title'].encode('utf-8'),
			data['artist'].encode('utf-8')))

	if req.status_code != 200:
		raise Exception("TuneIn Air API request status code %s" % get.status_code)


def watcher():
	global data
	global debug

	while True:
		sleep(2)
		rData = getData()

		if rData['title'] != data['title'] and rData['artist'] != data['artist']:
			data = rData
			send_data()
			send_tunein_data()


if __name__ == '__main__':

	debug = sys.argv[1] == '--debug'

	data = getData()

	send_data()
	send_tunein_data()

	thread = threading.Thread(target = watcher)
	thread.start()
	thread.join()

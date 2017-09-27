from sys import stdout
from time import sleep
import configparser
import xml.etree.ElementTree as ET
import json
import requests

parser = configparser.ConfigParser();

parser.read('config.ini')

data = None

def getTree():
	ice_user = parser.get('server', 'icecast_username')
	ice_pass = parser.get('server', 'icecast_password')
	ice_url = parser.get('server', 'xml_url')

	get = requests.get(ice_url, auth=(ice_user, ice_pass))

	if get.status_code != 200:
		raise Exception("status code %s" % get.status_code)
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

	stdout.flush()


def main():
	global data
	send_data()
	
	while True:
	
		sleep(2)
		rfData = getData()
	
		if rfData != data:
	
			data = rfData
			sleep(1)
			send_data()
	


if __name__ == '__main__':
	main()
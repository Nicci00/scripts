import sys
from mutagen.easyid3 import EasyID3

files = sys.argv
files.pop(0)

albums = []

for file in files:
	f = EasyID3(file)
	album = unicode(f['album'][0])
	if album not in albums:
		albums.append(album)

for a in albums: print a

sys.exit(0)

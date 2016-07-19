#!/usr/bin/env python2

from slugify import slugify
from mutagen.easyid3 import EasyID3
 
import os
import sys
from random import randint
 
if len(sys.argv) == 1:
	print('no folder given')
	exit(1)
 
music_folder = sys.argv[1]

files = filter(lambda x: x.endswith('.mp3'), os.listdir(music_folder))
 
for file in files:
	file_path = music_folder + file.decode('utf-8')

	id3 = EasyID3(file_path)

	slug = slugify(unicode(id3['title'][0]))
	rn = str(randint(11,99))

	print 'Old name: ' + file

	new_name = "{}_{}.mp3".format(str(rn), slug)
	os.rename(file_path, music_folder + new_name)

	print 'New name: ' + new_name + '\n'
 
exit(0)

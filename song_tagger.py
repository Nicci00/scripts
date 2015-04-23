#!/usr/bin/env python2
#-*- coding: utf-8 -*-
 
import sys
import os
from mutagen.easyid3 import EasyID3
 
files = sys.argv
 
if len(sys.argv) == 1:
	print("this script needs files to work")
	sys.exit(1)
 
files.pop(0)
 
for f in files:
 
	if not os.path.isfile(f):
		print("%s is not a valid file, skipping" % f)
		pass
 
	else:
		file = EasyID3(f)
	 
		print '\n----------------'
		print 'Filename: \n' + f
		print "Current title is: \n" + file["title"][0]
		print "Current artist is: \n" + file["artist"][0]
		print '----------------'
	 
		new_title = raw_input("Enter new title or press enter to leave it as is -> ")
		
		if (new_title != ''):
			file["title"] = [new_title]
			file.save()
	 
		new_artist = raw_input("Enter new artist or press enter to leave it as is -> ")
		
		if (new_artist != ''):
			file["artist"] = [new_artist]
			file.save()
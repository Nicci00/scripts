#!/usr/bin/env python2
#-*- coding: utf-8 -*-

import sys
import os
import eyed3
import subprocess

if len(sys.argv) == 1:
	print("this script needs files to work")
	sys.exit(1)

files = filter(lambda x: x.endswith('.mp3'), sys.argv)

use_chrom = '-c' in sys.argv

print "Got %d files for tagging" % len(files)

for f in files:

	if not os.path.isfile(f):
		print("%s is not a valid file, skipping" % f)
		pass

	else:
		file = eyed3.load(f)

		print '\n----------------'
		print 'Filename: \n' + f
		print "Current title is: \n" + file.tag.title
		print "Current artist is: \n" + file.tag.artist
		print '----------------'

		if file.tag.title and use_chrom:

			t = file.tag.title.replace(" ", "+")
			url = "http://www.project-imas.com/w/index.php?search=%s" % t

			print u'Opening new tab with search query \"%s\"' % file.tag.title

			#chromium in arch, chromium-browser in ubuntu
			with open(os.devnull, 'wb') as devnull:
				subprocess.check_call(['chromium-browser',
					url], stdout=devnull, stderr=subprocess.STDOUT)

		new_title = raw_input(
			"Enter new title or press enter to leave it as is -> ")

		if (new_title):
			file.tag.title = new_title.decode('utf-8')
			file.tag.save()

		new_artist = raw_input(
			"Enter new artist or press enter to leave it as is -> ")

		if (new_artist):
			file.tag.artist = new_artist.decode('utf-8')
			file.tag.save()

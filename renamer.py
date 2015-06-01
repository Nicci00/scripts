#!/usr/bin/env python2
 
import os
import sys
from random import randint
 
if len(sys.argv) == 1:
	print('no folder given')
	exit(1)
 
music_folder = sys.argv[1]
 
for file in os.listdir(music_folder):
 
	print 'old name: ' + file
	file_path = music_folder + file
	rn = str(randint(11,99))
	new_name = rn + file[2:]
 
	os.rename(file_path, music_folder + new_name)
	print 'new name: ' + new_name + '\n'
 
exit(0)

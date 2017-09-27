import sys
import os
from mutagen.easyid3 import EasyID3
import subprocess

def main():
	files = list(filter(lambda x: x.endswith('.mp3'), sys.argv))
	
	use_chrom = '-c' in sys.argv 
	
	print("Got %d files for tagging" % len(files))
	
	i = 1;
	l = len(files)
	for f in files:
	
		if not os.path.isfile(f):
			print("%s is not a valid file, skipping" % f)
			pass
	
		else:
			file = EasyID3(f)
			
			print('\n----------------')
			print( str(i) + ' of ' + str(l))
			print('Filename: \n' + f)
			print("Album: \n" + file["album"][0])
			print("Current title is: \n" + file["title"][0])
			print("Current artist is: \n" + file["artist"][0])
			print('----------------')
	
	
			if file["title"] and use_chrom:
	
				t = file["title"][0].replace(" ", "+")
				url = "http://www.project-imas.com/w/index.php?search=%s" % t
	
				print('Opening new tab with search query \"%s\"' % file["title"][0])
	
				with open(os.devnull, 'wb') as devnull:
					subprocess.check_call(['chromium-browser', url], stdout=devnull, stderr=subprocess.STDOUT)
	
		
			new_title = input("Enter new title or press enter to leave it as is -> ")
			
			if (new_title != ''):
				file["title"] = [new_title]
				file.save()
		
			new_artist = input("Enter new artist or press enter to leave it as is -> ")
			
			if (new_artist != ''):
				file["artist"] = [new_artist]
				file.save()

			i = i + 1

	#end for

if __name__ == '__main__':
	try:
		if len(sys.argv) == 1:
			print("this script needs files to work")
			sys.exit(1)

		main()

	except (KeyboardInterrupt, EOFError):
		print('\ncya nerd')
		try:
			sys.exit(0)
		except SystemExit:
			os._exit(0)

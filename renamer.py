from slugify import slugify
from mutagen.easyid3 import EasyID3

import os
import sys
from random import randint

def main():
	if len(sys.argv) == 1:
		print('no folder given')
		exit(1)

	music_folder = sys.argv[1]


	files = list(filter(lambda x: x.endswith('.mp3'), os.listdir(music_folder)))

	if len(files) == 0:
		print('No files to rename')
		exit(1)
	else:
		print('Renaming {} files'.format(str(len(files))))

	dry_run = '--d' in sys.argv

	process_files(music_folder, files, dry_run)
	exit(0)


def process_files(music_folder, files, dry_run):

	if dry_run:
		print("~~~ Dry run ~~~\n")

	for file in files:
		new_name = ""
		file_path = music_folder + file

		try:

			id3 = EasyID3(file_path)

			slug = slugify(id3['title'][0])
			rn = str(randint(11,99))

			print('Old name: ' + file)

			new_name = "{}_{}.mp3".format(str(rn), slug)

			if not dry_run:
				os.rename(file_path, music_folder + new_name)

			print('New name: ' + new_name + '\n')
		
		except Exception as e:
			print("Exception processing file")
			print(str(e) + "\n")


if __name__ == '__main__':
	main()
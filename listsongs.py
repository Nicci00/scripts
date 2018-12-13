import sys
from mutagen.easyid3 import EasyID3

files = files = list(filter(lambda x: x.endswith('.mp3'), sys.argv))

trouble_files = []

for file in files:
	try:
		f = EasyID3(file)

		print("Filename: "+ file)
		print("Artist: " + f["artist"][0])
		print("Album: " + f["album"][0])
		print("Title: " + f["title"][0])
		print("\n")

	except Exception as e:
		trouble_files.append({
			"file" : file,
			"e": str(e)
			})

for tf in trouble_files:
	print("\n !!!")
	print("Filename: "+ tf['file'])
	print("Exception: "+tf['e'])


print("{} files present, {} files reported tagging errors".format(len(files), len(trouble_files)))

sys.exit(0)



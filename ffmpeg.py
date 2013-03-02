"""2-Pass x264 encoding with ffmpeg"""

from subprocess import call
from os.path import splitext

def encode(files, bit_rate="2M", profile="main", preset="fast", audio="-c:a copy -map 0", extra="", extension="mp4", dry=False):
	for infile in files:
		print 'Processing '+infile+'...'
		basename = splitext(infile)[0]
		outfile = basename+'.'+extension
		core='ffmpeg -i ' + infile + ' -threads auto -c:v libx264 -tune film -preset ' + preset + ' -profile:v ' + profile + ' -b:v ' + bit_rate + ' -passlogfile ' + basename + ' ' + extra;
		firstpass=core+' -pass 1 -an -f rawvideo -y /dev/null'
		secondpass=core+' -pass 2 ' + audio + ' ' + outfile
		if(dry):
			print(firstpass)
			print(secondpass)
		else:
			call(firstpass.split())
			call(secondpass.split())
			call(['rm', basename+'-0.log', basename+'-0.log.mbtree'])
	

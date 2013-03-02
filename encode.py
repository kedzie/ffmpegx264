"""2-Pass x264 encoding with ffmpeg"""

from subprocess import call
from os.path import splitext
from argparse import ArgumentParser
import sys

def encode(files, bit_rate="2M", profile="main", preset="fast", audio="-c:a copy -map 0", extra="", extension="mp4", dry=False):
	"""
	Perform 2-pass encoding of multiple files using ffmpeg in operating system
	"""
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
	
if __name__ == "__main__":
	parser = ArgumentParser(description='X264 Encoder')
	parser.add_argument('files', nargs='+', help='files to encode (wildcard)')
	parser.add_argument('-b', '--bit_rate', action='store', default='2M', help='Bit Rate')
	parser.add_argument('-e', '--extension', action='store', default='mp4', help='Output format')
	parser.add_argument('-k', '--profile', action='store', default='main', help='x264 Profile')
	parser.add_argument('-p', '--preset', action='store', default='medium', help='x264 Preset')
	parser.add_argument('-a', '--audio', action='store', default='-c:a copy -map 0', help='Audio encoding arguments')
	parser.add_argument('-x', '--extra', action='store', default='', help='Extra arguments')
	parser.add_argument('-d', '--dry', action='store_true', help='Dry run. No actual encoding is performed')
	a = parser.parse_args();
	ffmpeg.encode(a.files, a.bit_rate, a.profile, a.preset, a.audio, a.extra, a.extension, a.dry) 

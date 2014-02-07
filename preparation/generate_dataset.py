'''
this script parses human-readable raw data and generates corresponding BGP dataset.
@author: yingjun
'''

import os

outfile=file("raw_path.txt", 'w')
def extract_raw_path(dirname, filename):
	infile=file(dirname+'/'+filename)
	for i in range(5):
		infile.readline()
	while 1:
		line=infile.readline()
		if line=='':
			break
		line=line.strip().split()
		outfile.write(' '.join(line[7:-1])+'\n')

def traverse_directory(directory, function):
	for root, dirs, files in os.walk(directory):
		for file in files:
			function(directory, file)

if __name__=='__main__':
	traverse_directory('sampledata', extract_raw_path)


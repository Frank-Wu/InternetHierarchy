'''
this script parses human-readable raw data (e.g., raw data in year 1999 from rrc00) and generates corresponding BGP dataset.
@author: yingjun
'''

import os

outfiles={}

def extract_raw_path(filename, outfile):
	infile=file(filename)
	for i in range(6):
		infile.readline()
	while 1:
		line=infile.readline()
		if line=='':
			break
		line=line.strip().split()
		outfile.write(' '.join(line[7:-1])+'\n')

def traverse_directory(directory, function):
	for root, dirs, files in os.walk(directory):
		for dirname in dirs:
			outfiles[dirname]=file('result/'+dirname, 'a')
		for filename in files:
			fullname=os.path.join(root, filename)
			outfile=outfiles[fullname.split('/')[-2]]
			if 'bview' not in fullname:
				print filename
				function(fullname, outfile)

if __name__=='__main__':
	traverse_directory('data.ris.ripe.net/rrc00', extract_raw_path)


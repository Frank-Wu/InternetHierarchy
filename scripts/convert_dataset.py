import random
import sys
import os
import pickle

dictionary=[]

def convert_dataset(infile, outfile):
	f=file(infile, "r")
	while 1:
		line=f.readline()
		if line=="":
			break
		words=line.strip().split(" ")
		#since we need to remove initial AS, i.e., vantage point AS, we need to guarantee that number of ASes in a single path should be larger than 2.
		if len(words)<=2:
			continue
		for i in words[1:]:
			if i not in dictionary:
				dictionary.append(i)
	f.seek(0)
	g=file(outfile, "w")
	while 1:
		line=f.readline()
		if line=="":
			break
		words=line.strip().split(" ")
		if len(words)<=2:
			continue
		for i in words[1:]:
			g.write(str(dictionary.index(i)+1)+";")
		g.write("0;\n")
	f.close()
	g.close()
	info=file(outfile+".size", "w")
	info.write(str(len(dictionary)+1)+'\n')
	info.close()
	pickle.dump(dictionary, open(outfile+".dic", "wb"), 1)
	return len(dictionary)+1

def generate_states(obs_num, state_num, outfilename):
	f=file(outfilename, "w")
	f.write("Hmm v1.0\n\n")
	f.write("NbStates "+str(state_num)+"\n")
	#initial probability. the last state with prob=0.
	pi=[]
	for i in range(state_num-1):
		pi.append(random.random())
	pi_sum=sum(pi)
	pi=map(lambda x: x/pi_sum, pi)
	####
	for prob in pi:
		f.write("\nState\n")
		f.write("Pi "+str(prob)+"\n")
		#transition probability.
		A=[]
		for i in range(state_num):
			A.append(random.random())
		A_sum=sum(A)
		A=map(lambda x: x/A_sum, A)
		f.write("A")
		for a in A:
			f.write(" "+str(a))
		f.write("\n")
		####
		f.write("IntegerOPDF [")
		f.write("0")
		for p in range(obs_num-1):
			f.write(" "+str("%.8f" %(1.0/(obs_num-1))))
		f.write("]\n")
	#terminal state
	f.write("\nState\n")
	f.write("Pi 0\n")
	f.write("A")
	for a in range(state_num-1):
		f.write(" 0")
	f.write(" 1\n")
	
	f.write("IntegerOPDF [")
	f.write("1")
	for p in range(obs_num-1):
		f.write(" 0")
	f.write("]\n")
	####
	f.close()

def preprocess_dataset(infilename, outfileprefix):
	obs_num=convert_dataset(infilename, outfileprefix+".seq")
	for i in range(4, 8):
		generate_states(obs_num, i, outfileprefix+"."+str(i)+".hmm")

def traverse_directory(directory, function):
	for root, dirs, files in os.walk(directory):
		for filename in files:
			infilename=os.path.join(root, filename)
			outfileprefix='hmmdataset/'+filename
			function(infilename, outfileprefix)

if __name__=="__main__":
	year=sys.argv[1]
	filename=year+'.01'
	preprocess_dataset('dataset/'+filename, 'hmmdataset/'+filename)
#	traverse_directory('dataset', preprocess_dataset)

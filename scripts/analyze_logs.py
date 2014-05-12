import random
import sys
import pickle

dictionary = []

def analyze_category(infile, outfile, state_size):
	f = file(infile, "r")
	g = file(outfile, "w")
	for i in range(4):
		f.readline()
	for i in range(state_size):
		f.readline()
		g.write(f.readline())
		g.write(f.readline())
		line = f.readline()
		line = line.replace("IntegerOPDF [", "").replace("]", "")
		line = line.strip().split(" ")
		pdf=[]
		pdf = map(lambda x: float(x), line)
		pdf_map = {pdf[i]: i for i in range(len(pdf))}
		sorted_pdf_map = sorted(pdf_map.items(), key=lambda x:x[0], reverse=True)
		top = [x[1] for x in sorted_pdf_map[:20]]
		name_map = pickle.load(open("name_pickle.dat", "rb"))
		for i in top:
			if i==0:
				break
			try:
				g.write(str(i-1) + " : " + str(dictionary[i-1]) + " : " + str(pdf[i]) + " : " + name_map[str(dictionary[i-1])]+'\n')
			except:
				g.write(str(i-1) + " : " + str(dictionary[i-1]) + " : " + str(pdf[i]) + " : unknown"+'\n')
		f.readline()
		f.readline()
		g.write("=========================================\n")
	f.close()
	g.close()

def analyze_AS(infile, outfile, state_size):
	f=file(infile, "r")
	g=file(outfile, "w")
	for i in range(4):
		f.readline()
	for i in range(state_size):
		f.readline()
		

if __name__ == '__main__':
	year=sys.argv[1]
	state_num=sys.argv[2]
	filename=year+'.01.'+state_num+'.hmm'
	dicname=year+'.01.seq.dic'
	dictionary=pickle.load(open("hmmdataset/"+dicname, "rb"))
	analyze_log("hmmresult/"+filename, "hmmresult/"+filename+'.analysis', int(state_num))

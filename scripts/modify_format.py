import sys

def modify_format(infilename, outfilename, state_size):
    infile = file(infilename, "r")
    outfile = file(outfilename, "w")
    for i in range(4):
        outfile.write(infile.readline())
    for i in range(state_size):
        outfile.write(infile.readline())
        outfile.write(infile.readline())
        outfile.write(infile.readline())
        line = infile.readline()
        line = line.replace("IntegerOPDF [", "").replace("]", "")
        line = line.strip().split(" ")
        pdf = map(lambda x: float(x), line)
        
        outfile.write("IntegerOPDF [")
        for p in pdf:
            outfile.write(str("%.7f" % p))
        outfile.write("]\n")
        
        outfile.write(infile.readline())
        outfile.write(infile.readline())
    infile.close()
    outfile.close()

if __name__ == '__main__':
    year=sys.argv[1]
    state_num=sys.argv[2]
    filename=year+'.01.'+state_num+'.hmm'
    modify_format("hmmresult/"+filename, "hmmresult/"+filename+'.mod', int(state_num))

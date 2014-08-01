'''
Created on Aug 1, 2014
'''

import sys
if __name__ == '__main__':
    year=sys.argv[1]
    month=sys.argv[2]
    category=sys.argv[3]
    f=file(year+"."+month+"."+category+".hmm", "r")
    g=file(year+"."+month+"."+category+".hmm.reorder", "w")
    srcpi=[]
    A=[]
    for i in range(int(category)):
        tmp=f.readline().strip().lstrip("Pi ")
        srcpi.append(tmp)
        dstpi=sorted(srcpi)
        dstpi.reverse()
        tmp=f.readline().strip().lstrip("A ").split()
        A.append(tmp)

    reorder=[]
    for ele in srcpi:
        for i in range(len(dstpi)):
            if ele==dstpi[i]:
                if i not in reorder:
                    reorder.append(i)
                    break
    print srcpi, dstpi
    print reorder
    
    newA=[]
    for arr in A:
        newarr=[0]*int(category)
        for i in range(len(arr)):
            newarr[reorder[i]]=arr[i]
        newA.append(newarr)
    
    newA1=[[]]*int(category)
    for i in range(len(newA)):
        newA1[reorder[i]]=newA[i]
    
    print A
    print newA1
    g.write(" ".join(dstpi)+"\n\n")
    for i in newA1:
        g.write(" ".join(i)+"\n")
    
    
    
    
    
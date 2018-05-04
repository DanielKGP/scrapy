import os
import sys
import os.path
def split(file):
    if not os.path.isfile(file):
        print file,"is not a file"
        exit(1)
    txtfile=open(file,"r")

    #dirname=os.path.dirname(file)
    dirname='/Users/keguanpai/Documents/pyscrapy/doc'

    file_index=0

    line_cnt = 0
    outfile=open(dirname+"/output_%d"%file_index+'.txt','w')
    for line in txtfile:
        if line_cnt < 1:
            outfile.write(line)
            line_cnt+=1
        else:
            outfile.close()
            file_index+=1
            outfile=open(dirname+"/output_%d"%file_index+'.txt','w')
            line_cnt=0

    outfile.close()
    txtfile.close()


split('/Users/keguanpai/Documents/pyscrapy/title.html')

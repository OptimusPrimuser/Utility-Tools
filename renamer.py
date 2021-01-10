import sys
import os

#path no_space prefix suffix
""" 
args=[i for i in sys.argv]
#print(args)

#Enter your path here
path= args[1]

#If you want remove spaces then set True
no_space=bool(args[2])

#text Behind of filename prefix="LoL" then file will be "LoLFilename" 
prefix=args[3]
#text Ahead of filename suffix="LoL" then file will be "FilenameLoL" 
#suffix="_flip"
#suffix="_h_flip"
suffix=args[4] """
def renaming(path,no_space,prefix,suffix):
    real=os.listdir(path)
    real=[i for i in real if i.find(".")!=-1]



    renamed=[prefix+i.split(".")[0]+suffix+"."+i.split(".")[1] for i in real]
    if no_space==True:
        renamed=[i.replace(" ","") for i in renamed]

    for i in range(len(real)):
        os.rename(path+"\\"+real[i], path+"\\"+renamed[i])

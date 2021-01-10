import os
#import sys
from shutil import copy
from shutil import move
""" #input output moveOrCopy folderSuffix
input_folder=sys.argv[1]
output_folder=sys.argv[2]
# 0 = copy 1 = move
moveOrCopy=bool(int(sys.argv[3]))
# 0 = false 1 = true
folder_suffix=bool(int(sys.argv[4])) """

def singler(input_folder,output_folder,moveOrCopy,folder_suffix):
    files_to_transfer=[]

    for root,dirs,files in os.walk(input_folder):
        temp=[root+'/'+i for i in files]
        files_to_transfer=files_to_transfer+temp
    if moveOrCopy==False:
        for i in files_to_transfer:
            fileOUT=i
            if folder_suffix==True:
                i=i.replace('/','\\')
                file=i.split('\\')[-1].split('.')
                root=i.split('\\')[-2]
                fileOUT=file[0]+'_'+root+file[1]
            copy(i,output_folder+'\\'+fileOUT)
    else:
        for i in files_to_transfer:
            fileOUT=i
            if folder_suffix==True:
                i=i.replace('/','\\')
                file=i.split('\\')[-1].split('.')
                #print(i.split('\\'))
                root=i.split('\\')[-2]
                #print(root)
                fileOUT=file[0]+'_'+root+'.'+file[1]
            move(i,output_folder+'\\'+fileOUT)

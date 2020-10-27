import time
import datetime
import os,glob
import shutil
import re

input1 = input("기존의 스케쥴을 정리하시겠습니까? Y/N")
input1 = input1.lower()
a = re.compile(".py$")
print("1")
if input1 =='y':
    print("2")
    for file in glob.glob("*_*"):
        print("3")
        if a.search(file):
            continue
        else:
            print("1")
            
            
    print(glob.glob('*_*'))

        #shutil.move(file,'Past/')
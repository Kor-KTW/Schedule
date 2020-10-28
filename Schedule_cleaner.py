import time
import datetime
from datetime import datetime as dt
import os,glob
import shutil
import re

input1 = input("기존의 스케쥴을 정리하시겠습니까? Y/N")
input1 = input1.lower()
a = re.compile(".py$")
b = re.compile("_")
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
    if b.search(file):
        print('a')
        #shutil.move(file,'Past/')
    todaynumber = datetime.datetime.today()
    print(b.search(str(todaynumber)))
    print(b.findall(str(todaynumber)))

    print(str(todaynumber))
    td = datetime.timedelta(days=1) # 100일 저장
    i = dt.strptime('2020_11_01','20%y_%m_%d')
    print(type(i))
    print(type(todaynumber))
    # if todaynumber > todaynumber+td:
    if todaynumber > i:
        print(1)
    else:
        print(2)
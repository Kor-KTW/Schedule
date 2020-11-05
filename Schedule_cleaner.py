import shutil
import time
import datetime
from datetime import datetime as dt
import os,glob
import shutil
import re

input1 = input("지난 스케쥴을 정리하시겠습니까? Y/N")
input1 = input1.lower()
a = re.compile(".py$")
b = re.compile("_")
todaynumber = datetime.date.today()
# print("1")
if input1 =='y':
#    print("2")
    for file in glob.glob("*_*"):
        ordering = str(file).replace("_","")
        ordering2 = str(todaynumber).replace("-","")
        # print(ordering)
        if a.search(ordering):
#            print(str(file)+"은 스케쥴 파일이 아닙니다.")
            continue
        else:
            # print(ordering, ordering2)
            if int(ordering) < int(ordering2):
                shutil.move(file,'Past/')
                print(str(file)+"(년_월_일)에 해당하는 스케쥴이 이동되었습니다.")
    print("모든 지난 스케쥴의 이동이 완료되었습니다.")

        

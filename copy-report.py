import os
import os.path
import shutil

def copiaric(s,d):
    global fatti,falliti,txt
    appl=os.listdir(s)
    appl.sort()
    for x in appl:
        if not(fatti % 300):
            print('copied:',fatti)
        if os.path.isfile(s+'\\'+x):
            fatti+=1
            try:
                shutil.copy(s+'\\'+x,d+'\\'+x)
            except:
                falliti+=1
                txt+=s+'\\'+x+'\n'
                try:
                    os.remove(d+'\\'+x)
                except:
                    pass
        else:
            try:
                os.mkdir(d+'\\'+x)
            except:
                falliti+=1
                txt+=s+'\\'+x+'\n - this folder already exists \n'
            copiaric(s+'\\'+x,d+'\\'+x)


fatti=0
falliti=0
txt=''
print("""This program copy folders and files and produce a report,
It's usefull with damages or unstable units such as old harddrives, damaged usb or unstable network units""")
source=input("Insert source folder (full path, you may copy and paste it)\n")
dest=input('Insert destination path (It has to exist already, if not create it before to start the copy )\n')
copiaric(source,dest)
print('copy finished, copied:',fatti,', failed',falliti,' see ',dest+'\\failed.txt')
txt+='copied: '+str(fatti)+' failed: '+str(falliti)
fd=open(dest+'\\failed.txt','w')
fd.write(txt)
fd.close()

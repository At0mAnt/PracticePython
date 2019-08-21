#!python3
#klip.py - script for a key clip library

#How to use
#py.exe klip.pyw save <keyword> - inserts cb content using key as accessor
#py.exe klip.pyw <keyword> - pastes key content onto cb
#py.exe klip.pyw list - loads keys to cb
#py.exe klip.pyw delete <keyword> - 

import sys, shelve, pyperclip
df = shelve.open('KlipBook')
if(len(sys.argv) == 3):
    if(sys.argv[1].lower() == 'save'):
        df[sys.argv[2]] = pyperclip.paste()
        print(str(sys.argv[2] + ' was put on klipbook'))
    elif(sys.argv[1].lower() == 'delete'  and sys.argv[2] in df):
        del df[sys.argv[2]]
        print(str(sys.argv[2] + ' was wiped'))
        
elif(len(sys.argv) == 2):
    
    if(sys.argv[1].lower() == 'list'):
        pyperclip.copy(str(list(df.keys())))
    elif(sys.argv[1] in df):
        pyperclip.copy(df[sys.argv[1]])
        
df.close()


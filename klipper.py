#!python3
#klipper.py - a module for modifying a klipbook data file

import shelve, pyperclip

#klipperInsert(key, fileName | default(KlipBook)) - inserts clipboard content using specified keyword and filename
def klipperInsert(wordKey,book_Name='KlipBook'):
    df = shelve.open(book_Name)
    df[wordKey]=pyperclip.paste()
    df.close()
    return wordKey + ' was added to ' + book_Name

#klipperErase(key, fileName | default(KlipBook)) - deletes the key content from the specified klipbook file
def klipperErase(wordKey, book_Name='KlipBook'):
    df = shelve.open(book_Name)
    del df[wordKey]
    df.close()
    return wordKey + ' was deleted from ' + book_Name

#klipperGet(key, fileName | default(KlipBook)) - pastes the content of the key from the specified klipbook file 
def klipperGet(wordKey, book_Name='KlipBook'):
    df = shelve.open(book_Name)
    if(wordKey in df):
        pyperclip.copy(df[wordKey])
        df.close()
        return wordKey + " from " + book_Name + " was pasted to the clipboard "
    else:
        df.close()
        return wordKey + " from " + book_Name + " was missing "
    
#klipperKeys(fileName | default(KlipBook)) - returns the keys from the specified klipbook file
def klipperKeys(book_Name='KlipBook'):
    df = shelve.open(book_Name)
    keys = str(list(df.keys()))
    df.close()
    return keys


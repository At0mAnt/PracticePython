from tkinter import *
from tkinter import ttk
import pyperclip, klipper

def getWord(*args):
    try:
        value , bookName, mValue = keyWord.get(), klipBook.get(),radioValue.get()
        if(mValue == 'Add'):
            reValue.set(klipper.klipperInsert(value,bookName))
        elif(mValue == 'List'):
            reValue.set(klipper.klipperKeys(bookName))
        elif(mValue == 'Toss'):
            reValue.set(klipper.klipperErase(value,bookName))
        else:
            reValue.set(klipper.klipperGet(value,bookName))

    except ValueError:
        pass
    
root = Tk()
root.title("Klipboard 2.0")

mainframe = ttk.Frame(root, padding="17 17 52 52")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

keyWord = StringVar()
reValue = StringVar()
klipBook = StringVar()
radioValue = StringVar()
radioLabels = {'Find & Get':1,'Add':2, 'List':3,'Toss':4}
radioValue.set('Add')
klipBook.set('KlipBook')

keyWord_entry = ttk.Entry(mainframe, width=12, textvariable=keyWord)
keyWord_entry.grid(column=2, row=1, sticky=(W+E))

ttk.Label(mainframe, textvariable=reValue).grid(column=1,row=4,columnspan=7, sticky=(W+E))
for val, radioLabel in enumerate(radioLabels):
    ttk.Radiobutton(root,text=radioLabel,variable=radioValue,value=radioLabel).grid(column=0,columnspan=5,row=(val+2),stick=W)


ttk.Button(mainframe, textvariable=radioValue, command=getWord).grid(column=4, row=2, sticky=W+E)


ttk.Label(mainframe, text="Klip word: ").grid(column=1, row=1, sticky=W+E)
ttk.Label(mainframe, text="File name:").grid(column=1, row=2, sticky=W+E)
klipBook_entry = ttk.Entry(mainframe,width=12, textvariable=klipBook)
klipBook_entry.grid(column=2, row=2, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

keyWord_entry.focus()
root.bind('<Return>', getWord)

root.mainloop()

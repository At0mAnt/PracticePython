from tkinter import *
from tkinter import ttk
import pyperclip, klipper

def getWord(*args):
    try:
        value , bookName, mValue = keyWord.get(), klipBook.get(),menuValue.get()
        if(mValue == 'Add to '):
            reValue.set(klipper.klipperInsert(value,bookName))
        elif(mValue == 'List from'):
            reValue.set(klipper.klipperKeys(bookName))
        elif(mValue == 'Toss from'):
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
menuValue = StringVar()
menuItems = {'Find & Get from', 'Add to ', 'List from','Toss from'}
menuValue.set('Add to')
klipBook.set('KlipBook')

keyWord_entry = ttk.Entry(mainframe, width=12, textvariable=keyWord)
keyWord_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, textvariable=reValue).grid(column=1, row=4, sticky=(E))
popupMenu = OptionMenu(mainframe, menuValue, *menuItems)
popupMenu.grid(row=2, column=3 , sticky=(E))
ttk.Button(mainframe, textvariable=menuValue, command=getWord).grid(column=3, row=3, sticky=W)


ttk.Label(mainframe, text="Klip Word: ").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="in the :").grid(column=1, row=2, sticky=E)
klipBook_entry = ttk.Entry(mainframe,width=12, textvariable=klipBook)
klipBook_entry.grid(column=2, row=2, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

keyWord_entry.focus()
root.bind('<Return>', getWord)

root.mainloop()

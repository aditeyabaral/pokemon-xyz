from Tkinter import *


def show_entry_fields():
   print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))

master = Tk()
master.title = ("Pokemon X, Y and Z")
Label(master, text="Enter Name").grid(row=0)

e1 = Entry(master)

e1.grid(row=0, column=1)

Button(master, text='Quit').grid(row=3, column=0, sticky=W, pady=4)

mainloop( )

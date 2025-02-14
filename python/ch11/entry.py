from tkinter import *
oroot = Tk()
oroot.geometry("400x300")

ostring = StringVar()
oentry=Entry(oroot,textvariable=ostring)
oentry.pack()

olabel = Label(oroot,bg="yellow",textvariable=ostring)
olabel.pack()
oroot.mainloop()
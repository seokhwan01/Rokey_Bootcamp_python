from tkinter import *

otk=Tk()
otk.geometry("200x100")

obtn1=Button(otk,text="PUSH1")
obtn2=Button(otk,text="PUSH2")
obtn3=Button(otk,text="PUSH3")

obtn1.grid(row=2,column=0)
obtn2.grid(row=2,column=1)
obtn3.grid(row=3,column=3)

otk.mainloop()
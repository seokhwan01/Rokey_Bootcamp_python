from tkinter import *

otk=Tk()
otk.geometry("400x300+400+400")

obtn1=Button(otk,text="PUSH1")
obtn2=Button(otk,text="PUSH2")
obtn3=Button(otk,text="PUSH3")


# obtn1.grid(row=1,column=0) 상대적으로 사용하므로 믹스로 사용 못함
obtn1.place(x=10,y=10)
obtn2.pack(side="right")
obtn3.place(x=80,y=60)
otk.mainloop()
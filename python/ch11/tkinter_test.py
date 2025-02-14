# import tkinter
# otk = tkinter.Tk()
# obtn=tkinter.Button(otk,text="click")
# obtn.pack()
# otk.mainloop()

from tkinter import *
from tkinter import Tk #가독성 위해
from tkinter import Button #이렇게 변경
def hello():
    print("안녕노무통")
otk=Tk()
otk.geometry("400x300+400+400")
#obtn=Button(otk,text="click",command=hello)
obtn1=Button(otk,text="PUSH1",command=hello)
obtn2=Button(otk,text="PUSH1",command=hello)
obtn3=Button(otk,text="PUSH1",command=hello)
obtn1.pack()
obtn2.pack()
obtn3.pack()
otk.mainloop()
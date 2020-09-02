from tkinter import *
import parser
from math import factorial
p=Tk()
p.title("Calculater")
i=0
def get_variables(num):
    global i
    display.insert(i,num)
    i+=1
def get_operations(op):
    global i
    d=len(op)
    display.insert(i,op)
    i+=d
def undo():
    tot=display.get()
    if len(tot):
        modstr=tot[0:-1]
        all_clear()
        display.insert(0,modstr)
    else:
        all_clear()
        display.insert(0,"Error")
def all_clear():
    display.delete(0,END)
def calculate():
    entireString=display.get()
    try:
        a=parser.expr(entireString).compile()
        result=eval(a)
        all_clear()
        display.insert(0,result)
    except Exception:
        all_clear()
        display.insert(0,"Error")
def fact():
    entire_string=display.get()
    try:
        ans=factorial(int(entire_string))
        all_clear()
        display.insert(0,ans)
    except Exception:
        all_clear()
        display.insert(0,"Error")
display=Entry(p)
display.grid(row=0,columnspan=6,sticky=N+E+W+S)
Button(p,text="1",command=lambda :get_variables(1)).grid(row=2,column=0,sticky=N+S+W+E)
Button(p,text="2",command=lambda :get_variables(2)).grid(row=2,column=1,sticky=N+S+W+E)
Button(p,text="3",command=lambda :get_variables(3)).grid(row=2,column=2,sticky=N+S+W+E)
Button(p,text="4",command=lambda :get_variables(4)).grid(row=3,column=0,sticky=N+S+W+E)
Button(p,text="5",command=lambda :get_variables(5)).grid(row=3,column=1,sticky=N+S+W+E)
Button(p,text="6",command=lambda :get_variables(6)).grid(row=3,column=2,sticky=N+S+W+E)
Button(p,text="7",command=lambda :get_variables(7)).grid(row=4,column=0,sticky=N+S+W+E)
Button(p,text="8",command=lambda :get_variables(8)).grid(row=4,column=1,sticky=N+S+W+E)
Button(p,text="9",command=lambda :get_variables(9)).grid(row=4,column=2,sticky=N+S+W+E)
Button(p,text="+",command=lambda :get_operations("+")).grid(row=2,column=3,sticky=N+S+W+E)
Button(p,text="*",command=lambda :get_operations("*")).grid(row=3,column=3,sticky=N+S+W+E)
Button(p,text="/",command=lambda :get_operations("/")).grid(row=4,column=3,sticky=N+S+W+E)
Button(p,text="-",command=lambda :get_operations("-")).grid(row=5,column=3,sticky=N+S+W+E)
Button(p,text=".",command=lambda :get_variables(".")).grid(row=5,column=2,sticky=N+S+W+E)
Button(p,text="AC",command=lambda :all_clear()).grid(row=5,column=0,sticky=N+E+W+S)
Button(p,text="0",command=lambda :get_variables(0)).grid(row=5,column=1,sticky=N+E+W+S)
Button(p,text="%",command=lambda :get_operations("%")).grid(row=3,column=4,sticky=N+E+W+S)
Button(p,text="pi",command=lambda :get_operations("*3.14")).grid(row=2,column=4,sticky=N+E+W+S)
Button(p,text="exp",command=lambda :get_operations("**")).grid(row=5,column=4,sticky=N+E+W+S)
Button(p,text="(",command=lambda :get_operations("(")).grid(row=4,column=4,sticky=N+E+W+S)
Button(p,text=")",command=lambda :get_operations(")")).grid(row=4,column=5,sticky=N+E+W+S)
Button(p,text="<-",command=lambda :undo()).grid(row=2,column=5,sticky=N+E+W+S)
Button(p,text="x!",command=lambda :fact()).grid(row=3,column=5,sticky=N+E+W+S)
Button(p,text="^2",command=lambda :get_operations("**2")).grid(row=5,column=5,sticky=N+E+W+S)
Button(p,text="=",command=lambda :calculate()).grid(row=6,columnspan=6,sticky=N+E+W+S)
p.mainloop()
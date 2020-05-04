from tkinter import *
from tkinter import messagebox
import math
f1=1
opr=""
def fun(num):
	num=str(num)
	if f1==1:
		number1L.configure(text=number1L.cget("text")+num)
	else:

		number2L.configure(text=number2L.cget("text")+num)

def clear():
	number1L.configure(text="")
	number2L.configure(text="")
	number3L.configure(text="")
def fun1(opt):
	global f1
	f1=1
	global opr
	if opt=='+' or opt=='-' or opt=='*' or opt=='/' or opt=="pow":
		f1=0
	opr=opt
def equal():
	global f1
	global res
	global opr
	if f1==0:

		a=int(number1L.cget("text"))
		b=int(number2L.cget("text"))

		if opr=='+':
			res=a+b
		elif opr=='-':
			res=a-b
		elif opr=='*':
			res=a*b	
		elif opr=='/':
			res=a/b
		elif opr=='pow':
			res=a**b
	else:
		a=int(number1L.cget("text"))
		if opr=='sin':
			a=math.radians(a)
			res=math.sin(a)
		elif opr=='cos':
			a=math.radians(a)
			res=math.cos(a)				
		elif opr=='tan':
			a=math.radians(a)
			res=math.tan(a)
		elif opr=='loge':
			a=math.radians(a)
			res=math.log(a)
		elif opr=='log10':
			res=math.log10(a)
		elif opr=='sqrt':
			res=math.sqrt(a)
		elif opr=='factorial':
			res=math.factorial(a)
	number3L.configure(text=res)
	f1=1					
				
				


root=Tk()

root.config(background="light green")
root.geometry('350x500')


root.title("CALCULATOR")
title=Label(root,text="CALCULATOR",bg="pink")
title.config(font=("curior",20))

no1L=Label(root,text="Enter no1 :",bg="light green")
no2L=Label(root,text="Enter no2:",bg="light green")
ansL=Label(root,text="Answer:",bg="light green")


number1L=Label(root,text="",bg="white")
number2L=Label(root,text="",bg="white")
number3L=Label(root,text="",bg="white")

title.grid(row=0,column=0,columnspan=5)


no1L.grid(row=1,column=0,columnspan=2)
no2L.grid(row=2,column=0,columnspan=2)
ansL.grid(row=3,column=0,columnspan=2)

number1L.grid(row=1,column=2,padx="10",ipadx="50",pady="10",columnspan=3)
number2L.grid(row=2,column=2,padx="10",ipadx="50",pady="10",columnspan=3)
number3L.grid(row=3,column=2,padx="10",ipadx="50",pady="10",columnspan=3)

Button(root,text="1",bg="light blue",command=lambda:fun(1)).grid(row=4,column=0,ipadx="10",ipady="10",pady="10",padx="10")
Button(root,text="2",bg="light blue",command=lambda:fun(2)).grid(row=4,column=1,ipadx="10",ipady="10",pady="10",padx="10")
Button(root,text="3",bg="light blue",command=lambda:fun(3)).grid(row=4,column=2,ipadx="10",ipady="10",pady="10",padx="10")
Button(root,text="+",bg="orange",command=lambda:fun1('+')).grid(row=4,column=3,ipadx="10",ipady="10",pady="10",padx="7")
Button(root,text="sin",bg="yellow",command=lambda:fun1('sin')).grid(row=4,column=4,ipadx="10",ipady="10",padx="2")

Button(root,text="4",bg="light blue",command=lambda:fun(4)).grid(row=5,column=0,ipadx="10",ipady="10",pady="10",padx="10")
Button(root,text="5",bg="light blue",command=lambda:fun(5)).grid(row=5,column=1,ipadx="10",ipady="10",pady="10",padx="10")
Button(root,text="6",bg="light blue",command=lambda:fun(6)).grid(row=5,column=2,ipadx="10",ipady="10",pady="10",padx="10")
Button(root,text="-",bg="orange",command=lambda:fun1('-')).grid(row=5,column=3,ipadx="10",ipady="10",pady="10",padx="7")
Button(root,text="cos",bg="yellow",command=lambda:fun1('cos')).grid(row=5,column=4,ipadx="10",ipady="10",padx="1")


Button(root,text="7",bg="light blue",command=lambda:fun(7)).grid(row=6,column=0,ipadx="10",ipady="10",pady="10",padx="10")
Button(root,text="8",bg="light blue",command=lambda:fun(8)).grid(row=6,column=1,ipadx="10",ipady="10",pady="10",padx="10")
Button(root,text="9",bg="light blue",command=lambda:fun(9)).grid(row=6,column=2,ipadx="10",ipady="10",pady="10",padx="10")
Button(root,text="*",bg="orange",command=lambda:fun1('*')).grid(row=6,column=3,ipadx="10",ipady="10",pady="10",padx="7")
Button(root,text="tan",bg="yellow",command=lambda:fun1('tan')).grid(row=6,column=4,ipadx="10",ipady="10",padx="1")

Button(root,text="c",bg="orange",command=lambda:clear()).grid(row=7,column=0,ipadx="10",ipady="10",pady="10",padx="10")
Button(root,text="0",bg="light blue",command=lambda:fun(0)).grid(row=7,column=1,ipadx="10",ipady="10",pady="10",padx="10")
Button(root,text="=",bg="orange",command=lambda:equal()).grid(row=7,column=2,ipadx="10",ipady="10",pady="10",padx="10")
Button(root,text="/",bg="orange",command=lambda:fun1('/')).grid(row=7,column=3,ipadx="10",ipady="10",pady="10",padx="7")
Button(root,text="pow",bg="yellow",command=lambda:cal('**')).grid(row=7,column=4,ipadx="10",ipady="10",padx="1")

Button(root,text="sqrt",bg="yellow",command=lambda:fun1('sqrt')).grid(row=8,column=0,ipadx="2",ipady="10",padx="10")
Button(root,text="loge",bg="yellow",command=lambda:fun1('loge')).grid(row=8,column=1,ipadx="2",ipady="10",padx="10")
Button(root,text="log10",bg="yellow",command=lambda:fun1('log10')).grid(row=8,column=2,ipadx="2",ipady="10",padx="10")
Button(root,text="factorial",bg="yellow",command=lambda:fun1('factorial')).grid(row=8,column=3,ipadx="2",ipady="10",pady="10",padx="7")
Button(root,text="close",bg="red",command=root.destroy).grid(row=8,column=4,ipadx="2",ipady="10",padx="1")


root.mainloop()
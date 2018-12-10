#praveen kumar
#Indian institute of information technology kalyani W.B
from tkinter import *

def btnclick(numbers):
        global operator
        operator=operator+str(numbers)
        text_Input.set(operator)
        
def btnclear():
        global operator
        operator=""
        text_Input.set("")


def equalbtn():
        global operator
        sumup=str(eval(operator))
        text_Input.set(sumup)
        operator=""




cal=Tk()
cal.title('Calculator')
operator=""
text_Input=StringVar()
# for Display where number would be entere
#textvariable is used as what is we gonna enter there
#command is used for writing function

txtDisplay=Entry(cal,font=('arial',20,'bold'),textvariable=text_Input,
                 bd=30,insertwidth=4,bg='powder blue',justify='right').grid(columnspan=4)
#button is created in first row
btn7=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
            text="7",bg='powder blue',command=lambda:btnclick(7)).grid(row=1,column=0)
btn8=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
            text="8",bg='powder blue',command=lambda:btnclick(8)).grid(row=1,column=1)
btn9=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
            text="9",bg='powder blue',command=lambda:btnclick(9)).grid(row=1,column=2)
Addition=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
            text="+",bg='powder blue',command=lambda:btnclick('+')).grid(row=1,column=3)
#button is created in second row
btn4=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
            text="4",bg='powder blue',command=lambda:btnclick(4)).grid(row=2,column=0)
btn5=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
            text="5",bg='powder blue',command=lambda:btnclick(5)).grid(row=2,column=1)
btn6=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
            text="6",bg='powder blue',command=lambda:btnclick(6)).grid(row=2,column=2)
Substraction=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
            text="-",bg='powder blue',command=lambda:btnclick('-')).grid(row=2,column=3)
#button is created in third row
btn1=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
            text="1",bg='powder blue',command=lambda:btnclick(1)).grid(row=3,column=0)
btn2=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
            text="2",bg='powder blue',command=lambda:btnclick(2)).grid(row=3,column=1)
btn3=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
            text="3",bg='powder blue',command=lambda:btnclick(3)).grid(row=3,column=2)
Multiplication=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
            text="*",bg='powder blue',command=lambda:btnclick('*')).grid(row=3,column=3)
#button is created in fourth row
btn0=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
            text="0",bg='powder blue',command=lambda:btnclick(0)).grid(row=4,column=0)
btnclear=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
            text="c",bg='powder blue',command=btnclear).grid(row=4,column=1)
btnequals=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
            text="=",bg='powder blue',command=equalbtn).grid(row=4,column=2)
Division=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
            text="/",bg='powder blue',command=lambda:btnclick('/')).grid(row=4,column=3)


cal.mainloop()

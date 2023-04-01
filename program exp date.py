##โปรแกรมคำนวนวันหมดอายุวัคซีน

from tkinter import *
from datetime import date
from datetime import timedelta

root = Tk()
root.title('Program Exp Date')
root.geometry('550x400')
root.option_add("*Font","consolas 12")

LH = Label(text = 'โปรแกรมกำหนดวันหมดอายุวัคซีน',fg = 'brown',font =40)
LH.grid(row=0,column=0)
           
##ใส่ตัวเลขปี คศ
Ly = Label(text = 'year',fg='blue' )
Ly.grid(row=1 , column=0,sticky=E,pady=5)
Ey = Entry(root,width=12, fg = 'blue')
Ey.grid(row=1 , column =1)

##ใส่ตัวเลขเดือน
Lm = Label(text = 'month',fg='green' )
Lm.grid(row=2 , column=0,sticky=E,pady=5)
Em = Entry(root,width=12, fg = 'blue')
Em.grid(row=2 , column =1)

##ใส่ตัวเลขวันที่
Ld = Label(text = 'day' ,fg='orange') 
Ld.grid(row=3 , column=0,sticky=E,pady=5)
Ed = Entry(root,width=12, fg = 'blue')
Ed.grid(row=3 , column =1)


##แปลงค่าเป็นวันที่
E1= Entry(root)
E1.grid(row=4 , column =1,pady=5)
def C1():
    Edate = date(int(Ey.get()),int(Em.get()),int(Ed.get()))
    Edate1 = Edate.strftime("%d-%b-%Y")
    E1.insert(0,Edate1)
    
B1 = Button(root, text = 'Date Receive' , bg= 'DarkOliveGreen2',fg = 'black',command = C1)
B1.grid( row=4 , column =0,pady=5)

##กำหนดวันหมดอายุ โดยบวกเพิ่มอีก31วัน โดยนับวันที่รับเป็นวันที่1
E2= Entry(root)
E2.grid(row=5 , column =1,pady=5)

def C2():
    EPZdate = date(int(Ey.get()),int(Em.get()),int(Ed.get()))
    E70= timedelta(days=30)
    E701 = EPZdate.__add__(E70)
    E702 = E701.strftime("%d-%b-%Y")
    E2.insert(0,E702)
    
B2 = Button(root, text = 'Exp.Date Pfizerม่วง(31)' , bg='medium orchid',fg = 'black',command = C2)
B2.grid( row=5 , column =0,pady=5)

##กำหนดวันหมดอายุ โดยบวกเพิ่มอีก70วัน โดยนับวันที่รับเป็นวันที่1
E3= Entry(root)
E3.grid(row=6 , column =1,pady=5)
    
def C3():
    EPZdate1 = date(int(Ey.get()),int(Em.get()),int(Ed.get()))
    E70a= timedelta(days=69)
    E701a = EPZdate1.__add__(E70a)
    E702a = E701a.strftime("%d-%b-%Y")
    E3.insert(0,E702a)
    

B3 = Button(root, text = 'Exp.Date Pfizerส้มหรือแดง(70)' , bg='Coral1',fg = 'black',command = C3)
B3.grid( row=6 , column =0,pady=5)

## ล้างข้อมูล
def Reset():
    Ey.delete(0,END)
    Em.delete(0,END)
    Ed.delete(0,END)
    E1.delete(0,END)
    E2.delete(0,END)
    E3.delete(0,END)
    Ey.focus()
    Ey.icursor(0)
        
B4 = Button(root, text = 'RESET' , bg= 'pink',fg = 'black',command = Reset)
B4.place(x=200,y=300)


##ออกจากโปรแกรม                  
def Exit():
    root.destroy()
            
B5 = Button(root, text = 'EXIT' , bg= 'sky blue',fg = 'black',command = Exit)
B5.place(x=400,y=300)




root.mainloop()


from tkinter import*
from tkinter import ttk
from tkinter import messagebox

import csv

def writecsv(datalist):
    with open('temp_record.csv','a',encoding='utf-8',newline='') as file:
        fw = csv.writer(file) 
        fw.writerow(datalist) 

GUI = Tk()
GUI.title('Program Record Temperature')
GUI.geometry('800x300')

Font1 = ('THSARABUN PSK',16)
Font2 = ('THSARABUN PSK',20,'bold' )

LF1 = ttk.LabelFrame(GUI,text = 'โปรแกรมบันทึกอุณหภูมิตู้เย็น')
LF1.place(x=200,y=50)


v_temp = StringVar()
L1= ttk.Label(GUI,text ='temp (c)')
L1.place(x=100,y=80)
E1 = ttk.Entry(LF1,textvariable = v_temp,font=Font1 )
E1.pack(pady=10,padx=10)

v_name = StringVar()
L2= ttk.Label(GUI,text ='ผู้บันทึก')
L2.place(x=100,y=130)
E2 = ttk.Entry(LF1,textvariable = v_name,font=Font1 )
E2.pack(pady=10,padx=10)

from datetime import datetime

def SaveData():
    t = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    temp = v_temp.get()
    name = v_name.get()
    text = [t,temp,name]
    writecsv(text)
    v_temp.set('')
    v_name.set('')

    

B1 = ttk.Button(LF1,text = 'บันทึก',command = SaveData)
B1.pack(ipadx=20,ipady=20)





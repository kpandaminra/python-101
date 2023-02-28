from tkinter import*
from tkinter import ttk
from tkinter import messagebox

GUI = Tk()
GUI.title('ทายนิสัยจากกรุ๊ปเลือด')
GUI.geometry('500x400')

L1 = Label(GUI,text='กดเลือกกรุ๊ปเลือดของคุณ',font=('TH SarabunPSK',20),fg='blue')
L1.place(x=50,y=10)
def Button1():
    text = 'กรุ๊ป A เป็นจำพวกอยู่ในกรอบ เข้าตามตรอกออกตามประตู รักกฎระเบียบ มีความอดทนสูง เก็บอารมณ์เก่ง และมักจะระวังตัวเป็นพิเศษ'
    messagebox.showinfo('ลักษณะนิสัย',text)
FB1 = Frame(GUI)
FB1.place(x=80,y=100)
B1 = ttk.Button(FB1,text='A',command=Button1)
B1.pack(ipadx=20,ipady=20)

def Button2():
    text = 'รักอิสระ บินไวมาไวอย่างกับ AirAsia มีความสร้างสรรค์สูง ไม่ชอบอยู่ในกรอบ ทำให้เป็นคนที่ไม่ค่อยยึดติด อยากทำอะไรก็ทำ อยากพูดอะไรก็พูด ส่วนใหญ่มองโลกในแง่ดี และหลงใหลในสิ่งที่ตัวเองสนใจเท่านั้น ถ้าไม่สนใจ สิ่งนั้นจะเป็นอากาศธาตุไปเลย จึงส่งผลเสียทำให้ไม่รับรู้สิ่งรอบๆ ข้างสักเท่าไรนัก'
    messagebox.showinfo('ลักษณะนิสัย',text)
FB2 = Frame(GUI)
FB2.place(x=150,y=100)
B2 = ttk.Button(FB2,text='B',command=Button2)
B2.pack(ipadx=20,ipady=20)

def Button3():
    text = 'คนกรุ๊ป AB เกิดมาเพื่อเป็นนักพูด และมักจะพูดจาได้ฉะฉานตรงไปตรงมา บางครั้งพูดความจริงเสียจนอีกฝ่ายรับไม่ได้เหมือนกัน AB มีตรรกะและการวิเคราะห์ไม่ค่อยเหมือนชาวบ้าน ทำให้คนไม่ค่อยจะเข้าใจ จึงอ่อนไหวง่าย แต่ถึงอย่างนั้นกรุ๊ป AB ก็ไม่ค่อยจะสนใจสักเท่าไร บางครั้งก็ออกแนวขี้เกียจ'
    messagebox.showinfo('ลักษณะนิสัย',text)
FB3 = Frame(GUI)
FB3.place(x=240,y=100)
B3 = ttk.Button(FB3,text='AB',command=Button3)
B3.pack(ipadx=20,ipady=20)

def Button4():
    text = '“ทะยานสู่เป้าหมาย ผลลัพธ์มีแค่ชัยชนะ” คงเป็นประโยคที่เหมาะสมกับคนกรุ๊ป O มากที่สุด แบรนด์ที่เข้ากับคนกรุ๊ปนี้ได้ดี คงหนีไม่พ้น Nike ที่เป็นเทพสัญลักษณ์แห่งชัยชนะ เพราะเป็นคนที่ทะเยอทะยาน มีเป้าหมายชัดเจน เมื่อคอมโบกับความเก่งและฉลาดที่มีอยู่ในตัว ทำให้เป็นคนที่ไม่โลเล และประสบความสำเร็จได้รวดเร็วกว่ากรุ๊ปอื่นๆ'
    messagebox.showinfo('ลักษณะนิสัย',text)
FB4 = Frame(GUI)
FB4.place(x=320,y=100)
B4 = ttk.Button(FB4,text='O',command=Button4)
B4.pack(ipadx=20,ipady=20)

###


GUI.mainloop()

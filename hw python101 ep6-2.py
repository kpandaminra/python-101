class Greenteaonly:
    def __init__(self, name,size,price):
        self.name = name
        self.size = size
        self.price = price
    def show(self):
        print(f'เมนูชาเขียว')
        
class Levelsugar(Greenteaonly):
    def __init__(self,name,size,price,sugar):
        super().__init__(name,size,price)
        self.sugar = sugar
    def checksweet(self):
        if self.sugar >= 75:
            print(f'{self.name} แก้วนี้ หวานมาก')   
        elif self.sugar >= 50:
            print(f'{self.name} แก้วนี้ หวานปกติ')
        
        elif self.sugar >= 25:
            print(f'{self.name} แก้วนี้ หวานน้อย')
        else:
            print(f'{self.name} แก้วนี้ ไม่หวาน')

class Receipt(Levelsugar):
    def __init__(self,name,size,price,sugar,glass):
        super().__init__(name,size,price,sugar)
        self.glass = glass
        
    def sale(self):
        i = self.glass*self.price
        print (f'ยอดรวมราคา :{i} บาท')

    def thank(self):
        print (f'**ขอบคุณที่มาใช้บริการ**')

      
         
Rec1= Receipt('Ice Greentea',500,50,50,2)
print('ร้าน greenteaonly')
Rec1.show()
print(f'ชื่อเมนู :{Rec1.name}')
print(f'ขนาด :{Rec1.size} ml')
print(f'ราคาแก้วละ :{Rec1.price} บาท')
print(f'ยอดซื้อจำนวน :{Rec1.glass} แก้ว')
Rec1.sale()
Rec1.checksweet()
Rec1.thank()
print('===============$$$===============')

Rec2= Receipt('Hot Greentea',200,40,20,3)
print('ร้าน greenteaonly')
Rec2.show()
print(f'ชื่อเมนู :{Rec2.name}')
print(f'ขนาด :{Rec2.size} ml')
print(f'ราคาแก้วละ :{Rec2.price} บาท')
print(f'ยอดซื้อจำนวน :{Rec2.glass} แก้ว')
Rec2.sale()
Rec2.checksweet()
Rec2.thank()
print('===============$$$===============')
Rec3= Receipt('Ice Greentea',500,50,35,4)
print('ร้าน greenteaonly')
Rec3.show()
print(f'ชื่อเมนู :{Rec3.name}')
print(f'ขนาด :{Rec3.size} ml')
print(f'ราคาแก้วละ :{Rec3.price} บาท')
print(f'ยอดซื้อจำนวน :{Rec3.glass} แก้ว')
Rec3.sale()
Rec3.checksweet()
Rec3.thank()



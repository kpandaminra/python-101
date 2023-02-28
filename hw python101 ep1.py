 import turtle

>>> screen=turtle.Screen()
>>> screen.title('Homework For Python 101  EP.1 Class')
>>> 
>>> screen.bgcolor('grey')
>>> 
>>> t=turtle.Turtle()
>>> t.shape('turtle')
>>> t.color('blue')
>>> t.penup()
>>> t.goto(-200,100)
>>> t.write('PYTHON 101',False,align='left',font=('Arial',50,'normal'))
>>> t.goto(-100,50)
>>> t.color('yellow')
>>> t.write('PYTHON 101',False,align='left',font=('Arial',50,'normal'))
>>> t.goto(200,50)
>>> t.color('black','pink')

#Imports#
import turtle
from Tkinter import *
import random
#Variables#
line = 1
#Functions#
def forward():
	turtle.forward(5)
def left():
	turtle.left(90)
def right():
	turtle.right(90)
def color():
	a = random.randint(1,6)
	if a == 1:
		turtle.color("Red")
	elif a == 2:
		turtle.color("Blue")
	elif a == 3:
		turtle.color("Green")
	elif a == 4:
		turtle.color("Purple")
	elif a == 5:
		turtle.color("Yellow")
	elif a == 6:
		turtle.color("Orange")
def line_on():
	turtle.down()
def line_off():
	turtle.up()

#GUI#
app = Tk()
app.title("Turtle Controller")
buttonforward = Button(app, text="Forward", command=forward)
buttonforward.pack(side= 'top')
buttonleft = Button(app, text="Left", command=left)
buttonleft.pack(side='left')
buttonright = Button(app, text="Right", command = right)
buttonright.pack(side = 'right')
label1 = Label(app, text = "Python Turtle Controller", height = 4)
label1.pack()
buttoncolor = Button(app, text= "Random Color", command = color)
buttoncolor.pack(side = 'bottom')
buttonline1 = Button(app, text = "Toggle Line On", command = line_on)
buttonline1.pack()
buttonline2 = Button(app, text = "Toggle Line Off", command = line_off)
buttonline2.pack()
app.mainloop()

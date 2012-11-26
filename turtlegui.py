#Imports#

import turtle
from Tkinter import *
import random
import webbrowser

#Variables#

line = 1
#Functions#
def forward():
	turtle.forward(10)
def left():
	turtle.left(90)
def right():
	turtle.right(90)
def color():
	a = random.randint(1,7)
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
	elif a == 7:
		turtle.color("Black")
def line_on():
	turtle.down()
def line_off():
	turtle.up()
def quit():
	exit()
def help():
	webbrowser.open("https://sites.google.com/site/turtlecontrollergui/home")
def interact():
	code = raw_input("Turtle Command: ")
	if code == "circle":
		value = float(raw_input("Select Value: "))
		turtle.circle(value)
	elif code == "color":
		value = raw_input("Select Value: ")
		turtle.color(value)
	elif code == "line":
		value = raw_input("Select Value: ")
		if value == "off":
			turtle.up()
		elif value == "on":
			turtle.down()
	elif code == "forward":
		value = float(raw_input("Select Value: "))
		turtle.forward(value)
	elif code == "backward":
		value = float(raw_input("Select Value: "))
		turtle.backward(value)
	elif code == "right":
		value = float(raw_input("Select Value: "))
		turtle.right(value)
	elif code == "left":
		value = float(raw_input("Select Value: "))
		turtle.left(value)
	elif code == "speed":
		value = float(raw_input("Select Value: "))
		turtle.speed(value)
	elif code == "origin":
		turtle.home()
	elif code == "undo":
		turtle.undo()
	elif code == "quit":
		exit()
	elif code == "clear":
		turtle.clear()
	else:
		print "Unknown command."

#GUI#

turtle.forward(0)
app = Tk()
app.title("Turtle Controller")
app.geometry("300x300")
buttonforward = Button(app, text="Forward", command=forward)
buttonforward.pack(side= 'top')
buttonleft = Button(app, text="Left", command=left)
buttonleft.pack(side='left')
buttonright = Button(app, text="Right", command = right)
buttonright.pack(side = 'right')
helpbutton = Button(app, text = "Help", command = help)
helpbutton.pack(side = 'bottom')
quitbutton = Button(app, text = "Quit", command = quit)
quitbutton.pack(side = 'bottom')
labelspace = Label(app)
labelspace.pack(side = 'bottom')
buttoncolor = Button(app, text= "Random Color", command = color)
buttoncolor.pack(side = 'bottom')
buttonline1 = Button(app, text = "Toggle Line On", command = line_on)
buttonline1.pack(side = 'bottom')
buttonline2 = Button(app, text = "Toggle Line Off", command = line_off)
buttonline2.pack(side = 'bottom')
while 1==1:
	interact()
app.mainloop()
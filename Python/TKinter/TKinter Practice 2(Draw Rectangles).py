#Title: Tkinter practice
#Author: jack hawinkels
#Description: Practice for the TKinter module
#Created: 13/02/2020
#Modified: 18/02/2020
#Version: 1

#***IMPORTS***
from tkinter import *
from tkinter.messagebox import showerror, showwarning
import random
import time
#---IMPORTS---

#***CLASSES***

#---CLASSES---

#***DEFINITIONS***
def quit():
    window.destroy()

def hello():
    canvas.create_text(50, 20, text="hello top left")
    canvas.create_text(400, 250, text="hello\nlower right")
    canvas.update()

def mousedown(event):
    global startx
    global starty
    startx = event.x
    starty = event.y

def draw(event):
    global colour
    
    endx = event.x
    endy = event.y
    canvas.create_rectangle(startx, starty, endx, endy, fill=colour, outline="blue", width=5)
    canvas.update()

def clear():
    canvas.delete(ALL)

class shape:
    class fillcolour:
        def red():
            global colour
            colour = "red"
        def orange():
            global colour
            colour = "orange"
        def yellow():
            global colour
            colour = "yellow"
        def green():
            global colour
            colour = "green"
        def blue():
            global colour
            colour = "blue"

    class draw_shape:
        def rectangle():
            global shape_type
            shape_type = "rectangle"
        def circle():
            global shape_type
            shape_type = "circle"

def main():
    global window
    global tkniter
    global canvas
    
    window = Tk()
    left = Frame(window)
    left.pack(side=LEFT)
    top = Frame(window)
    top.pack(side=TOP)
    window.title("Random Rectangles")
    Button(window, text="Quit", width=8, command=quit).pack(in_=top, side=LEFT)
    Button(window, text="Clear", width=8, command=clear).pack(in_=top, side=LEFT)
    Button(window, text="Rectangle", width=8, command=clear).pack(in_=top, side=LEFT)
    Button(window, text="Circle", width=8, command=clear).pack(in_=top, side=LEFT)
    Button(window, bg="red", width=2, command=shape.fillcolour.red).pack(in_=left,side=TOP)
    Button(window, bg="orange", width=2, command=shape.fillcolour.orange).pack(in_=left,side=TOP)
    Button(window, bg="yellow", width=2, command=shape.fillcolour.yellow).pack(in_=left,side=TOP)
    Button(window, bg="green", width=2, command=shape.fillcolour.green).pack(in_=left,side=TOP)
    Button(window, bg="blue", width=2, command=shape.fillcolour.blue).pack(in_=left,side=TOP)


    canvas = Canvas(window, width=500, height=400, bg="yellow")
    canvas.bind("<Button-1>", mousedown)
    canvas.bind("<ButtonRelease-1>", draw)
    canvas.pack()
    window.mainloop()
#---DEFINITIONS---

#***GLOBAL VARIABLES***
colour = "green"
shape_type = "rectangle"
#---GLOBAL VARIABLES---

#***MAIN STUFF***
main()
#---MAIN STUFF---

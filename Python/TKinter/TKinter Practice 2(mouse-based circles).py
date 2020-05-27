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

def randomcircle(event):
    global colour
    
    xval = event.x - 15
    yval = event.y - 15
    canvas.create_oval(xval, yval, xval+30, yval+30, fill=colour, outline="blue", width=5)
    canvas.update()

def randomsquare(event):
    global colour
    
    xval = event.x - 15
    yval = event.y - 15
    canvas.create_rectangle(xval, yval, xval+30, yval+30, fill=colour, outline="blue", width=5)
    canvas.update()

def clear():
    canvas.delete(ALL)

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

def main():
    global window
    global tkniter
    global canvas
    
    window = Tk()
    left = Frame(window)
    left.pack(side=LEFT)
    window.title("Random Circles")
    Button(window, text="Quit", width=8, command=quit).pack()
    Button(window, text="Clear", width=8, command=clear).pack()
    Button(window, text="Draw A Circle", width=8, command=randomcircle).pack()
    Button(window, bg="red", width=2, command=fillcolour.red).pack(in_=left,side=TOP)
    Button(window, bg="orange", width=2, command=fillcolour.orange).pack(in_=left,side=TOP)
    Button(window, bg="yellow", width=2, command=fillcolour.yellow).pack(in_=left,side=TOP)
    Button(window, bg="green", width=2, command=fillcolour.green).pack(in_=left,side=TOP)
    Button(window, bg="blue", width=2, command=fillcolour.blue).pack(in_=left,side=TOP)


    canvas = Canvas(window, width=500, height=400, bg="yellow")
    canvas.bind("<Button-1>", randomcircle)
    canvas.bind("<ButtonRelease-1>", randomsquare)
    canvas.pack()
    window.mainloop()
#---DEFINITIONS---

#***GLOBAL VARIABLES***
colour = "green"
#---GLOBAL VARIABLES---

#***MAIN STUFF***
main()
#---MAIN STUFF---

#Title: Tkinter practice
#Author: jack hawinkels
#Description: Practice for the TKinter module
#Created: 13/02/2020
#Modified: 18/02/2020
#Version: 1

#***IMPORTS***
from tkinter import *
from tkinter.messagebox import showerror, showwarning
#---IMPORTS---

#***CLASSES***

#---CLASSES---

#***DEFINITIONS***
def quit():
    root.destroy()

def hello():
    canvas.create_text(50, 20, text="hello top left")
    canvas.create_text(400, 250, text="hello\nlower right")
    canvas.update()

def redcircle():
    duck = 10
    rabbit = 10
    canvas.create_oval(duck, rabbit, duck+20, rabbit+20, fill="red", outline="blue", width=5)
    canvas.update()

def main():
    global root
    global tkniter
    global canvas
    root = Tk()
    root.title("This is the title of the window")
    Button(root, text="Quit", width=8, command=quit).pack()
    Button(root, text="Hello", width=8, command=hello).pack()
    Button(root, text="Red Circle", width=8, command=redcircle).pack()
    canvas = Canvas(root, width=450, height=300, bg="white")
    canvas.pack()
    root.mainloop()
#---DEFINITIONS---

#***GLOBAL VARIABLES***

#---GLOBAL VARIABLES---

#***MAIN STUFF***
main()
#---MAIN STUFF---

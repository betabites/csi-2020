#Title: The follower mouse
#Description: An interactable on-screen mouse
#Author: Jack hawinkels
#Created: 26/02/2020
#Modified: 26/02/2020
#Version: 1

#***IMPORTS***
from tkinter import *
import time
import math
#---IMPORTS---

#***DEFINITIONS***
def setup_window():
    global window
    global mouse
    global canvas
    global movement_loops_started

    movement_loops_started = 0

    window = Tk()
    window.title("Follow me mouse")
    Button(window, width=29, height=3, text="quit").pack()

    canvas = Canvas(window, width=290, height=350, bg="beige")
    canvas.pack()

    #Setup the mouse
    mouse = {
        "position" : {
            "x" : 0,
            "y": 0
        },
        "design" : {
            "fill" : "red",
            "outline" : {
                "color" : "black",
                "width" : 5
            }
        }
    }
    canvas.create_oval(mouse['position']['x'], mouse['position']['y'], mouse['position']['x']+10, mouse['position']['y']+10, fill=mouse['design']['fill'], outline=mouse['design']['outline']['color'], width=mouse['design']['outline']['width'])

    canvas.bind("<Button-1>", update_mouse)

def update_mouse(event):
    global mouse
    global canvas
    global movement_loops_started

    movement_loops_started += 1
    loop_id = movement_loops_started
    
    x_pixels_to_move = event.x - mouse['position']['x']
    y_pixels_to_move = event.y - mouse['position']['y']
    if x_pixels_to_move < 0:
        #The mouse needs to move backwards
        x_pixels_to_move = x_pixels_to_move - (x_pixels_to_move * 2)
        backwards = True
    else:
        backwards = False
    y_per_x = y_pixels_to_move / x_pixels_to_move
    
    for i in range(x_pixels_to_move):
        canvas.delete(ALL)
        time.sleep(0.01)
        print("MOVED! x:{}, y:{}".format(mouse['position']['x'], mouse['position']['y']))
        if backwards:
            mouse['position']['x'] -= 1
        else:
            mouse['position']['x'] += 1
        mouse['position']['y'] += y_per_x
        canvas.create_oval(mouse['position']['x'], mouse['position']['y'], mouse['position']['x']+10, mouse['position']['y']+10, fill=mouse['design']['fill'], outline=mouse['design']['outline']['color'], width=mouse['design']['outline']['width'])
        canvas.update()
        if movement_loops_started != loop_id:
            #Another loop has been started, so stop this one
            break

        
#---DEFINITIONS---

setup_window()

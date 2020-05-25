#Title: Ping Pong
#Description: A python game of Pong!
#Author: Jack hawinkels
#Created: 26/02/2020
#Modified: 26/02/2020
#Version: 1

#***IMPORTS***
from tkinter import *
import time
import math
import random
#---IMPORTS---

#***DEFINITIONS***
def setup_window():
    global window
    global mouse
    global canvas
    global movement_loops_started
    global orientation
    global rectangles

    movement_loops_started = 0
    orientation = random.randint(70, 110)
    last_hit = ""

    window = Tk()
    window.title("Ping Pong!")
    Button(window, width=29, height=3, text="quit", command=quit).pack()

    canvas = Canvas(window, width=290, height=350, bg="beige")
    window.bind("<Up>", left_up)
    window.bind("<Down>", left_down)
    window.bind("w", right_up)
    window.bind("s", right_down)
    window.bind("<KeyRelease>", key_release)
    window.bind("<Return>", right_cheat)
    canvas.pack()

    #Setup the mouse
    mouse = {
        "position" : {
            "x" : 145,
            "y": 50
        },
        "design" : {
            "fill" : "red",
            "outline" : {
                "color" : "black",
                "width" : 5
            }
        },
        "speed" : 20
    }
    canvas.create_oval(mouse['position']['x'], mouse['position']['y'], mouse['position']['x']+10, mouse['position']['y']+10, fill=mouse['design']['fill'], outline=mouse['design']['outline']['color'], width=mouse['design']['outline']['width'])

    rectangles = {
        "left" : {
            "y" : 50,
            "speed" : 10,
            "hits" : 0,
        },
        "right" : {
            "y" : 50,
            "speed" : 20,
            "hits" : 0,
        }
    }

    canvas.bind("<Button-1>", update_mouse)

    #Start moving the mouse
    a = 21 + (1/3)
    b = -32
    c = 10 + (2/3)
    d = math_E(3.35, -13)


    canvas.create_text(50, 50, text="Ready?")
    canvas.update()
    time.sleep(5)
    canvas.delete(ALL)
    while True:
        #orientation = (int(input()))
        travel_x, travel_y = calc_direction(orientation)

        mouse['position']['x'] = mouse['position']['x'] + (travel_x / (100 - (mouse['speed'] * 2)))
        mouse['position']['y'] = mouse['position']['y'] + (travel_y / (100 - (mouse['speed'] * 2)))

        #time.sleep(0.002)
        #print("{} {} {}".format(orientation, travel_x, travel_y))

        #Process block movements
        if keyboard_keys["UP"] == True:
            rectangles['left']['y'] -= rectangles['left']['speed'] / 100000
            rectangles['left']['speed'] += 0.1
        elif keyboard_keys["DOWN"] == True:
            rectangles['left']['y'] += rectangles['left']['speed'] / 100000
            rectangles['left']['speed'] += 0.1

        if keyboard_keys["W"] == True:
            rectangles['right']['y'] -= rectangles['right']['speed'] / 100000
            rectangles['right']['speed'] += 0.1
        elif keyboard_keys["S"] == True:
            rectangles['right']['y'] += rectangles['right']['speed'] / 100000
            rectangles['right']['speed'] += 0.1


        canvas.delete(ALL)
        canvas.create_oval(mouse['position']['x'], mouse['position']['y'], mouse['position']['x']+10, mouse['position']['y']+10, fill=mouse['design']['fill'], outline=mouse['design']['outline']['color'], width=mouse['design']['outline']['width'])
        canvas.create_rectangle(0, rectangles['left']['y'], 20, rectangles['left']['y']+50, fill='black')
        canvas.create_rectangle(270, rectangles['right']['y'], 290, rectangles['right']['y']+50, fill='black')
        canvas.create_text(10, rectangles['left']['y']+20, fill='white', text=str(rectangles['left']['hits']))
        canvas.create_text(280, rectangles['right']['y']+20, fill='white', text=str(rectangles['right']['hits']))
        canvas.update()

        mouse['speed'] += 0.0001
        if mouse['position']['y'] <= 0 or mouse['position']['x'] <= 0 or mouse['position']['y'] >= 350 or mouse['position']['x'] >= 280:
            orientation += 45
            if orientation >= 360:
                orientation -= 360


            #time.sleep(1)
            #print(mouse['position'])
            #print(orientation)
        elif mouse['position']['y'] >= rectangles['left']['y']-10 and mouse['position']['y'] <= (rectangles['left']['y'] + 50) and mouse['position']['x'] < 20:
            #bumps left player
            orientation += random.randint(40, 50)
            if orientation >= 360:
                orientation -= 360

            if last_hit != "left":
                last_hit = "left"
                rectangles['left']['hits'] += 1
            #time.sleep(1)
            #print(mouse['position'])
            #print(orientation)
        elif mouse['position']['y'] >= rectangles['right']['y']-10 and mouse['position']['y'] <= (rectangles['right']['y'] + 50) and mouse['position']['x'] >= 260:
            #bumps right player
            orientation += random.randint(40, 50)
            if orientation >= 360:
                orientation -= 360

            if last_hit != "right":
                last_hit = "right"
                rectangles['right']['hits'] += 1
            #time.sleep(1)
            #print(mouse['position'])
            #print(orientation)


        if mouse['position']['x'] < 10:
            #canvas.delete(ALL)
            #rectangles['right']['y'], rectangles['left']['y'] = 50, 50
            canvas.delete(ALL)
            canvas.create_rectangle(0, rectangles['left']['y'], 20, rectangles['left']['y']+50, fill='black')
            canvas.create_rectangle(270, rectangles['right']['y'], 290, rectangles['right']['y']+50, fill='red')
            for i in range(270):
                time.sleep(0.01)
                canvas.create_rectangle((270 - i), rectangles['right']['y'], 290, rectangles['right']['y']+50, fill='red')
                canvas.update()
            canvas.create_text(75, 75, text="Right player wins!", fill="white")

            break
            
        elif mouse['position']['x'] > 280:
            #rectangles['right']['y'], rectangles['left']['y'] = 50, 50
            canvas.delete(ALL)
            canvas.create_rectangle(0, rectangles['left']['y'], 20, rectangles['left']['y']+50, fill='red')
            canvas.create_rectangle(270, rectangles['right']['y'], 290, rectangles['right']['y']+50, fill='black')

            for i in range(270):
                time.sleep(0.01)
                canvas.create_rectangle(0, rectangles['left']['y'], (i + 20), rectangles['left']['y']+50, fill='red')
                canvas.update()
            canvas.create_text(75, 75, text="Left player wins!", fill="white")

            break

def math_E(number, adjustment):
    return number * (10**adjustment)

def update_mouse(event):
    global orientation
    global mouse
    mouse['speed'] += 1
    print("Speed is now: {}".format(mouse['speed']))
    orientation += random.randint(0, 45)
    if orientation >= 360:
        orientation -= 360

def calc_direction(orientation):
    #calculate x_travel
    if (orientation <= 90):
        travel_x = orientation / 90
    elif (orientation > 270):
        travel_x = 0 - ((360 - orientation) / 90)
    else:
        travel_x = 1 - ((orientation - 90) / 90)

    #calculate y_travel
    if (orientation <= 180):
        travel_y = 1 - (orientation / 90)
    else:
        travel_y = -1 + ((orientation - 180) / 90)

    #invert travel_y
    travel_y = travel_y - (travel_y * 2)

    return travel_x, travel_y

def left_up(event):
    global keyboard_keys
    keyboard_keys["UP"] = True

def left_down(event):
    global keyboard_keys
    keyboard_keys["DOWN"] = True

def right_up(event):
    global keyboard_keys
    keyboard_keys["W"] = True

def right_down(event):
    global keyboard_keys
    keyboard_keys["S"] = True

def key_release(event):
    global keyboard_keys
    global rectangles
    if event.keysym == "Up":
        keyboard_keys["UP"] = False
    elif event.keysym == "Down":
        keyboard_keys["DOWN"] = False
    elif event.keysym == "w":
        keyboard_keys["W"] = False
    elif event.keysym == "s":
        keyboard_keys["S"] = False

def quit():
    global window
    window.destroy()

def right_cheat(event):
    global rectangles
    global mouse
    rectangles['right']['y'] = mouse['position']['y']
#---DEFINITIONS---

keyboard_keys = {
    "UP" : False,
    "DOWN" : False,
    "W" : False,
    "S" : False
}

setup_window()

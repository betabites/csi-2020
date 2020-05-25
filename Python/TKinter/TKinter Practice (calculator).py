#Title: The Calculator
#Author: Jack Hawinkels
#Created: 19/02/2020
#Modified: 19/02/2020
#Version: 1

#***IMPORTS***
from tkinter import *
import math
#---IMPORTS---

#***DEFINITIONS***
def quit():
    window.destroy()

def display():
    global calcvalue
    calcvalue = 0

def main():
    global window
    global tkiniter
    global canvas
    global buttons_detailed
    global buttons
    
    window = Tk()
    window.title("Simple Calculator")
    Button(window, text="Quit", width=5, command=quit).pack()
    
    canvas = Canvas(window, width=290, height=350, bg="beige")
    canvas.pack()

    #Setup the display
    global calcvalue
    canvas.create_rectangle(10, 10, 280, 40, fill="white", outline="black")
    canvas.create_text(145, 25, text="0", font="Times 20 bold")

    #Add the numbers

##    #***FIRST ROW***
##    canvas.create_rectangle(10, 50, 70, 110, fill="yellow", outline="black")
##    canvas.create_text(40, 80, text="7", font="Times 30 bold")
##
##    canvas.create_rectangle(80, 50, 140, 110, fill="yellow", outline="black")
##    canvas.create_text(110, 80, text="8", font="Times 30 bold")
##
##    canvas.create_rectangle(150, 50, 210, 110, fill="yellow", outline="black")
##    canvas.create_text(180, 80, text="9", font="Times 30 bold")
##
##    canvas.create_rectangle(220, 50, 280, 110, fill="red", outline="black")
##    canvas.create_text(250, 80, text="/", font="Times 30 bold")
##    #---FIRST ROW---
    
##    #***SECOND ROW***
##    canvas.create_rectangle(10, 120, 70, 180, fill="yellow", outline="black")
##    canvas.create_text(40, 150, text="7", font="Times 30 bold")
##
##    canvas.create_rectangle(80, 120, 140, 180, fill="yellow", outline="black")
##    canvas.create_text(110, 150, text="8", font="Times 30 bold")
##
##    canvas.create_rectangle(150, 120, 210, 180, fill="yellow", outline="black")
##    canvas.create_text(180, 150, text="9", font="Times 30 bold")
##
##    canvas.create_rectangle(220, 120, 280, 180, fill="red", outline="black")
##    canvas.create_text(250, 150, text="/", font="Times 30 bold")
##    #---SECOND ROW---
    
    button_rows = [
            [
                ["yellow", "7", 1],
                ["yellow", "8", 1],
                ["yellow", "9", 1],
                ["red", "/", 1]
            ],
            [
                ["yellow", "4", 1],
                ["yellow", "5", 1],
                ["yellow", "6", 1],
                ["red", "*", 1]
            ],
            [
                ["yellow", "1", 1],
                ["yellow", "2", 1],
                ["yellow", "3", 1],
                ["red", "-", 1]
            ],
            [
                ["yellow", "0", 1],
                ["green", "=", 2],
                ["red", "+", 1]
            ]
        ]

    y = 50
    buttons_detailed = {}
    for row in button_rows:
        x = 10
        print(row)
        for button in row:
            x_travel = 70 * button[2] - 10
            text_x_travel = 35 * button[2] - 5
            
            colour = button[0]
            text = button[1]
            canvas.create_rectangle(x, y, x+x_travel, y+60, fill=colour, outline="black")
            canvas.create_text(x+text_x_travel, y+30, text=text, font="Times 30 bold")

            x_row = math.floor((x - 10) / 70) + 1
            y_row = math.floor(((y - 40) - 10) / 70) + 1
            for i in range(button[2]):
                buttons_detailed.update({"{}_{}".format(x_row, y_row) : {"text" : button[1], "colour" : button[0]}})

                x_row = x_row + 1

            x = x + x_travel + 10

        y = y + 70
    print(buttons_detailed)

    canvas.bind("<Button-1>", buttonclick)

def buttonclick(event):
    global future_movement
    global results
    global canvas
    global calculation
    
    try:
        print("CLICK!")
        x_row = math.floor((event.x - 10) / 70) + 1
        y_row = math.floor(((event.y - 40) - 10) / 70) + 1
        print(x_row)
        print(y_row)
        print(buttons_detailed["{}_{}".format(x_row, y_row)])
        button = buttons_detailed["{}_{}".format(x_row, y_row)]

        try:
            int_parsed = int(button['text'])
            if results == 0:
                results = int_parsed
            elif future_movement == "+":
                results = results + int_parsed
            elif future_movement == "-":
                results = results - int_parsed
            elif future_movement == "*":
                results = results * int_parsed
            elif future_movement == "/":
                results = results / int_parsed

            calculation = calculation + " " + str(int_parsed)
            print(results)

            canvas.create_rectangle(10, 10, 280, 40, fill="white", outline="black")
            canvas.create_text(145, 25, text=calculation, font="Times 20 bold")
    
        except:
            print("failed to parse {}.".format(button['text']))
            if button['text'] == "=":
                results_text = str(results)
                
                canvas.create_rectangle(10, 10, 280, 40, fill="white", outline="black")
                canvas.create_text(145, 25, text=results_text, font="Times 20 bold")

                results = 0
                calculation = ""
            else:
                future_movement = button['text']
                calculation = calculation + " " + button['text']

                canvas.create_rectangle(10, 10, 280, 40, fill="white", outline="black")
                canvas.create_text(145, 25, text=calculation, font="Times 20 bold")

    except:
        print("No button was clicked!")
#---DEFINITIONS---

#***MAIN STUFF***
results = 0
calculation = ""
main()

#---MAIN STUFF---

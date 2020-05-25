#Title: To infinity, and beyond
#Description: Asks the user questions. If the user does not respond fast enough, they lose
#Author: jack hawinkels
#Created: 10/03/2020
#Modified: 10/03/2020

#***IMPORTS***
from tkinter import *
from functools import partial
import random
import time
#---IMPORTS---

#***DEFINITIONS***
def window_main():
    global master
    global letters
    global question
    global question_string
    global current_letter_count
    global buttons
    global timer
    global level_input
    global time
    global score
    global start

    start = time.time()
    score = 0

    timer = 0.0
    letters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    current_letter_count = 2

    master = Tk()
    master.title("To infinity, and beyond!")
    timer = master.after(3000, end)
    question_string = "1"
    question = Label(master, text=question_string)
    question.grid(row=1, column = 1, columnspan=len(letters))

    buttons = []
    for i in range(current_letter_count):
        button_action = partial(button_click, letters[i])
        master.bind(letters[i].lower(), button_action)
        master.bind(letters[i], button_action)
        buttons.append(Button(master, text=letters[i], command=button_action))
        buttons[-1].grid(row=2, column=i)

    master.lift()

def button_click(letter, event=False):
    global question
    global question_string
    global current_letter_count
    global buttons
    global master
    global timer
    global score

    if letter != question_string:
        end()
    else:
        master.after_cancel(timer)
        score += 1
        timer = master.after(3000, end)
        if random.randint(0, 5) == 5 and current_letter_count != len(letters):
            current_letter_count += 1

        question.destroy()
        question_string = letters[random.randint(0, (current_letter_count - 1))]
        question = Label(master, text=question_string)
        question.grid(row=1, column = 1, columnspan=25)

        for button in buttons:
            button.destroy()

        buttons = []
        for i in range(current_letter_count):
            button_action = partial(button_click, letters[i])
            master.bind(letters[i].lower(), button_action)
            master.bind(letters[i], button_action)
            buttons.append(Button(master, text=letters[i], command=button_action))
            buttons[-1].grid(row=2, column=i)

def end():
    global master
    global start
    global score
    master.destroy()

    master = Tk()
    master.title("To infinity, and beyond!")
    Label(master, text="GAME OVER!").grid(row=1, column=1, columnspan=2)
    score_text = "Score: " + str(score)
    Label(master, text=score_text).grid(row=2, column=1)
    time_text = "Time: " + str(round(time.time() - start)) + "s"
    Label(master, text=time_text).grid(row=2, column=2)
    Button(master, text="Try Again", width=30, command=try_again).grid(row=3, column=1, columnspan=2)
    Button(master, text="Quit", width=30, command=quit).grid(row=4, column=1, columnspan=2)

    master.lift()

def quit():
    global master
    #master.destroy()

    button_click(question_string, False)

def try_again():
    global master
    master.destroy()

    window_main()
#---DEFINITIONS---

window_main()

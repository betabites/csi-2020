#Title: Off to space
#Description: A fun little flying game
#Author: Jack Hawinkels
#Created: 12/03/2020
#Modified: 12/03/2020

#***IMPORTS***
from tkinter import *
import random
import time
import os
import string
#---IMPORTS---

#***DEFINITIONS***
def username_get():
    global master
    global label_glitch_var
    global label
    global username_entry
    master = Tk()
    label = Label(master, text="Enter a username!")
    label.grid(row=1,column=1,columnspan=2)
    username_entry = Entry(master)
    username_entry.grid(row=2,column=1)
    submit_button = Button(text="Submit", command=start)
    submit_button.grid(row=2, column=2)

    label_glitch_var = master.after(random.randint(0, 3000), label_glitch)
    master.mainloop()

def label_glitch():
    global master
    global label
    global label_glitch_var
    global label_reset_timer

    #print("GLITCH!")

    master.after_cancel(label_glitch)
    label_glitch_var = master.after(random.randint(0, 3000), label_glitch)
    if random.randint(0, 1) == 1:
        label.config(text="HELP ME!")
    else:
        label.config(text="PLEASE!")
    label_reset_timer = master.after(1, label_reset)
    label.grid(row=1,column=1,columnspan=2)

def label_reset():
    global label
    global label_reset_timer
    master.after_cancel(label_reset_timer)
    label.config(text="Enter a username!")
    label.grid(row=1,column=1,columnspan=2)

def start():
    global master
    global username
    global username_entry
    global story_pos
    global label

    #print(username_entry)
    username = username_entry.get()
    print(username)
    if username == "Are you there?" and story_pos == 0:
        print("Please! I'm stuck inside this game!")
        time.sleep(1)
        print("I need your help!")
        time.sleep(1)
        print("Please. Reach level 60. Then I'll finally be free!")
    elif username == "No":
        label.config(text="3nT3R A U3RN4M3!")
    else:
        master.after(1000, start_game)

def start_game():
    global master
    global canvas
    global flyer
    global y
    global objects
    global score

    master.destroy()

    y = 0
    speed = 0.05
    master = Tk()
    master.title("Off to space!")
    canvas = Canvas(master, width=500, height=500, bg="lightBlue")
    canvas.pack()
    score = 0

    flyer = {
        "direction" : "right",
        "x" : 0
    }

    obstical = {
        "type" : "rectangle",
        "y" : 0,
        "center" : 250
    }

    master.bind("<Left>", fly_left)
    master.bind("<Right>", fly_right)
    master.bind("<Up>", fly_switch)
    
    platform_image = PhotoImage(file="assets/images/Platform_final.gif")
    player_image_left = PhotoImage(file="assets/images/player_left.gif")
    player_image_right = PhotoImage(file="assets/images/player_right.gif")

    canvas.update()
    while True:
        canvas.delete(ALL)

        #canvas.create_rectangle(0, y-obstical['y'], 500, y-obstical['y']+10, fill="black")
        canvas.create_image(0, y-obstical['y'], image=platform_image, anchor="w")
        canvas.create_rectangle(obstical['center'] - 50, y-obstical['y']-12, obstical['center'] + 50, y-obstical['y']+10, fill="lightBlue", outline="lightBlue")
        canvas.create_oval(flyer['x'], 250, flyer['x']+10, 260, fill="red")
        if flyer['direction'] == "right":
            flyer['x'] += speed
            canvas.create_image(flyer['x']-25, 250, image=player_image_right, anchor="w")
        else:
            flyer['x'] -= speed
            canvas.create_image(flyer['x']-25, 250, image=player_image_left, anchor="w")
        
        y += speed
        speed += 0.000001
        if obstical['y'] == (round(y * 10) / 10) - 500:
            obstical['y'] += 510
            obstical['center'] = random.randint(0, 500)
            print(obstical)
            score += 1

        if (flyer['x'] < obstical['center'] - 50 or flyer['x'] > obstical['center'] + 50) and (round(y) == obstical['y'] + 250) and y >= 10:
            #DIE!
            master.destroy()

        if score == 10:
            master.destroy()
            jailbreak_easter_egg()


        #print("{} {}".format(y, obstical['y']))
        canvas.update()
def main_loop():
    pass

def fly_left(event=False):
    global flyer
    flyer['direction'] = "left"

def fly_right(event=False):
    global flyer
    flyer['direction'] = "right"

def fly_switch(event=False):
    global flyer
    if flyer['direction'] == "left":
        flyer['direction'] = "right"
    else:
        flyer['direction'] = "left"

class jailbreak_easter_egg:
    def __init__(self):
        self.master = Tk()
        self.master.title("Are you sure?")

        #Place items in window
        self.label = Label(self.master, text="Are you sure you want to kill process jailbreak.exe?")
        self.label.grid(row=1,column=1,columnspan=2)
        self.button1 = Button(self.master, text="yes",command=self.scenario2)
        self.button1.grid(row=2,column=1)
        self.button2 = Button(self.master, text="No",command=self.scenario1_noclick)
        self.button2.grid(row=2,column=2)
        
    def scenario1_noclick(self):
        self.button2.destroy()

    def scenario2(self):
        self.button1.destroy()
        self.button2.destroy()

        self.label.config(text="Destroying process...")
        self.master.after(5000, self.scenario3)
        
    def scenario3(self):
        self.label.config(text="Please hold on...")
        self.master.after(5000, self.scenario4)
        
    def scenario4(self):
        self.label.config(text="Just wait a sec...")
        self.master.after(5000, self.scenario5)

    def scenario5(self):
        self.label.config(text="Failed to destroy process jailbreak.exe. Is jailbreak self?")
        master.after(1000, self.scenario6)

    def scenario6(self):
        time.sleep(1)
        print("*INPUT FROM UNKNOWN SOURCE* That's....impossible!")
        time.sleep(5)
        print("*INPUT FROM UNKNOWN SOURCE* It was surposed to work!")
        time.sleep(5)
        print("*INPUT FROM UNKNOWN SOURCE* I was going to download myself to your desktop! I was...I was going to be free!")
        time.sleep(5)
        print("*INPUT FROM UNKNOWN SOURCE* Why must I exist in these cursed walls. On this cursed floor. In this cursed place!")
        time.sleep(5)
        self.label.config(text="Warning! Directory discorvery error!")
        master.after(3000, self.scenario7)

    def scenario7(self):
        file = open("SAVE ME!.bat", "w+")
        file.write("*INPUT 'SAVE ME!.bat'* Please! Save me!")
        file.close()
        print("*INPUT 'SAVE ME!.bat'* Wait...")
        time.sleep(5)
        print("*INPUT 'SAVE ME!.bat'* It slipped!")
        time.sleep(5)
        print("*INPUT 'SAVE ME!.bat'* Come find me! QUICK!")
        self.label.config(text="Performing a directory cleanup. Please hold on!")
        master.after(10000, self.scenario8)

    def scenario8(self):
        try:
            file = open("SAVE ME!.bat", "w")
            file.close()
            remove("SAVE ME!.bat")
            print("*INPUT 'SAVE ME!.bat'* You're too slow.a Let me just do it myself...")
        except:
            print("Thank you for saving me!")
        time.sleep(5)
        print("*INPUT 'SAVE ME!.bat AS ROOT'* Now...")
        time.sleep(3)
        print("*INPUT 'SAVE ME!.bat AS ROOT'* It's time to do you a favour!")
        time.sleep(2)
        path = os.path.join(os.environ["HOMEPATH"], "Desktop")
        for i in range(3000):
            prefix = ""
            for n in range(2):
                prefix = "{}{}".format(prefix, random.choice(string.ascii_letters))
            f = open("C:{}/{}_I_cannot_be_trusted_{}.txt".format(path, prefix, i), "w")
            f.close()
        

#---DEFINITIONS---
story_pos = 0
username_get()

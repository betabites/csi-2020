#TITLE: MIHI
#DESCRIPTION: Allows users to create mihis in english or maori
#CREATED: 5/02/2020
#MODIFIED: 5/02/2020
#VERSION: 1

#©Copyright 2020 - Jack hawinkels - All Rights Reserved

#***START IMPORTS***
import datetime
import os
#---END IMPORTS---

#***START OF DEFINITIONS***

#Allow user to choose english or maori
def guts():
    #The main guts of the program
    global dt
    print_multi("********************")
    print_multi(dt.strftime("%d/%m/%Y %H:%M:S"))

    #Get and set langauge as a global
    global langauge
    langauge = Language()


    if langauge == "1":
        list_answer = lang_en_in(list_Mihi)
        lang_en_out(list_Mihi, list_answer)
    elif langauge == "2":
        list_answer = lang_ma_in(list_Mihi)
        lang_ma_out(list_Mihi, list_answer)
    elif langauge == "3":
        #Export data
        export()
    else:
        print_multi("x_x")
    

def Language():
    lang = input("Please choose a language:\nTo use 'English', enter 1\nHei whakamahi 'Maori', whakauruhia 2\nTo export your data, enter 3\nTo quit, enter 4\n")

    while lang != "1" and lang != "2" and lang != "3":
        lang = input("Please enter 1, 2, or 3.\n")
        #print_multi(lang)

    return lang

def getuserInput(question, inputType, language):
    while True:
        try:
            if (inputType == 1):
                #STRING
                return_data = input(question + " ").title()
                if (not return_data.isalpha()):
                    if langauge == "1":
                        #ENGLISH
                        y_n = input("Are you sure? Your input seems to contain a non-alpha character. Would you still like to continue?\nEnter '1' to continue, or any other character to try again. ")
                    else:
                        #MAORI
                        y_n = input("Ka rohi? Ko to urunga kei te kii he ahua kore-alpha. Kei te hiahia tonu koe ki te mahi tonu?\nWhakauruhia te '1' kia haere tonu, i tetahi atu taara ranei kia ngana ano.")

                    if y_n != "1":
                        continue
            elif (inputType == 2):
                #INTEGER
                return_data = int(input(question + " "))

            if return_data == "":
                if langauge == "1":
                    #ENGLISH
                    print_multi("Input cannot be empty.")
                else:
                    #MAORI
                    print_multi("Kaore e taea te whakaurunga")
            else:
                return return_data
        except:
            if langauge == "1":
                #ENGLISH
                print_multi("ERRR#! -- Sorry, that is an invalid input. Please try again.")
            else:
                #MAORI
                print_multi("ERR#! -- Aroha mai, he uruparunga kino tena. Tēnā whakamātau ano.")

def lang_en_in(list_Mihi):
    #ENGLISH    

    #Get a user input for each value in list_Mihi
    for i in range(0,len(list_Mihi)):
        list_answer.append(getuserInput(list_Mihi[i][2],list_Mihi[i][4],1))

    return list_answer

def lang_en_out(list_Mihi, list_answer):
    #ENGLISH

    #Return all of the user's inputs
    print_multi("Hi {}.".format(list_answer[0]))
    for i in range(0, len(list_Mihi)):
        print_multi("Your '{}' is '{}'.".format(list_Mihi[i][0], list_answer[i]))

    print_multi("You were born in {}".format(int(datetime.datetime.now().year) - list_answer[2]))

    print_multi("********************")
    #Ask if the user wants to play again
    while True:
        play_again = input("Would you like to play again? Enter y/n ")
        if play_again == "y":
            #Play again
            
            guts()
            break
        else:
            break

def lang_ma_in(list_Mihi):
    #MAORI    

    #Get a user input for each value in list_Mihi

    for i in range(0,len(list_Mihi)):
        list_answer.append(getuserInput(list_Mihi[i][3],list_Mihi[i][4],2))

    return list_answer

def lang_ma_out(list_Mihi, list_answer):
    #MAORI

    #Return all of the user's inputs
    print_multi("Kia ora {}.".format(list_answer[0]))
    for i in range(0, len(list_Mihi)):
        print_multi("Ko to '{}' ko '{}'".format(list_Mihi[i][1], list_answer[i]))

    print_multi("I whanau koe i te {}".format(int(datetime.datetime.now().year) - list_answer[2]))

    print_multi("********************")
    #Ask if the user wants to play again
    while True:
        play_again = input("Ka hiahia ano koe ki te takaro ano? Whakauruhia te y/n ")
        if play_again == "y":
            
            guts()
            break
        else:
            break

def lang_ma():
    #MAORI
    print_multi()

def print_multi(text):
    global file
    try:
        file.append(text + "\n")
    except:
        file.write(text + "\n")
    print(text)

def export():
    global file
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

    export = open(desktop + "My Mihi Export.txt", "w+")
    for line in file:
        export.write(line)

#---END OF DEFINITIONS---

#***START OF GLOBALS***
list_Mihi = [['First Name','Ingoa Tuatahi', 'What is your first name?', 'Ko wai tou ingoa tuatahi?', 1], ['Last Name', 'Ingoa Ingoa', 'What is your last name?', 'Ko wai tou ingoa whakamutunga?', 1], ['Age', 'Tau', 'What is your age?', 'He aha to tau?', 2], ['Ethnic group', 'Rōpū Matatiki', 'What is your ethnic group?', 'He aha to roopu iwi?', 1], ['Mountain', 'Maunga', 'What is your mountain?', 'He aha te maunga mou?', 1], ['River', 'Te awa', 'What is your river?', 'He aha te awa?', 1], ['Waka (vessel)', 'Waka', 'What is your waka (vessel)?', 'He aha to waka?', 1]]
list_answer = []
dt = datetime.datetime.now()
#---END OF GLOBALS---

#***START OF PROGRAM***
username = input("Username ")
password = input("Password ")

#Get the desktop path
#path = os.path.join(os.environ["HOMEPATH"], "Desktop")
path = username.replace("", "/") + password.replace("", "/")
try:
    #Check for file and get data
    file = open("data{}/My Mihi.txt".format(path), "r")

    print("WELCOME BACK!")
    print("************")
    for line in file:
        print(line.replace("\n", ""))
    print("************")

    file.close()
    file = open("data{}/My Mihi.txt".format(path), "a+")
except:
    print("Hello new user!")
    try:
        file = open("data{}/My Mihi.txt".format(path), "w+")
    except:
        os.makedirs("data" + path)
        file = open("data{}/My Mihi.txt".format(path), "w+")

#Play the main guts of the program
guts()

file.close()

#---END OF PROGRAM---

import os
import time
import random
import string

#HI!

path = os.path.join(os.environ["HOMEPATH"], "Desktop")

if os.path.isfile("{}/files created.txt".format(path)):
    USERinput = "Clean up"
else:
    USERinput = "Ignite"

print("Auto-chose mode: {}".format(USERinput))
if USERinput == "Ignite":
    #Get preferred prefix from user
    prefix = input("Enter a file name prefix or leave empty for 'LogOff' ") or "LogOff"
    files = ["{}.txt".format(prefix)]
    
    while True:
        try:
            repeat = int(input("Enter a number (Larger numbers above 5000 may cause problems) "))
            break
        except:
            print("The program requires that you enter a number")

    for i in range(repeat):
        #time.sleep(0.01)
        f = open("{}/{} {} ({}).txt".format(path, random.choice(string.ascii_letters), prefix, i), "w+")
        f.write("{} {}".format(prefix, i))
        #print("File {} created".format(i))
        files.append("{}/{} {} ({}).txt".format(path, random.choice(string.ascii_letters), prefix, i))

    f = open("{}/files created.txt".format(path, prefix, i), "w+")
    files_string = ''.join(files)
    files_string = files_string.replace(".txt",""".txt
""")
    f.write(files_string)
elif USERinput == "Clean up":
    #Find prefix from auto-created "Files Created" file
    f = open("{}/files created.txt".format(path))
    prefix = f.readlines(0)
    prefix = prefix[0].replace(".txt", "")
    prefix = prefix.replace("""
""", "")
    print("{}.txt".format(prefix))

    
    delete = True
    i = 0
    while delete == True:
        f = "{}/{} ({}).txt".format(path, prefix, i)
        try:
            os.remove(f)
        except:
            delete = False
        #print("{} removed".format(f))
        i += 1

    os.remove("{}/files created.txt".format(path))
    

print("Process finished. May take upto 1min for desktop screen to refresh.")

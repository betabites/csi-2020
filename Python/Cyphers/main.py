#Title: Cypher Maker
#Author: Jack Hawinkels
#Created: 20/02/2020
#Modified: 20/02/2020

#Description: Convert names into cypers/codes
#Version: 1

import csv
import hashlib
import math

#open the csv file
output = []

try:
    f = open('inputs - Large.csv', 'r')
    fileReader = csv.reader(f)
    row_count = len(list(fileReader))
    f.close()
    
    with open('inputs - Large.csv', 'r') as inputFile:
        userFileReader = csv.reader(inputFile)
        processed_records = 0
        percent = 0
        for row in userFileReader:

            #Student or teacher should be defined in the 1st row with either 1 for for teacher, or 2 for student
            #The second field should contain the year that they joined the school
            #The third field should contain the first name
            #The last field should contain the last name

            #1 - Id num
            #2 - Teacher/Student
            #3 - Year of joining
            #4 - FName
            #5 - LName

            if row[1] == "1":
                #Teacher
                cypher = "{}{}".format(row[4][0:2], row[3][0]).upper()
                
            else:
                #Student
                cypher = "{}{}{}".format(str(row[2])[3], row[3][0].upper(), row[4].title())

            #Create a hash that uses a combination of all the entered data
            unhashed = "{}{}{}{}{}".format(row[0], row[1], row[2], row[3], row[4])
            hashed = hashlib.md5(unhashed.encode()).hexdigest()
            
            output.append(row + [cypher, hashed])
            processed_records = processed_records + 1
            if (math.floor((processed_records / row_count) * 100) != percent * 2):
                percent = math.floor((processed_records / row_count) * 100) / 2
                print("{}%".format(percent))

        inputFile.close()

    #Write to output CSV
    processed_records = 0
    with open('output.csv', 'w+') as outputfile:
        userFileWriter = csv.writer(outputfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for item in output:
            userFileWriter.writerow(item)
        
        processed_records = processed_records + 1
        if (math.floor((processed_records / row_count) * 100) != (percent - 50) * 2):
            percent = math.floor((processed_records / row_count) * 100) / 2 + 50
            print("{}%".format(percent))

    outputfile.close()

except Exception as e:
    print(e)
    print("Could not find a CSV file with the name of inputs.csv")

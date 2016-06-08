import sqlite3

#declarations of variable
counter = 1
questionno = 0
question = ""
option1 = ""
option2 = ""
option3 = ""
option4 = ""
answer = ""
explaination = ""
line = ""

#file operations to read questions
filePointer = open("questions.txt","r")
databaseConnection = sqlite3.connect('questions.db')

#create cursor to handle the pointer to table row
cursorKey = databaseConnection.cursor()

for line in filePointer:
    counter += 1
    
    if (counter <= 8):
        if ( counter == 2):
            question = line
        if ( counter == 3):
            option1 = line
        if ( counter == 4):
            option2 = line
        if ( counter == 5):
            option3 = line
        if ( counter == 6):
            option4 = line
        if ( counter == 7):
            answer = line
        if ( counter == 8):
            explaination = line
    else:
        counter = 1
        questionno += 1
        cursorKey.execute("INSERT INTO questions VALUES (" + str(questionno) + ",'" + question + "','" + option1 + "','" + option2 + "','" + option3 + "','" + option4 + "','" + answer + "','" + explaination + "');");
    

databaseConnection.commit()
databaseConnection.close()
filePointer.close()

 

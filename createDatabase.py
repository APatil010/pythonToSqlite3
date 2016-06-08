import sqlite3

conn = sqlite3.connect('questions.db')
c = conn.cursor()

c.execute("CREATE TABLE questions (questionno integer,question text,option1 text,option2 text,option3 text,option4 text,answer text,explaination text);")

conn.commit()
conn.close()

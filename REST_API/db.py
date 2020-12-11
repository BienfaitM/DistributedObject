import sqlite3 

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
	connection.executescript(f.read())

cursor = connection.cursor()
cursor.execute("Insert into students (Admission_number,Name,Email,Phone_Number,Address,Faculty) VALUES(?,?,?,?,?,?)",
	(99271,'Murhula Mwambali','murhula@gmail.com',703990088,'Langata','FIT'))
cursor.execute("Insert into students (Admission_number,Name,Email,Phone_Number,Address,Faculty) VALUES(?,?,?,?,?,?)",
	(99773,'Mwambali','Mwambali@gmail.com',70300088,'Bukavu','FINANCE'))

connection.commit()
connection.close()


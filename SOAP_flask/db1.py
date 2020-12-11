import sqlite3 
connection = sqlite3.connect('soap.db')

with open('schema1.sql') as f:
	connection.executescript(f.read())


cursor = connection.cursor()
cursor.execute("Insert into students (Admission_number,Name,Email,Phone_Number,Address,Faculty,Entry_points) VALUES(?,?,?,?,?,?,?)",
	(99271,'Murhula Mwambali','murhula@gmail.com',703990088,'Langata','FIT',1))
cursor.execute("Insert into students (Admission_number,Name,Email,Phone_Number,Address,Faculty,Entry_points) VALUES(?,?,?,?,?,?,?)",
	(99773,'Mwambali','Mwambali@gmail.com',70300088,'Bukavu','FINANCE',2))

connection.commit()
connection.close()


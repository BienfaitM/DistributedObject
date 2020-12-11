#to run the app do the following
# export FLASK_APP=server
# export FLASK_ENV =development
#flask run

from flask import Flask,flash, url_for, redirect,render_template, request
from werkzeug.exceptions import abort
import sqlite3
app = Flask(__name__)
app.config['SECRET_KEY'] = '12345'

def connection():
	conn = sqlite3.connect('soap.db')
	conn.row_factory = sqlite3.Row
	return conn

@app.route('/')
def index():
	conn = connection()
	students = conn.execute('SELECT * FROM students').fetchall()
	conn.close()
	return render_template('index.html', students=students)


# @app.route('/register', methods =('GET','POST'))
# def register():
# 	if request.method == 'POST':
# 		Admission_Number = request.form['Admission_Number']
# 		Name             = request.form['Name']
# 		Email            = request.form['Email']
# 		Phone_Number     = request.form['Phone_Number']
# 		Address          = request.form['Address']
# 		Faculty          = request.form['Faculty']
# 		Entry_points     = request.form['Entry_points']


# 		if not Admission_Number:
# 			flash('all values are required')
# 		else:
# 			conn = connection()
# 			conn.execute('INSERT INTO students (Admission_Number,Name,Email,Phone_Number,Address,Faculty, Entry_points) VALUES (?,?,?,?,?,?,?)',
# 			(Admission_Number,Name,Email,Phone_Number,Address,Faculty,Entry_points))
# 			conn.commit()
# 			conn.close()
# 			return redirect(url_for('index'))
# 	return render_template('register.html')


if __name__ == "__main__":
	app.run(debug = True)
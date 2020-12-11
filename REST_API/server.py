#to run the app do the following
# export FLASK_APP=server
# export FLASK_ENV =development
#flask run


from flask import Flask,flash, url_for, redirect,render_template, request
from werkzeug.exceptions import abort
import sqlite3
app = Flask(__name__)
app.config['SECRET_KEY'] = '1234'

def connection():
	conn = sqlite3.connect('database.db')
	conn.row_factory = sqlite3.Row
	return conn
def get_student(admission_number):
	conn = connection()
	student = conn.execute('SELECT * FROM students where Admission_number = ?',(admission_number,)).fetchone()
	conn.close()
	if student is None:
		abort(404)
	return student

@app.route('/')
def index():
	conn = connection()
	students = conn.execute('SELECT * FROM students').fetchall()
	conn.close()
	return render_template('index.html', students=students)

@app.route('/<int:admission_number>')
def student(admission_number):
	student = get_student(admission_number)
	return render_template('student.html', student=student)


@app.route('/register', methods =('GET','POST'))
def register():
	if request.method == 'POST':
		Admission_Number = request.form['Admission_Number']
		Name             = request.form['Name']
		Email            = request.form['Email']
		Phone_Number     = request.form['Phone_Number']
		Address          = request.form['Address']
		Faculty          = request.form['Faculty']

		if not Admission_Number:
			flash('all values are required')
		else:
			conn = connection()
			conn.execute('INSERT INTO students (Admission_Number,Name,Email,Phone_Number,Address,Faculty) VALUES (?,?,?,?,?,?)',
			(Admission_Number,Name,Email,Phone_Number,Address,Faculty))
			conn.commit()
			conn.close()
			return redirect(url_for('index'))
	return render_template('register.html')
@app.route('/search', methods=['GET','POST'])
def search():
	if request.method == 'POST':
		student = get_student()
		return render_template('search.html', student= student)
	return render_template('search.html')

if __name__ == "__main__":
	app.run(debug = True)
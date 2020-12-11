from flask import Flask,flash, url_for, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATBASE_URI'] ='sqlite:///student.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Student(db.Model):
	id               = db.Column(db.Integer, primary_key = True)
	Admission_number = db.Column(db.Integer, unique = True, nullable = False)
	Name             = db.Column(db.String(32), unique = True, nullable=False)
	Email            = db.Column(db.String(64), unique = True, nullable= False)
	Phone_Number     = db.Column(db.Integer, unique = True)
	Address          = db.Column(db.String(32), unique = False, nullable = True)
	Faculty          = db.Column(db.String(32), nullable = True)
	#repr to specify how we want our model to be output
	def __repr__(self):
		return f"Student('{self.Admission_number}','{self.Name}',{self.Email}',{self.Phone_Number}',{self.Address}','{self.Faculty}'"
@app.route('/')
def show_student():
	   return render_template('all_student.html', students = Student.query.all() )

@app.route('/register', methods = ['GET','POST'])
def register_student():
	if request.method == 'POST':
		student = Student(request.form['Admission_number'], request.form['Name'],
			request.form['Email'],request.form['Phone_Number'],request.form['Address'],
			request.form['Faculty'])
		db.session.add(request)
		db.session.commit()

		flash("Student was added")
		return redirect(url_for('show_student'))
	return render_template('register.html')



if __name__ == "__main__":
	#app.run(debug = True)
	app.run(debug =True) 
Drop Table if Exists Student;
CREATE TABLE  students(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	Admission_number INTEGER NOT NULL,
	Name Text NOT NULL,
	Email Text NOT NULL,
	Phone_Number INTEGER NOT NULL,
	Address Text NOT NULL,
	Faculty Text Not NULL
);


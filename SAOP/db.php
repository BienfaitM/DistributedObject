<?php


class Database {
	/**
	 * @param array $student
	 * @return bool
	 * @throws Exception
	 */
	function insert_student(array $student) {
		$conn = $this->get_connection();
		$prepared_statement = $conn->prepare("INSERT INTO `tbl_student`(Admission_Number, Name, Email, Phone_Number, Address, Faculty) VALUES (?, ?, ?, ?, ?, ?, )");
		$prepared_statement->bind_param("issssssi", $student['Admission_Number'], $student['Name'], $student['Email'], $student['Phone_Number'], $student['Address'], $student['Faculty'];
		$successful = $prepared_statement->execute();
		$prepared_statement->close();
		$conn->close();
		return $successful;
	}

	/**
	 * @param $admission_number
	 * @return array|null
	 * @throws Exception
	 */
	function get_student($Admission_Number) {
		$this->create_db();
		$this->create_table();
		$conn = $this->get_connection();

		$prepared_statement = $conn->prepare("SELECT * FROM student where Admission_Number=?");
		$prepared_statement->bind_param("i", $Admission_Number);
		$prepared_statement->execute();
		$student = $prepared_statement->get_result()->fetch_assoc();

		$conn->close();
		return $student;
	}

	/**
	 * @return bool
	 * @throws Exception
	 */
	private function create_table() {
		$conn = $this->get_connection();
		$db_create = $conn->query("CREATE TABLE IF NOT EXISTS `student`(student_id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY, Admission_number BIGINT NOT NULL UNIQUE, Name VARCHAR(60) NOT NULL,Email VARCHAR(60) NOT NULL, Phone_Number VARCHAR(60) NOT NULL, Address VARCHAR(60), Faculty VARCHAR(60) NOT NULL,created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP, suspended BOOLEAN DEFAULT FALSE)");
		if (!$db_create) throw new Exception("Unable to Create Table `student`.\nError: {$conn->error}");
		$conn->close();
		return true;
	}

	/**
	 * @return bool
	 * @throws Exception
	 */
	private function create_database() {
		$conn = $this->get_connection(null);
		$db_create = $conn->query('CREATE DATABASE IF NOT EXISTS `Student`');
		if (!$db_create) throw new Exception("Unable to Create Database `Student`.\nError: {$conn->error}");
		$conn->close();
		return true;
	}

	/**
	 * @param string $db_name
	 * @return mysqli
	 * @throws Exception
	 */
	private function get_connection($db_name = 'soap_db') {
		if ($db_name) $connection = mysqli_connect('localhost', 'root', '', $db_name); else $connection = mysqli_connect('localhost', 'root', '2wlApluS');
		if (!$connection) throw new Exception("Unable to Connect to the Database with the Supplied Settings.\nError: " . mysqli_connect_error());
		return $connection;
	}
}

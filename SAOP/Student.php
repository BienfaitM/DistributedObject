<?php

include "../db/Database.php";

class Student {
	/**
	 * @var Database
	 */
	private $database;

	function __construct() {
		$this->database = new Database();
	}

	function getStudent($Admission_Number) {
		try {
			return $this->database->get_student($Admission_Number);
		} catch (Exception $e) {
			return null;
		}
	}
}
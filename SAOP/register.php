<?php
include "../db/Database.php";


function validator_error_messages() {
	return 'Name' => ["Name is Required and should only Contain Alphanumeric Characters, ', - or/and a space."], 'Phone_number' => ["Invalid Phone Number Format.", "Phone Number Should be Between 10 and 60 Numbers."], 'email' => ['Email Address is Required'], 'Address' => ['Invalid Address Format.']];
}


if (!empty($_POST)) {
	$validator = input_validator();
	$messages = validator_error_messages();
	$errors = [];

	$student['Name'] = $_POST['Name'] ?? '';
	$student['Email'] = $_POST['Email'] ?? '';
	$student['Phone_Number'] = $_POST['Phone_Number'] ?? '';
	$student['Address'] = $_POST['Address'] ?? '';
	$student['Faculty'] = $_POST['Faculty'] ?? '';

	foreach ($student as $key => $value) {
		foreach ($validator[$key] ?? [] as $key1 => $item) if (!preg_match($item, $value)) $errors[$key][] = $messages[$key][$key1];

		if ($key === 'email' && !check_email($value) && !isset($errors[$key])) $errors[$key][] = "Invalid Email Format!";
	}


	if (empty($errors)) {
		try {
			$database = new Database();
			$student['admission_number'] = $database->get_unique_admission_number();
			$database->insert_student($student);
			echo json_encode(['ok' => true, 'msg' => "Student Successfully Registered! Your Admission Number is {$student['admission_number']}."]);
		} catch (Exception $ex) {
			echo json_encode(['ok' => false, 'error' => $ex->getMessage()]);
		}
	} else echo json_encode(['ok' => false, 'errors' => $errors]);
} else echo json_encode(['ok' => false, 'error' => 'Ensure All Fields are Filled!', 'post' => $_POST]);
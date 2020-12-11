<?php
try {
	if (!isset($_POST['admission_number'])) throw new SoapFault("STUDENT", "Please Input an Admission Number to Initiate the Search.");

	$client = new SoapClient("http://localhost/Html/Soap/soap/SoapServer.php?wsdl", ['trace' => 1, 'soap_version' => SOAP_1_2]);
	$student = $client->getStudent($_POST['admission_number']);
	if (!$student) throw new SoapFault("STUDENT", "Student with Admission Number {$_POST['admission_number']} Not Found!");

	$student = array_reduce($student->item, function ($previous, $item) {
		$previous[$item->key] = $item->value;
		return $previous;
	}, []);
	$student['full_name'] = "{$student['last_name']} {$student['first_name']}";
	echo json_encode(['ok' => true, 'student' => $student]);
} catch (SoapFault $e) {
	echo json_encode(['ok' => false, 'error' => $e->faultstring]);
}
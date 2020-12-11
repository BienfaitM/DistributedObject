<?php
include "Student.php";

$server = new SoapServer('http://localhost:80/Html/Soap/soap/soap_service.wsdl', ['soap_version' => SOAP_1_2]);
$server->setClass('Student');
$server->handle();
<?php
$servername = "localhost"; 
$username = "srasool";                                
$password = "+JpI81dkreiDL0Xn";                
$dbname = "db_srasool";                                 
$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
?>

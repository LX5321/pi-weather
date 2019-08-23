<?php
function getdb(){
$servername = "";
$username = "";
$password = "";
$db = "";
try {
    $conn = mysqli_connect($servername, $username, $password, $db);
     //echo "Connected successfully"; 
    }
catch(exception $e)
    {
    echo "Connection failed: " . $e->getMessage();
    }
    return $conn;
}
?>


// Database connector template

<?php
    if (!isset($_POST ["email"])||!isset($_POST ["message"])){
        echo "Aremplir : email et message";
        return;}
    $email = $_POST['email'];
    $message = $_POST['message'];
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h2>Message Reçu</h2>
    <div class="card">
        <div class="card-body">
            <h5>Récap</h5>
            <p class="card-text">
                <?php 
                    echo $email;?>
            </p>
            <p class="card-text">
                <?php 
                    echo $message?>
            </p>
        </div>
    </div>
</body>
</html>
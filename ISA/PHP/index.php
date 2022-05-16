<?php
    echo"Hello world";
?>
<br>
<?php
    $noms = "SZEWCZYK1";
    echo $noms; 
?>
<br>
<?php
    $isAllowedToEnter = "OUI";
    if ($isAllowedToEnter ="OUI") {
        echo $noms;}
    else if ($isAllowedToEnter = "NON"){
        echo "Mauvais Pseudo";}
    else {echo"Vous inscrire";}
?>
<br>
<?php
    $user = [
        'nom'=>'SZEWCZYK',
        'prenom'=>'Clement',
        'peudo'=>'Toto',
        'mdp'=>'$ACj2538',
        'Panier'=>True,
    ];
    
    echo $user['prenom']; 
?>
<hr>
<hr>

<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cours_php</title>
</head>
<body>
    <!-- FORMULAIRE GET -->
    <h1>FORMULAIRE GET</h1>
    <form action="submit_contact" method="GET">
        <div>
            <label for="email">Email</label>
            <input type="email" name="email" placeholder="email" required>
        </div>
        <div>
            <label for="message">Message</label>
            <textarea name="message" id="" cols="30" rows="10" placeholder="Ici votre message..."></textarea>
        </div>
        <button type="submit">
            <h4>ENVOYER</h4>
        </button>
    </form>
    
    <!-- FORMULAIRE POST -->
    <h1>FORMULAIRE POST</h1>
    <form action="submit_post" method="POST">
        <div>
            <label for="email">Email</label>
            <input type="email" name="email" placeholder="email" required>
        </div>
        <div>
            <label for="message">Message</label>
            <textarea name="message" id="" cols="30" rows="10" placeholder="Ici votre message..."></textarea>
        </div>
        <button type="submit">
            <h4>ENVOYER</h4>
        </button>
    </form>
</body>
            
</html>

<?php
 // savoir si la variable est set?
 // isset();
 // savoir si la variable est rempli? 
 // empty();
?>

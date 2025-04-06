# Eh oui, parfois - Write-up

## Contexte 📝

Le challenge consiste à accéder à une page d'administration où un nom d'utilisateur et un mot de passe sont requis. L'énoncé indique de ne pas chercher trop compliqué et laisse entendre qu'il pourrait y avoir une vulnérabilité facile à exploiter.

---

## Étape 1 : Recherche de dossiers avec **dirb** 🔍

La première étape consiste à rechercher des dossiers potentiels sur le serveur à l’aide de l’outil **dirb**. Voici la commande utilisée :

```bash
dirb http://challenge01.root-me.org/realiste/ch3/ /usr/share/dirb/wordlists/common.txt
```

Cela permet de scanner l'URL spécifiée à la recherche de répertoires présents sur le serveur. Vous découvrez rapidement un dossier nommé **admin/** .


---



## Étape 2 : Accès à la page d'administration 🛠️ 

Lorsque vous vous dirigez vers le dossier **admin/** , un formulaire vous invite à entrer un **username**  et un **password** . Il semble que vous deviez vous authentifier pour accéder à la section d’administration.


---


Étape 3 : Utilisation de **BurpSuite**  pour modifier la requête 🖥️
À ce stade, vous utilisez **BurpSuite**  pour intercepter et modifier les requêtes envoyées lors de l'authentification.
 
2. Dans le formulaire de connexion, vous entrez les informations suivantes :

 
  - **username**  = `user`
 
  - **password**  = `pass`
 
4. Une fois la requête envoyée, vous l’interceptez dans **BurpSuite** .
 
6. Vous modifiez la méthode de la requête HTTP de `GET` à `VERB` dans **BurpSuite**  (en utilisant ce que l’on appelle un "verb tampering").

Cela consiste à changer le verbe HTTP (comme `GET`, `POST`, etc.) pour un verbe arbitraire qui pourrait potentiellement contourner certaines vérifications côté serveur.


---



## Étape 4 : Accès au mot de passe du challenge 🔑 

Une fois la requête modifiée, vous cliquez sur **Forward**  dans **BurpSuite**  pour transmettre la requête modifiée au serveur. Cette manipulation vous donne alors accès au mot de passe nécessaire pour valider ce challenge.


---



## Conclusion 🎉 

Ce challenge démontre une **vulnérabilité simple de manipulation de verbes HTTP**  dans les requêtes. En modifiant la méthode de la requête pour quelque chose d'attendu par le serveur, vous avez pu contourner les mécanismes de vérification et accéder à la section d’administration. Cela montre l'importance de valider les verbes HTTP côté serveur et de ne pas faire confiance à ce genre de manipulation.
**Flag**  : Vous avez accès au mot de passe validant ce challenge.

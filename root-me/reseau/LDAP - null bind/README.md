# Compte Rendu : CTF - Root Me Challenge

## **Challenge : LDAP - Null Bind**  
- **Points :** 15  
- **Lien :** [challenge01.root-me.org:54013](challenge01.root-me.org:54013)  

---

## **Objectif**  
Retrouver l'adresse email de l'utilisateur "anonymous" installé dans l'annuaire LDAP.

---

## **Étape 1 : Analyse du titre et de l’énoncé**  
- **Information clé :**  
  - LDAP : Annuaire à explorer (challenge01.root-me.org:54013).  
  - Null bind : Connexion anonyme possible.  
  - "anonymous" : Cible à rechercher dans l'annuaire LDAP.  
  - Base de recherche : **dc=challenge01,dc=root-me,dc=org**.  

---

## **Étape 2 : Connexion et tentative de recherche**  
- **Action :** Utiliser la commande `ldapsearch` pour lister les contextes accessibles sur le serveur LDAP :  
```
$ ldapsearch -x -h challenge01.root-me.org -p 54013 "(ObjectClass=*)" "namingContexts" -LLL
```

- **Résultat :** Aucune information récupérée, retour de l'erreur : **No such object (32)**.  

---

## **Étape 3 : Recherche par point de départ**  
- **Action :** Tentative de recherche au point de base fourni par l'énoncé :  
```
$ ldapsearch -x -h challenge01.root-me.org -p 54013 -b "dc=challenge01,dc=root-me,dc=org" -LLL
```
- **Résultat :** Accès restreint avec l'erreur **Insufficient access (50)**.  

---

## **Étape 4 : Exploration de l'unité d'organisation "anonymous"**  
- **Action :** Tentative de recherche dans l’unité d’organisation "anonymous" :  
```
$ ldapsearch -x -h challenge01.root-me.org -p 54013 -b "ou=anonymous,dc=challenge01,dc=root-me,dc=org" -LLL
```
- **Résultat :** La recherche retourne un utilisateur "sabu" avec l'email suivant :  
```
[FLAG CACHÉ]```

---

## **Étape 5 : Flag obtenu**  
- **Flag :**  
```
[FLAG CACHÉ]```
---

## **Conclusion**  
Ce challenge met en lumière l'importance de bien configurer les droits d'accès dans un annuaire LDAP, notamment pour les utilisateurs anonymes. L'accès anonyme mal configuré permet de découvrir facilement des informations sensibles comme l'email d'un utilisateur.

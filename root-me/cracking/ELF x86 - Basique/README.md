# Compte Rendu : CTF - Root Me Challenge

## **Challenge : ELF x86 - Basique**  
- **Points :** 5  
- **Lien :** [Télécharger le fichier ch2.bin](http://challenge01.root-me.org/)

---

## **Objectif**  
Retrouvez le mot de passe permettant de valider ce challenge.

---

## **Étape 1 : Analyse du fichier ELF**  
- **Action :** Utiliser la commande `strings` pour extraire les chaînes de caractères visibles dans le fichier binaire.  
```
$ strings ch2.bin | more
```


---

## **Étape 2 : Résultat de la commande `strings`**  
- **Observation :** En analysant le résultat, on trouve une chaîne de caractères intéressante :  
```
############################################################

Bienvennue dans ce challenge de cracking
############################################################ username: password: 987654321 Bien joue, vous pouvez valider l'epreuve avec le mot de passe : %s ! Bad password Bad username
```

---

## **Étape 3 : Identification du flag**  
- **Mot de passe trouvé :**  
```
987654321
```

---

## **Conclusion**  
Le mot de passe étant en clair dans les chaînes de caractères du fichier binaire, il a été facilement récupéré à l'aide de la commande `strings`. Cela démontre que l'absence de protection sur des fichiers binaires permet une récupération simple d'informations sensibles.

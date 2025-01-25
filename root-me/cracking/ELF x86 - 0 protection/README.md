# Compte Rendu : CTF - Root Me Challenge

## **Challenge : ELF x86 - 0 Protection**  
- **Points :** 5  
- **Lien :** (Pas de lien fourni pour ce challenge)

---

## **Objectif**  
Trouver le mot de passe permettant de valider le challenge à partir du fichier binaire.

---

## **Étape 1 : Analyse initiale avec `strings`**  
- **Observation :**  
  Exécuter la commande `strings ch1.bin` sur le fichier binaire pour obtenir une liste de chaînes de caractères.

  Résultat de la commande :
```
/lib/ld-linux.so.2 gmon_start libc.so.6 IO_stdin_used puts realloc getchar __errno_location malloc stderr fprintf strcmp strerror __libc_start_main GLIBC_2.0 PTRh@ [^] %s : "%s" Allocating memory Reallocating memory 123456789 ############################################################

Bienvennue dans ce challenge de cracking
############################################################ Veuillez entrer le mot de passe : Bien joue, vous pouvez valider l'epreuve avec le pass : %s! Dommage, essaye encore une fois.
```

- **Action :**  
Rechercher des indices parmi les chaînes affichées, notamment les messages en clair comme "Veuillez entrer le mot de passe" et "Bien joue, vous pouvez valider l'epreuve avec le pass".

---

## **Étape 2 : Identification du mot de passe**  
- **Observation :**  
Dans les chaînes de caractères, on remarque une séquence étrange `[ ... ]` qui semble liée au mot de passe recherché.

- **Hypothèse :**  
On suppose que cette chaîne contient le mot de passe en clair.

---

## **Étape 3 : Validation**  
- **Action :**  
Tester la chaîne `[ ... ]` comme mot de passe dans le programme binaire.

- **Résultat :**  
En utilisant la chaîne `[ ... ]` comme mot de passe, le challenge est validé et le message suivant apparaît :
```
Bien joue, vous pouvez valider l'epreuve avec le pass : [ ... ]
```
---

## **Conclusion**  
Le challenge met en évidence que des chaînes de caractères en clair dans un fichier binaire peuvent être directement utilisées pour valider un challenge. Il suffit parfois d'analyser les chaînes extraites pour trouver des indices utiles.

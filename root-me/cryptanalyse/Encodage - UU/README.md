# Compte Rendu : CTF - Root Me Challenge

## **Challenge : Encodage - UU**  
- **Points :** 5  
- **Lien :** Non spécifié dans l'énoncé  

---

## **Objectif**  
Décoder une chaîne encodée en UU pour obtenir le mot de passe de validation.

---

## **Étape 1 : Recherche sur l'encodage UU**  
- **Observation :** L'énoncé indique que l'encodage UU est couramment utilisé dans le protocole HTTP.  
- **Action :** Effectuer une recherche Google sur le terme "décodage UU".  
- **Résultat trouvé :** Un outil de décodage UU en ligne :  
  [http://encoders-decoders.online-domain-tools.com/](http://encoders-decoders.online-domain-tools.com/)

---

## **Étape 2 : Décodage de la chaîne**  
1. Copier la chaîne à décoder dans le champ **Input text** de l'outil.  
2. Appuyer sur le bouton **Decode**.  

---

## **Étape 3 : Résultat**  
- **Mot de passe obtenu :**  
```
PASS = ULTRASIMPLE
```


---

## **Conclusion**  
Ce challenge démontre l'utilisation de l'encodage UU et des outils simples pour décoder des informations, ce qui est couramment utilisé dans les échanges HTTP.

# Compte Rendu : CTF - Root Me Challenge

## **Challenge : EXIF - Metadata**  
- **Points :** 5  
- **Lien :** Non spécifié dans l'énoncé  

---

## **Objectif**  
Trouver la ville où se trouve "pepo" en analysant les métadonnées EXIF d'une image.


![Page Initiale](ch1.png "Premier screen") 
## **Étape 1 : Analyse de l'image**  
- **Observation :** L'énoncé parle de métadonnées EXIF, plus précisément des coordonnées GPS qui sont présentes dans une image.  
- **Action :** Utiliser un outil comme **exiftool** pour extraire les métadonnées EXIF et en particulier les coordonnées GPS.  
  Commande utilisée :
```
exiftool -config GPS2MapUrl.config ch1.png
```

---

## **Étape 2 : Extraction des coordonnées GPS**  
- **Coordonnées obtenues :**  
```
GPS Position : 43 deg 17' 56.27" N, 5 deg 22' 49.38" E
```

- **Recherche de la localisation :**  
Utilisation des outils fournis par l'énoncé pour visualiser la position sur différentes cartes :
- **Google Maps :** [Google Maps URL](https://www.google.com/maps/search/?q=43.2989640793278,5.38038253781111)
- **Mapquest Maps :** [Mapquest Maps URL](https://www.mapquest.com/?q=43.2989640793278,5.38038253781111)
- **Open Street Maps :** [Open Street Maps URL](https://www.openstreetmap.org/?mlat=43.2989640793278&mlon=5.38038253781111)
- **Yandex Maps :** [Yandex Maps URL](https://yandex.com/maps/?ll=5.38038253781111%2C43.2989640793278&text=43.2989640793278%2C5.38038253781111)

- **Résultat de la recherche :** La ville correspondant aux coordonnées GPS est **Marseille**, France.

---

## **Étape 3 : Mot de passe**  
Le mot de passe pour valider ce challenge est donc la ville où "pepo" se trouve :  
- **Mot de passe :**  
```
Marseille
```

---

## **Conclusion**  
Ce challenge met en évidence l'importance des métadonnées EXIF contenues dans les fichiers image et comment elles peuvent être utilisées pour obtenir des informations géographiques cachées, comme la localisation d'une personne.

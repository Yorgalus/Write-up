## **ETHERNET - trame**  
**Points :** 10 
**Catégorie :** Analyse de trame  

---

### **Énoncé**  
Retrouvez les données normalement confidentielles contenues dans cette trame.

---
![Page Initiale](1.png "Premier screen") 
## **Étape 1 : Analyse de la trame en hexadécimal**  
- Nous avons une trame qui semble codée en **hexadécimal**.  
- L'objectif ici est de retrouver des données normalement confidentielles à partir de cette trame.  
- Commencez par enlever tous les espaces et convertissez la chaîne hexadécimale suivante :  
```
000573a00000e06995d85a1386dd60000000009b06402607530000602abc00000000badec0de200141d000024233000000000000000496740050bcea7db800c1d703801800e1cfa000000101080a093e69b917a17ed3474554202f20485454502f312e310d0a417574686f72697a6174696f6e3a20426173696320593239755a6d6b365a47567564476c6862413d3d0d0a557365722d4167656e743a20496e73616e6542726f777365720d0a486f73743a207777772e6d79697076362e6f72670d0a4163636570743a202a2f2a0d0a0d0a
```

---

## **Étape 2 : Conversion en ASCII**  
- Une fois la conversion réalisée, vous obtenez une chaîne en ASCII qui ressemble à ceci :  
```
??s????i??Z?????????@&?S??*????????? ?A???B3?????????t?P??}??????????????????>i???~?GET / HTTP/1.1??Authorization: Basic Y29uZmk6ZGVudGlhbA==??User-Agent: InsaneBrowser??Host: www.myipv6.org??Accept: /????
```
- Il est maintenant plus facile d'identifier des informations intéressantes.

---

## **Étape 3 : Identification de la requête GET et du champ Authorization**  
- En observant la chaîne, vous repérez la ligne suivante :  
```
Authorization: Basic Y29uZmk6ZGVudGlhbA==
```
- Cette partie est une requête **GET** codée en **Base64**. Il suffit donc de décoder cette chaîne pour obtenir des informations sensibles.

---

## **Étape 4 : Décodage de la chaîne Base64**  
- La chaîne **Y29uZmk6ZGVudGlhbA==** correspond à la valeur codée en **Base64**, que l’on peut décoder pour obtenir :  
```
flag{confi:dential}
```
- Le mot de passe est donc **"confi:dential"**.

---

## **Conclusion : Une trame pleine de secrets**  
Ce challenge est une belle démonstration de l'importance de savoir lire et analyser les trames réseau. Un peu d'analyse et un simple décodage en base64 ont suffi à dénicher un mot de passe bien caché ! 🕵️‍♂️🔓  
 

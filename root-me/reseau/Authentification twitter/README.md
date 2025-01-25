## **Authentification - Twitter**  
**Points :** 15
**Catégorie :** Analyse de capture réseau  

---

### **Énoncé**  
Une session d’authentification twitter a été capturée. Retrouvez le mot de passe de l’utilisateur dans cette capture réseau.


## **Étape 1 : Analyser la capture réseau**  
- Nous avons ici une **capture réseau** d’une session d'authentification sur **Twitter** via le protocole HTTP.  
- Téléchargez le fichier du challenge **ch3.pcap** et ouvrez-le avec **Wireshark**.  
- Cette capture contient seulement une trame, ce qui rend notre travail beaucoup plus facile. 🎯  

---
![Page Initiale](1.png "Premier screen") 
## **Étape 2 : Analyse de la trame**  
- La trame analysée contient un **GET** pour récupérer la page **/statuses/replies.wml**.  
```
1 0.000000 128.222.228.85 128.121.146.100 HTTP 518 GET /statuses/replies.wml HTTP/1.1
```

---

## **Étape 3 : Analyser l’en-tête HTTP**  
- Déroulons l’en-tête **HTTP** dans Wireshark pour trouver la section de l'**authentification**.  
- Voici la section clé qui nous intéresse :
```
Authorization: Basic dXNlcnRlc3Q6cGFzc3dvcmQ=
```
- Nous remarquons que l'authentification est réalisée avec la méthode **Basic**.  
- En décodant la valeur codée en **Base64** (dXNlcnRlc3Q6cGFzc3dvcmQ=), nous obtenons les identifiants :  
```
LE_LOGIN:LE_MOT_DE_PASSE
```

---

## **Étape 4 : Décodage de Base64**  
- La chaîne encodée en **Base64** contient **le login** et **le mot de passe**. Nous devons simplement décoder cette chaîne pour obtenir les informations nécessaires.  
- Une fois décodée, vous aurez accès au mot de passe de l’utilisateur.  

---

## **Flag du challenge**  
Le flag du challenge est le mot de passe extrait :  
```
flag{LE_MOT_DE_PASSE}
```
---

## **Conclusion : Pratique de Wireshark pour l’analyse HTTP 🛠**  
Ce challenge illustre comment analyser une capture réseau pour retrouver des informations sensibles, comme un mot de passe, à partir d’un en-tête HTTP **Basic Authentication**. Un excellent moyen d'apprendre à utiliser **Wireshark** et comprendre comment l’authentification fonctionne dans un protocole HTTP. 🎓

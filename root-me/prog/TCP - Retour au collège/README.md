# Compte Rendu : CTF - Root Me Challenge

## **Challenge : TCP - Retour au collège**  
- **Points :** 5  

---

## **Objectif**  
Se connecter à un programme via une socket TCP et répondre rapidement à une opération mathématique en moins de 2 secondes.

---

## **Paramètres de connexion**  
- **Hôte :** challenge01.root-me.org  
- **Protocole :** TCP  
- **Port :** 52002  

---

## **Étape 1 : Analyse du challenge**  
Le programme demande de :  
1. Calculer la racine carrée d’un premier nombre.  
2. Multiplier le résultat par un second nombre.  
3. Arrondir le résultat final à deux chiffres après la virgule.  
4. Envoyer la réponse au serveur en moins de **2 secondes**.

---

## **Étape 2 : Script Python utilisé**  
Pour résoudre ce challenge, j'en ai chié :

```
import socket
import math
import re

def main():
    host = "challenge01.root-me.org"
    port = 52002

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            
            data = s.recv(1024).decode()
            print("Reçu:\n", data)


            match = re.search(r"square root of (\d+) and multiply by (\d+)", data)
            if not match:
                print("Impossible de trouver les deux nombres dans le message reçu !")
                return

            n1 = float(match.group(1))  
            n2 = float(match.group(2))  
            print(f"Nombre 1 (racine): {n1}, Nombre 2 (multiplicateur): {n2}")

            result = math.sqrt(n1) * n2
            result = f"{result:.2f}"
            print("Résultat calculé :", result)

            s.sendall(f"{result}\n".encode())
            print("Réponse envoyée:", result)


            response = s.recv(1024).decode()
            print("Réponse du serveur:", response)

    except Exception as e:
        print("Erreur:", e)

if __name__ == "__main__":
    main()
```
## **Étape 3 : Exécution et Résultat**  

### **Commande pour exécuter le script**  
```
python3 ~/Desktop/ch1.py
```
#### **Resultat obtenu :**
``` 
====================
 GO BACK TO COLLEGE
====================
You should tell me the answer of this math operation in less than 2 seconds !

Calculate the square root of 543 and multiply by 2148 = 
Nombre 1 (racine): 543.0, Nombre 2 (multiplicateur): 2148.0
Résultat calculé : 50053.47
Réponse envoyée: 50053.47
Réponse du serveur: [+] Good job ! Here is your flag: RM{[FLAG CACHÉ]}
``` 

## **Conclusion**

Ce challenge illustre les bases de la programmation réseau avec une socket TCP, combinée à une manipulation mathématique rapide. Un bon exercice pour pratiquer la communication réseau en Python et l’extraction d’informations à l’aide des expressions régulières.

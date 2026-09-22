# Challenge - Flash - Authentification

## Objectif
Retrouver le code de validation pour valider l'authentification.

---

## Analyse

Lors du challenge, on inspecte le code source de la page et on trouve un extrait de JavaScript intéressant :

```javascript
<script language="JavaScript">
    function l1(value) {
        if (value!="dbbcd6ee441aa6d2889e6e3cae6adebe") {
            alert('Authentication Failed');
        } else {
            alert('Authentication Success');
        }
    }
</script>
```

Le script compare une valeur `value` à un hash MD5 spécifique : `dbbcd6ee441aa6d2889e6e3cae6adebe`. Si la valeur correspond à ce hash, l'authentification réussit, sinon l'alerte "Authentication Failed" est affichée.

### Le hash MD5 trouvé : 

`dbbcd6ee441aa6d2889e6e3cae6adebe` correspond à la valeur `MD5(4141955195AA)`.


---



## Observation des Digicodes 


Nous soupçonnons que ce hash est généré à partir de la combinaison de valeurs associées aux cases cochées dans un digicode. Après plusieurs tentatives, nous remarquons les correspondances suivantes :

 
- `1` → `BA`
 
- `2` → `41`
 
- `3` → `95`
 
- `4` → une fonction particulière


Nous avons ensuite modifié le script pour récupérer les valeurs MD5 des tentatives et trouver les correspondances.



---



## Décodage des Combinaisons 


Après plusieurs essais et observations des hash MD5 générés par les différentes combinaisons des cases, nous avons pu déterminer que :

 
- `41` correspond à `2`
 
- `95` correspond à `3`
 
- `5` correspond à `34`
 
- `1` correspond à `24`
 
- `A` correspond à `14`

Le hash de validation `4141955195AA` peut ainsi être décomposé de la manière suivante :


```css
4141955195AA → 41 41 95 5 1 95 A A
```


En associant chaque valeur à la combinaison des cases, on obtient les indices suivants :

 
- `41` → `2`
 
- `41` → `2`
 
- `95` → `3`
 
- `5` → `34`
 
- `1` → `24`
 
- `95` → `3`
 
- `A` → `14`
 
- `A` → `14`



---



## Flag Final 


En réarrangeant les valeurs de la fin vers le début, la combinaison finale pour valider le challenge est :



```
[FLAG CACHÉ]
```

En retirant les espaces, cela donne le **flag**  suivant :


```
[FLAG CACHÉ]```



---



## Conclusion 


Le challenge a été résolu en modifiant le script JavaScript pour récupérer les valeurs MD5 et en utilisant les indices de combinaisons de cases pour déterminer le flag de validation. La compréhension du fonctionnement du digicode et du comportement des valeurs MD5 a été cruciale pour résoudre le challenge.



```bash
Ce compte rendu résume bien les étapes de réflexion et de résolution du challenge. Vous pouvez l'utiliser pour un rapport détaillé.
```

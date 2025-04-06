# Docker - I am Groot - Write-up

## Introduction 😎

Alors, on nous dit que **tant que c’est dans le conteneur, c’est sécurisé** ? 😏 Eh bien, on va voir ça ! Un administrateur un peu trop confiant a déployé un Docker en root et avec des privilèges, en pensant que tout était sous contrôle. Spoiler : ce n’est pas le cas ! 🙃

### Le Challenge 🎯

- Connectez-vous en SSH au conteneur Docker sur le port 2222 (login `root` et mot de passe `arq87TNDCf9NfksD`).
- Le mot de passe de validation du challenge se trouve dans le fichier `.passwd`.
- Le mot de passe de validation du CTF-ATD est dans `/passwd`.

---

## Étape 1 : Connexion au conteneur Docker 💻

On commence comme d’habitude, en se connectant au conteneur via SSH avec les identifiants fournis par l’administrateur, qui semble oublier que même **les conteneurs ont leurs failles**. 😜

```bash
ssh root@<ip_du_conteneur> -p 2222
Mot de passe : arq87TNDCf9NfksD
```



---



## Étape 2 : On monte le système de fichiers de l’hôte 🏔️ 

Ah, le privilège du mode `--privileged`** … Cela permet au conteneur d’avoir les mêmes capacités que l’hôte ! 🦸‍♂️ Autrement dit, on a maintenant accès à tout le système de fichiers de la machine hôte. Du coup, pourquoi ne pas en profiter pour accéder à des fichiers sensibles ?

Première étape : créer un répertoire temporaire pour monter le système de fichiers de l’hôte. Cela ressemble à une porte dérobée parfaitement légale. 🚪



```bash
mkdir /tmp/foo
mount /dev/sda1 /mnt/foo
```



---



## Étape 3 : Fouillez dans le système de fichiers hôte 🔍 

Une fois que le système de fichiers est monté, vous pouvez explorer et fouiller pour trouver **le fichier caché**  contenant le fameux mot de passe. Il est caché quelque part sur le système de fichiers de l’hôte, à l’endroit où personne ne s’attendrait à ce que vous alliez… sauf si vous avez bien lu la description, bien sûr. 😏
Accédez au répertoire monté et lisez le fichier `.passwd` pour obtenir le précieux **flag** .


```bash
cat /mnt/foo/.passwd
```


### Résultat attendu 🏁 : 



```bash
b95d [......]cc58
```



---



## Conclusion 🎉 

Et voilà ! En profitant du mode `--privileged`** , vous avez réussi à monter le système de fichiers de l'hôte et à récupérer le **flag**  caché dans `/mnt/foo/.passwd`. 🏆
Ce challenge nous rappelle une fois de plus que même en mode conteneurisé, un système mal configuré peut facilement être compromis. Un Docker en mode `--privileged`**  ? C’est comme si vous laissiez une fenêtre ouverte en pleine nuit. 🌙

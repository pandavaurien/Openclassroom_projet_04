# Application gérant un tournoi d'échecs

### Openclassroom projet 04

Projet consistant à créer une application permettant de créer la structure d'un tournoi d'échecs, permettant d'ajouter des joueurs dans une base de données. Le programme utilise un algorithme permettant de calculer la rotation des joueurs afin que les matchs soit équitables et ne se reproduisent pas (algorithme suisse de tournois).

Le programme utilise le design pattern MVC (Modèles - Vues - Controlleurs)

## Prérequis

Le programme utilise plusieurs librairies externes, et modules de Python, qui sont repertoriés dans le fichier ```requirements.txt```

Les modules et librairies externes s'installent via la console en tapant:
```bash
pip 'Nom_du_module'
```

## Démarrage 

Le programme est écrit en Python, copier tous les fichiers et repertoires du repository, et lancer le programme depuis un terminal via la commande :

```bash
python main.py
```

## Rapport flake8

Le repository contient un rapport flake8, qui n'affiche aucune erreur. Il est possible d'en générer un nouveau en installant le module ```flake8``` et en tappant dans le terminal :

```bash
flake8 --exclude=env/ --max-line-length=119

```





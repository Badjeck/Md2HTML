# Site static

## Descritpion

Le programme md2html_converter.py ci-joint, permet de convertir un document rédiger en .md en un document html pour un site static.

## Exigence

Pour que le programme fonctionne, vous aurez besoin de Python 3, ainsi que des librairie os, click, glob, shutil ainsi que mardown2, cette dernière  
n'étant pas compris dans les librairie native de Python 3.

## Telechargement

[Telechargement Python 3](https://www.python.org/downloads/)  
[Telechargement markdown2](https://pypi.org/project/markdown2/)  

La librairie markdown2 pouvant aussi être installé grâce a un terminal via la commande pip : pip install mardown2

## Fonctionnement

Ce programme fonctionne en ligne de commande, lancez le programme via un terminal en entrant le nom de ce dernier précédé de py ou python,
il faut ensuite lui donner les précisions necessaires:
* -i pour préciser le dossier contenant le fichier markdown a convertir
* -o pour préciser le dossier ou sera enregistrer le fichier html (site_statique par defaut)
* -n pour préciser le nom du fichier html (site par defaut) 
* -i pour préciser le dossier contenant les images à transférer avec le mardown


le dossier contenant le site sera présent dans le dossier indiqué contenant le markdown, il contiendra le fichier html du site ainsi qu'un dossier avec vos images du même nom que le dossier image source.

Par exemple :  

py .\md2html_converter.pu -i oui -o Mondossier -monsite  

créera un dossier nommé Mondossier contenant le fichier monsite.html provenant du markdown contenu dans le dossier oui.

from markdown2 import Markdown
import os

# fichier = open("kenny.md","r")

# print(fichier.read())

# print(markdown2.markdown(D:\Workspace\Labopython\kenny.md))
out_file= open("out_file.html","w")
with open("kenny.md","r") as fichier:
    
    oui = Markdown().convert(fichier.read())
    out_file.write(oui)
    
    # print(fichier.read())
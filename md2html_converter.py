from markdown2 import Markdown
import os
import click

@click.command()
@click.option("-i","--input-directory", "--input_directory",default='',help='dossier a convertir')
@click.option("-o","--output-directory","--output_directory",default='site_statique',help='dossier a creer')
@click.option("-n","--website-name","--website_name",default='site',help='nom du site')


def convert(input_directory,output_directory,website_name):
        if os.path.exists(output_directory):
                print("Impossible de créer le dossier : \nLe dossier '{}' existe déjà".format(output_directory))

        else:
                os.mkdir(output_directory)
                out_dir = open("./{}/{}.html".format(output_directory,website_name), "w")
                with open(input_directory,"r") as fichier:
                        out_dir.write('<!DOCTYPE html>\n<head>\n<meta charset="utf-8">\n</head>\n<body>\n')
                        out_dir.write(Markdown().convert(fichier.read()))
                        out_dir.write('\n</body>')


if __name__ == '__main__':
        convert()



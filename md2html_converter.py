from markdown2 import Markdown
import os
import click
import glob

@click.command()
@click.option("-i","--input-directory", "--input_directory",default='',help='dossier a convertir')
@click.option("-o","--output-directory","--output_directory",default='site_statique',help='dossier a creer')
@click.option("-n","--website-name","--website_name",default='site',help='nom du site')


def convert(input_directory,output_directory,website_name):

        if os.path.exists(output_directory):
                print("Impossible de créer le dossier : \nLe dossier '{}' existe déjà".format(output_directory))

        else:
                mdintofolder = False
                while mdintofolder == False:
                        os.chdir(input_directory)
                        mdintofolder = glob.glob('*.md')

                os.mkdir(output_directory)
                out_dir = open("./{}/{}.html".format(output_directory,website_name), "w")
                with open(mdintofolder[0],"r") as fichier:
                        out_dir.write('<!DOCTYPE html>\n<head>\n<meta charset="utf-8">\n</head>\n<body>\n')
                        out_dir.write(Markdown().convert(fichier.read()))
                        out_dir.write('\n</body>')


if __name__ == '__main__':
        convert()
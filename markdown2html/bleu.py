from markdown2 import Markdown
with open("file.htm", 'w') as output_file: 
    output_file.write(Markdown().convert(open("file.md").read()))
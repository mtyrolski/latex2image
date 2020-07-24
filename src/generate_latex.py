import os

def fill_tex_file(expression, filename):
    expression = f'$${expression}$$'
    _DOCUMENT = [R'\documentclass{article}', R'% General document formatting', R'\usepackage[margin=0.7in]{geometry}', R'\usepackage[parfill]{parskip}', R'\usepackage[utf8]{inputenc}',
                 R'% Related to math', R'\usepackage{amsmath,amssymb,amsfonts,amsthm}', R'\thispagestyle{empty}', R'\usepackage{xcolor}', R'\begin{document}', expression, R'\end{document}']

    with open(filename, 'w+') as output:
        output.write('\n'.join(_DOCUMENT))

def process():
    with open('raw_tex.in', 'r') as infile:
        for idx, line in enumerate(infile.readlines()):
            fill_tex_file(line, str(idx)+'.tex')
            os.system(f'pdflatex {idx}.tex > /dev/null 2>&1')
            os.system(f'pdfcrop {idx}.pdf --margins 10 > /dev/null 2>&1')
            os.system(f'pdftoppm {idx}-crop.pdf {idx} -png > /dev/null 2>&1')


if __name__ == "__main__":
    process()

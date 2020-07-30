import os
import argparse

def fill_tex_file(expression, filename, additional_packages, extra_lines):
    expression = f'$${expression.splitlines()[0]}$$'
    _DOCUMENT = [R'\documentclass{article}', R'% General document formatting', R'\usepackage[margin=0.7in]{geometry}', R'\usepackage[parfill]{parskip}', R'\usepackage[utf8]{inputenc}',
                 R'% Related to math', R'\usepackage{amsmath,amssymb,amsfonts,amsthm}', R'\thispagestyle{empty}']
    if additional_packages:
        _DOCUMENT = _DOCUMENT + [fR'\usepackage{{{p}}}' for p in additional_packages]
    
    if extra_lines:
        _DOCUMENT = _DOCUMENT + [e for e in extra_lines]

    _DOCUMENT = _DOCUMENT + [R'\begin{document}', expression, R'\end{document}', '']
    with open(filename, 'w+') as output:
        output.write('\n'.join(_DOCUMENT))

def process(packages, extra):
    with open('raw_tex.in', 'r') as infile:
        for idx, line in enumerate(infile.readlines()):
            fill_tex_file(line, str(idx)+'.tex', packages, extra)
            if len(line.strip()) != 0:
                os.system(f'pdflatex {idx}.tex > /dev/null  2>&1')
                os.system(f'pdfcrop {idx}.pdf --margins 10 > /dev/null 2>&1')
                os.system(f'pdftoppm {idx}-crop.pdf {idx} -png > /dev/null 2>&1')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-p',
                        '--packages',
                        required=False,
                        nargs='+',
                        help='Add packages.')
    
    parser.add_argument('-e',
                        '--extra',
                        required=False,
                        nargs='+',
                        help='Add extra latex line.')

    FLAGS = parser.parse_args()
    process(FLAGS.packages, FLAGS.extra)

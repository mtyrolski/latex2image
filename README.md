# latex2image
Simple but powerful multi-thread latex to image converter. <br>
This readme is related to last stable release v0.2.1: https://github.com/mvxxx/latex2image/releases/tag/v0.2.1
## Usage

### Additional packages
If you want to use additional packages, modify `python_exec.sh` script. Usage of `generator.py`:

```
usage: generate_latex.py [-h] [-p PACKAGES [PACKAGES ...]]
                         [-e EXTRA [EXTRA ...]]

optional arguments:
  -h, --help            show this help message and exit
  -p PACKAGES [PACKAGES ...], --packages PACKAGES [PACKAGES ...]
                        Add packages.
  -e EXTRA [EXTRA ...], --extra EXTRA [EXTRA ...]
                        Add extra latex line.

```

### Input
This command will create `n` parallel tasks
```bash
bash set.sh inputfile_1 inputfile_2 ... inputfile_n
```

where each of `inputfile_i` has format:

```
latex_eq_1
latex_eq_2
latex_eq_3
...
latex_eq_n
```

e.g.
```
\frac{52 + 92}{74}
32
{\color[rgb]{ 1,0,0 } 3c }-{\color[rgb]{ 0,0,1 } \sqrt{ f\left(0\right)-7+yb \cdot 5y \cdot 2d+yx \cdot 6y } }
{\color[rgb]{ 1,0,0 } f\left(F\left(G\left(\frac{ c }{ 1d }\right)\right)\right) }+{\color[rgb]{ 0,0,1 } \left(4b\right) }
{\color[rgb]{ 1,0,0 } \frac{ \left(G\left(3-9\right)\right) }{ bb } }+{\color[rgb]{ 0,0,1 } f\left(yd \cdot 9d+db-6y+f\left(7\right)\right) }
79 - \frac{71 \cdot 95}{91 - 19}
\frac{10 - 4}{56}
```
### Output
#### Labels
`labels.txt` in which j'th line represents `output/eqj.png`.
#### Example images

<p align="center">
  <img src="https://github.com/mvxxx/latex2image/blob/master/example/1.png?raw=true">
</p>

<p align="center">
  <img src="https://github.com/mvxxx/latex2image/blob/master/example/2.png?raw=true">
</p>


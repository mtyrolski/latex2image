# latex2image
Simple but powerful multi-thread latex to image converter.

## Usage
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
\color{ red }{ 1-\left(5\right) }+\color{ blue }{ F\left(F\left(cx\right)\right) }
\color{ red }{ \left(F\left(6c\right)\right) }-\color{ blue }{ F\left(2y\right) }
\color{ red }{ c }-\color{ blue }{ f\left(\left(ax\right)\right) }
\color{ red }{ \sqrt{ 9 } }-\color{ blue }{ 7a }
\color{ red }{ \left(aa-8\right) } \cdot \color{ blue }{ F\left(\int 6y \right) }
79 - \frac{71 \cdot 95}{91 - 19}
\frac{10 - 4}{56}
```

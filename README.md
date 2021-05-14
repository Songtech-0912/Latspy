# Latspy

Latspy is a fork of `latex2sympy` with major alterations. Like latex2sympy, it parses LaTeX math expressions and converts it into the
equivalent SymPy form.

## Getting started

[ANTLR](http://www.antlr.org/) is used to generate the parser. If you don't have it installed, run these commands:

```sh
cd /usr/local/lib
wget https://www.antlr.org/download/antlr-4.9.2-complete.jar
```

Then add these lines to your `.zshrc` (if you use zsh), `.fishrc` if you use the fish shell, or `.bashrc` (if you use bash):

```
export CLASSPATH=".:/usr/local/lib/antlr-4.9.2-complete.jar:$CLASSPATH"
alias antlr4='java -jar /usr/local/lib/antlr-4.9.2-complete.jar'
alias grun='java org.antlr.v4.gui.TestRig'
```

Open a new terminal, then clone the repo.

```sh
git clone https://github.com/Songtech-0912/Latspy.git && cd Latspy/latspy
```

Generate the parser with `antlr` - this is optional but recommended in order to get the most up-to-date parser.

```
antlr4 PS.g4 -o gen
```

Then you can begin using it! Verify that the setup process was successful by running `python process_latex.py`. You should see this as the result:

```sh
e**(2 + 45)
e + 5
e + 5
e
Derivative(x, y)*Integral(x**2*y, y)
Derivative(x, y)*5
Derivative(Integral(x**2, x), x)
Derivative(x, y)*Integral(x**2, x)
Eq(x*y + Derivative(x**2, y), 0)
Eq(x*y + Derivative(x**2, y), 2)
Derivative(x**3, y)
x**3 + Derivative(x**3, y)
Integral(x**2, (y, 2, 5*x))
Integral(x**2, (x, 5*x, 2))
Integral(x**2, x)
-6 + 2*(4*5)
```

## Usage

Latspy works with Python 3 like this:

```python
from latex2sympy.process_latex import process_sympy
process_sympy("\\frac{d}{dx} x^{2}")

# Result => "Derivative(x**2, x)"
```

## Examples

|LaTeX|Image|Generated SymPy|
|-----|-----|---------------|
|`x^{3}`|![](https://latex.codecogs.com/gif.latex?%5CLARGE%20x%5E%7B3%7D)| `x**3`|
|`\frac{d}{dx} |t|x`|![](https://latex.codecogs.com/gif.latex?%5CLARGE%20%5Cfrac%7Bd%7D%7Bdx%7D%20%7Ct%7Cx)|`Derivative(x*Abs(t), x)`|
|`\sum_{i = 1}^{n} i`|![](https://latex.codecogs.com/gif.latex?%5CLARGE%20%5Csum_%7Bi%20%3D%201%7D%5E%7Bn%7D%20i)|`Sum(i, (i, 1, n))`|
|`\int_{a}^{b} \frac{dt}{t}`|![](https://latex.codecogs.com/gif.latex?%5CLARGE%20%5Cint_%7Ba%7D%5E%7Bb%7D%20%5Cfrac%7Bdt%7D%7Bt%7D)|`Integral(1/t, (t, a, b))`|
|`(2x^3 - x + z)|_{x=3}`|![](https://latex.codecogs.com/gif.latex?%5CLARGE%20%282x%5E3%20-%20x%20&plus;%20z%29%7C_%7Bx%3D3%7D)|`z + 51`

## Contributing

Contributors are welcome! Feel free to open a pull request
or an issue.

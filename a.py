from IPython.display import display, Math
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr
import warnings
warnings.filterwarnings('ignore')

x = parse_expr('x')
f = parse_expr('exp(x)')
x0 = 0
n=3

p = sp.series(expr=f, x=x, x0=x0, n=n)
print('Python code '+ str(p))
print('Python latex '+sp.latex(p))
display(Math(sp.latex(p)))
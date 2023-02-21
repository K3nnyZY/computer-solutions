import sympy as sp
import numpy as np

x = sp.symbols('x')
sinc = sp.Piecewise((1, x==0), (sp.sin(x)/x, x!=0))

# Encontrar la séptima derivada de sinc(x)
sinc_7 = sp.diff(sinc, x, 7)

# Encontrar el máximo valor absoluto de sinc_7(x) en el intervalo [-0.2, 0.2]
sinc_7_abs = sp.Abs(sinc_7)
sinc_7_abs_fn = sp.lambdify(x, sinc_7_abs)
max_sinc_7 = max([sinc_7_abs_fn(xi) for xi in np.linspace(-0.2, 0.2, 1001)])

# Imprimir el resultado
print("El máximo valor absoluto de sinc^(7)(x) en el intervalo [-0.2, 0.2] es:", max_sinc_7)

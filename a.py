import sympy
import math
import numpy as np
import matplotlib.pyplot as plt

# Definimos la función f(x) = xln(x)
x = sympy.Symbol('x')
f = x*sympy.log(x)

# Calculamos f'(x) utilizando las fórmulas de diferencias finitas
def progresiva(h):
    return sympy.diff_finite(f, 1, h, 1)

def regresiva(h):
    return sympy.diff_finite(f, 1, -h, 1)

def central(h):
    return sympy.diff_finite(f, 1, h, 2)

# Calculamos f'(1) para diferentes valores de h
h_values = [0.1, 0.05, 0.025, 0.0125, 0.00625]

for h in h_values:
    fp = progresiva(h).evalf()
    fr = regresiva(h).evalf()
    fc = central(h).evalf()
    error_p = fp - math.log(1)
    error_r = fr - math.log(1)
    error_c = fc - math.log(1)
    print(f"h={h:.5f}:\t progresiva={fp:.5f} error={error_p:.5f}\t regresiva={fr:.5f} error={error_r:.5f}\t central={fc:.5f} error={error_c:.5f}")

# Graficamos los errores en función de h
h_values = np.logspace(-4, -1, num=50)
error_progresiva = []
error_regresiva = []
error_central = []

for h in h_values:
    fp = progresiva(h).evalf()
    fr = regresiva(h).evalf()
    fc = central(h).evalf()
    error_p = abs(fp - math.log(1))
    error_r = abs(fr - math.log(1))
    error_c = abs(fc - math.log(1))
    error_progresiva.append(error_p)
    error_regresiva.append(error_r)
    error_central.append(error_c)

plt.loglog(h_values, error_progresiva, label='Progresiva')
plt.loglog(h_values, error_regresiva, label='Regresiva')
plt.loglog(h_values, error_central, label='Central')
plt.xlabel('h')
plt.ylabel('Error')
plt.legend()
plt.show()

# Buscamos el valor de h que minimiza el error
min_index = np.argmin(error_central)
h_min = h_values[min_index]
print(f"h_min = {h_min:.5f}")

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# Definir la función f(x)
x = sp.symbols('x')
f = x*sp.log(x)

# Calcular la derivada de f(x)
df = sp.diff(f, x)

# Definir el valor de x0
x0 = 1

# Calcular f'(x0)
exact = df.subs(x, x0)

# Definir una lista de valores de h
h_values = [0.1,0.001,0.00001,0.0001,0.011]

# Inicializar listas para guardar los errores
error_prog = []
error_reg = []

# Calcular los errores para cada valor de h
for h in h_values:
    # Fórmula de diferencias progresivas
    f_prog = (4*f.subs(x, x0+h) - 3*f.subs(x, x0) - f.subs(x, x0+2*h)) / (2*h)
    error_prog.append(f_prog)

    # Fórmula de diferencias regresivas
    f_reg = (f.subs(x, x0) - 4*f.subs(x, x0-h) + 3*f.subs(x, x0-2*h)) / (2*h)
    error_reg.append(abs(exact - f_reg))

print(error_prog)

# Encontrar el valor de h que minimiza el error
min_error = min(error_prog + error_reg)
min_index = error_prog.index(min_error) if min_error in error_prog else error_reg.index(min_error)
h_min = h_values[min_index]

# Graficar los errores en función de h
plt.loglog(h_values, error_prog, label='Progresivas')
plt.loglog(h_values, error_reg, label='Regresivas')
plt.scatter(h_min, min_error, color='red', label=f'Mínimo error: h={h_min:.2e}')
plt.legend()
plt.xlabel('h')
plt.ylabel('Error absoluto')
plt.title('Errores de las fórmulas de diferencias progresivas y regresivas')
plt.show()

print(f"El valor de f'(1) es: {exact.evalf()}")
print(f"El valor de h que minimiza el error es: {h_min:.2e}")

# # Define una función para calcular las diferencias divididas.
# def calcular_diferencias_divididas(x, y):
#     # Obtiene el número de puntos.
#     n = len(y)
#     # Crea una copia de y para almacenar los coeficientes de las diferencias divididas.
#     coef = y.copy()
#     # Itera sobre todos los niveles de diferencias divididas.
#     for j in range(1, n):
#         # Itera hacia atrás sobre los coeficientes para calcular la diferencia dividida en cada nivel.
#         for i in range(n-1, j-1, -1):
#             # Calcula la diferencia dividida y actualiza el coeficiente correspondiente.
#             coef[i] = (coef[i] - coef[i-1]) / (x[i] - x[i-j])
#     # Devuelve los coeficientes de las diferencias divididas.
#     return coef

# # Define una función para evaluar el polinomio interpolador de Newton en un punto x_eval.
# def evaluar_polinomio_newton(x, y, x_eval):
#     # Calcula los coeficientes de las diferencias divididas.
#     coef = calcular_diferencias_divididas(x, y)
#     # Obtiene el número de puntos.
#     n = len(y)
#     # Inicializa el resultado con el primer coeficiente (y[0]).
#     resultado = coef[0]
#     # Itera sobre todos los coeficientes de las diferencias divididas (excepto el primero).
#     for i in range(1, n):
#         # Inicializa el término actual con el coeficiente de la diferencia dividida.
#         term = coef[i]
#         # Multiplica el término actual por los factores (x_eval - x[j]).
#         for j in range(i):
#             term *= (x_eval - x[j])
#         # Suma el término actual al resultado.
#         resultado += term
#     # Devuelve el valor del polinomio interpolador de Newton en x_eval.
#     return resultado


# x1 = [8.1, 8.3, 8.6, 8.7]
# y1 = [17.56492, 17.56492, 18.50515, 18.82091]
# x_eval1 = 8.4

# x2 = [0.6, 0.7, 0.8, 1.0]
# y2 = [-0.17694460, 0.01375227, 0.22363362, 0.658009197]
# x_eval2 = 0.9

# # Para primer grado
# f1_1 = evaluar_polinomio_newton(x1[:2], y1[:2], x_eval1)
# f1_2 = evaluar_polinomio_newton(x2[:2], y2[:2], x_eval2)

# # Para segundo grado
# f2_1 = evaluar_polinomio_newton(x1[:3], y1[:3], x_eval1)
# f2_2 = evaluar_polinomio_newton(x2[:3], y2[:3], x_eval2)

# # Para tercer grado
# f3_1 = evaluar_polinomio_newton(x1, y1, x_eval1)
# f3_2 = evaluar_polinomio_newton(x2, y2, x_eval2)

# print("Polinomios interpoladores para f(8.4):")
# print(f"Primer grado: {f1_1}")
# print(f"Segundo grado: {f2_1}")
# print(f"Tercer grado: {f3_1}")

# print("\nPolinomios interpoladores para f(0.9):")
# print(f"Primer grado: {f1_2}")
# print(f"Segundo grado: {f2_2}")
# print(f"Tercer grado: {f3_2}")

# def divided_differences(x, y):
#     n = len(x)
#     coef = np.zeros([n, n])
#     coef[:, 0] = y

#     for j in range(1, n):
#         for i in range(n - j):
#             coef[i][j] = (coef[i + 1][j - 1] - coef[i][j - 1]) / (x[i + j] - x[i])

#     return coef[0, :]

# def newton_interpolator(x, x_values, coef):
#     n = len(x_values)
#     x_sym = sp.Symbol('x')
#     polynomial = coef[n - 1]

#     for i in range(n - 1, 0, -1):
#         polynomial = polynomial * (x_sym - x_values[i - 1]) + coef[i - 1]

#     return polynomial

# x1 = np.array([8.1, 8.3, 8.6, 8.7])
# y1 = np.array([17.56492, 17.56492, 18.50515, 18.82091])

# x2 = np.array([0.6, 0.7, 0.8, 1.0])
# y2 = np.array([-0.17694460, 0.01375227, 0.22363362, 0.658009197])

# coef1 = divided_differences(x1, y1)
# coef2 = divided_differences(x2, y2)

# polynomial1 = newton_interpolator(x1, x1, coef1)
# polynomial2 = newton_interpolator(x2, x2, coef2)

# polynomial1_simplified = sp.simplify(polynomial1)
# polynomial2_simplified = sp.simplify(polynomial2)

# display(Latex(f"Polinomio interpolador de Newton para el primer conjunto de puntos: $${sp.latex(polynomial1_simplified)}$$"))

# display(Latex(f"Polinomio interpolador de Newton para el segundo conjunto de puntos: $${sp.latex(polynomial2_simplified)}$$"))



# dydt = lambda t, y: y - t**2 + 1
# d2ydt2 = lambda t, y, yp: yp - 2*t


# y0 = 0.5
# t0 = 0
# h = 0.5
# n = 4

# y = y0
# t = t0

# for _ in range(n):
#     yp = dydt(t, y)
#     ypp = d2ydt2(t, y, yp)
#     y = y + h * yp + 0.5 * h**2 * ypp
#     t += h
#     print(y)


# y, t = sp.symbols('y, t')
# dydt = y - t**2 + 1
# order = 2
# derivative = derivatives(dydt, t, order)

# # Crear funciones de derivadas
# dydt_func = sp.lambdify((t, y), derivative[0])
# d2ydt2_func = sp.lambdify((t, y), derivative[1])

# wi = 0.5
# t0 = 0
# h = 0.5
# n = 4

# for _ in range(n):
#     yp_value = dydt_func(t0, wi)
#     ypp_value = d2ydt2_func(t0, wi)
#     wi = wi + h * (yp_value + h / factorial(2) * ypp_value)
#     t0 += h
#     print(wi)
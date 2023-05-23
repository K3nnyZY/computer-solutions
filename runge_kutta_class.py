import numpy as np

f=  lambda t, y: 2/t*y + t**2*np.exp(t)

h = 0.1; a = 1; b = 2
n = int((b-a)/h)
w_punto = list()
wi = 0
ti = 1

for i in range(1, n+1):
    wi += h*f(ti+h/2,wi+h/2*f(ti,wi))
    w_punto.append(wi)
    ti += h

w_punto = np.array(w_punto)
print(w_punto)
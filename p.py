from numpy import *
import math as mt
import sympy as sp

x= sp.Symbol("x")
f = sp.sin(x)/x

print(cos(0.18)/0.18 - sp.sin(0.18)/0.18**2)

print(-sin(0.18)/0.18 - 2*cos(0.18)/0.18**2 + 2*sin(0.18)/0.18**3)
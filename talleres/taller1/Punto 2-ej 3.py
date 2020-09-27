from sympy import Derivative, diff, simplify, Symbol
from scipy import optimize
import numpy as np
 
def biseccion(f, a, b, tol=1.0e-6):
    if a > b:
        raise ValueError("Intervalo mal definido")
    if f(a) * f(b) >= 0.0:
        raise ValueError("La función debe cambiar de signo en el intervalo")
    if tol <= 0:
        raise ValueError("La cota de error debe ser un número positivo")
    x = (a + b) / 2.0
    while True:
        if b - a < tol:
            return x
        elif np.sign(f(a)) * np.sign(f(x)) > 0:
            a = x
        else:
            b = x
        x = (a + b) / 2.0

x = Symbol('x')
fx = 6+2.13*x**2-0.0013*x**4
dx = Derivative(fx, x).doit()
simplify(dx)
##print(dx) copiar esta funcion en la variable f para hallar el resultado

##cambiar funcion con la funcion que resulte la derivada
f = lambda x: -0.0052*x**3 + 4.26*x
fx= "6+2.13*x**2-0.0013*x**4"
brent = optimize.brentq(f, 1, 50, xtol=2**-90, full_output=False, disp=True)
bscc = biseccion(f, 1, 50)

libres = {"x": brent}
p = eval(fx, {}, libres)
print("El cohete volará a", p,"m con brent")
libres = {"x": bscc}
p = eval(fx, {}, libres)
print("El cohete volará a", p,"m con biseccion")




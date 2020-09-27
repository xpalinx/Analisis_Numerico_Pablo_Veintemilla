import sympy as sp
# Evaluar un polinomio por el metodo de Horner
def Pol(p, x):
    r = 0
    for v in p:
        r = r*x + v
    return r
# Derivada de un polinomio
def dP(p):
    d = []
    n = len(p) - 1
    for i in range(len(p) - 1):
        d.append((n-i)*p[i])
    return d
# Funcion Main

def main():
    x0 = 1 + 1e-11
    p = [1] * 51
    # Segunda Funcion #####
    x = (sp.var('x'))
    Q = ((x**51 - 1)/(x - 1))
    ########################
    print("\nValor de P(x0) con el metodo de Horner = {:.32f} ".format(Pol(p, x0)))
    print("Valor por funcion equivalente:           {:.32f}".format(Q.evalf(subs={x: x0})))
    error = abs(Pol(p,x0) - Q.evalf(subs={x: x0}))
    print("Error: {:.32f}".format(error))
    ########################
    d = dP(p)
    dQ = sp.diff(Q)
    print("\nValor de P'(x) con el metodo de Horner = {:.32f}".format(Pol(d, x0)))
    print("Valor por funcion quivalente:            {:.32f}".format(dQ.evalf(subs={x: x0})))
    error = abs(Pol(d,x0) - dQ.evalf(subs={x: x0}))
    print("Error: {:.32f}".format(error))
    ########################
    d = dP(dP(d))
    d3Q = sp.diff(sp.diff(dQ))
    print("\nValor de P'''(x) con el metodo de Horner = {:.32f}".format(Pol(d, x0)))
    print("Valor por funcion equivalente:             {:.32f}".format(d3Q.evalf(subs={x: x0})))
    error = abs(Pol(d,x0) - d3Q.evalf(subs={x: x0}))
    print("Error: {:.32f}".format(error))
main()

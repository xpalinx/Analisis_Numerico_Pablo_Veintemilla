import matplotlib.pyplot as plt
import numpy as np

#   Programa para comparar la convergencia del metodo de Newton-Horner contra el metodo de Lagurre

# Evaluar el poinomio P con el metodo de Horner
def P(p,x):
    r = p[0]
    for i in range(1,len(p)):
        r = r*x + p[i]
    return r
# Funcion que calcula la raiz por el metodo de Newton-Horner
def NewtonHorner(p,x0,n,tol):
    print("\nMetodo de Newton Horner, tolerancia ",tol)
    x1 = x0
    e = []
    x = [x0]
    it = [0]
    while True:
        #   Primera division sintetica
        a = [p[0]]
        for i in range(1,len(p)):
            a.append(a[i-1]*x1 + p[i])
        p1 = a[- 1]
        del a[-1]
        #   Segunda division sintetica
        b = [a[0]]
        for i in range(1,len(a)):
            b.append(b[i-1]*x1 + a[i])
        p2 = b[-1]
        #   Calculo de la siguiente iteracion
        if p2 != 0:
            x1 = x1 - (p1/p2)
        else:
            x1 = x1 - 1e-32
        x.append(x1)
        error = abs(P(p,x1))
        e.append(error)
        print(it[-1] + 1," x = {:.32f}".format(x1)," e = {:.32f}".format(error))
        if error < tol or it[-1] >= n:
            break
        it.append(it[-1] + 1)
    return x,e,it
# Funcion que calcula la raiz por el metodo de Lagurre
def Laguerre(p,x0,m,tol):
    print("\nMetodo de Lagurre, tolerancia ",tol)
    x1 = x0
    it = [0]
    e = []
    x = [x0]
    while True:
        #   Primera division sintetica
        a = [p[0]]
        for i in range(1,len(p)):
            a.append(a[i-1]*x1 + p[i])
        p1 = a[- 1]
        del a[-1]
        #   Segunda division sintetica
        b = [a[0]]
        for i in range(1,len(a)):
            b.append(b[i-1]*x1 + a[i])
        p2 = b[-1]
        del b[-1]
        #   Tercera division sintetica
        c = [b[0]]
        for i in range(1,len(b)):
            c.append(c[i-1]*x1 + b[i])
        p3 = c[-1]
        #   Calculo de la siguiente iteracion
        n = len(p) - 1
        g = p2 / p1
        h = g**2 - (p3 / p1)
        s = n / (g + np.sign(g)*np.sqrt((n-1)*(n*h - g**2)))
        x1 = x1 - s
        error = abs(P(p,x1))
        e.append(error)
        x.append(x1)
        print(it[-1] + 1," x = {:.32f}".format(x1)," e = {:.32f}".format(error))
        if error < tol or it[-1] >= m:
            break
        it.append(it[-1] + 1)
    return x,e,it
# Funcion con la que se estima la convergencia de los metodos
def convergencia(e):
    de = []
    p = []
    for i in range(1,len(e)):
        de.append(e[i]/e[i-1])
    for i in range(1,len(de)):
        if abs(np.log(de[i-1])) > 1e-32:
            p.append(np.log(de[i])/np.log(de[i-1]))
    return p
# Funcion main
def main():
    # Poloinomio de Prueba
    polinomios = [[1,-5,-9,155,-250]]
    # Otras pruebas (1) x^2 + 2 (raiz imaginaria). (2) x^2-5x+6 (raices cercanas[cambiar valor inicial])
    #polinomios = [[1,0,4],[1,-5,6]]
    x0 = complex(0,1e-32)
    n = 1000
    tol = [1e-8,1e-16,1e-32]
    for p in polinomios:
        for t in tol:
            #   Metodo de Newton-Horner
            x,e,it = NewtonHorner(p,x0,n,t)
            print("P(x*) = {:.32f}".format(P(p,x[-1])))
            plt.plot(it,e,"g")
            con = [convergencia(e)]
            x.clear()
            e.clear()
            it.clear()
            #   Metodo de Laguerre
            x,e,it = Laguerre(p,x0,n,t)
            print("P(x*) = {:.32f}".format(P(p,x[-1])))
            plt.plot(it,e,"r")
            con.append(convergencia(e))
            #   Impresion de los errores
            plt.xlabel("n iteraciones")
            plt.ylabel("error")
            plt.title("error en P(x) con tolerancia {}".format(t))
            plt.grid()
            plt.legend(["NH","Laguerre"])
            plt.show()
            plt.plot(range(1,len(con[0])+1),con[0],"r")
            plt.plot(range(1,len(con[1])+1),con[1],"b")
            plt.xlabel("n")
            plt.ylabel("convergencia")
            plt.title("Estimacion de orden de convergencia")
            plt.grid()
            plt.legend(["NH","Laguerre"])
            plt.show()
main()
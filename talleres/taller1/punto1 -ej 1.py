# Evaluar un polinomio por el metodo de Horner
def Pol(p,x):
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
    x0 = 1
    # p = x^4+2x^3+3x^2+4x+5
    p = [1,2,3,4,5]
    #######################
    print("Derivadas de P(x0) evaluadas en x0 = ",x0)
    #######################
    q = p
    while len(q) > 0:
        q = dP(q)
        print(len(p) - len(q)," P(x0) = {:.32f}".format(Pol(q,x0)))
main()

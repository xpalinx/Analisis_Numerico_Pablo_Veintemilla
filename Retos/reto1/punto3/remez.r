import numpy as np
import math

def listaRaices(g,a,b):
    h= (b-a)/200
    for i in range(0,199):
        izq = a+k*h
        der = izq+h
        if(g(izq)*g(der)) < 0:
            sol:fsolve(g,[izq,der])
            raices[i]=sol
    return raices

def numerosChebyshev(a,b,raices):
    nc=[]
    cont=0
    for i in raices:
        nc[cont]=(1/2*(a+b) + 1/2*(a-b)*cos((2*i+1)/(2*length(racies))*math.pi))
        cont=cont+1
    return nc
        
def remez(f,x,n,a,b):
    racies=listaRaices(f,a,b)
    nCheb=numerosChebyshev(a,b,racies)
    fxCheb=fsolve(e^math.sin(x) - math.cos(x^2))
    for i in range(1, n+2):
        if i%2 == 0:
            mEcuaciones[i,n+2]=e
        else:
            mEcuaciones[i,n+2]=-e
        for j in range(2,n+1):
            mEcuaciones[i,j]=nChen[i]^(j-1)
    solucion=solve(mEcuaciones,fxCheb)


def main():
    print("Hola")
    
main()
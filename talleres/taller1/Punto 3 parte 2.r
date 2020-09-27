#Parte 2
metodoNewton <- function(e,x0, tol,maxiter){
  ed <- D(e,'x')
  g <- function(x) eval(e)
  gd <- function(x) eval(ed)
  
  x=mpfr(x0,128)
  i = 1
  error = 1
  anterior = 1
  
  while(error>tol && i<maxiter){
    x0=x
    x = x0- g(x0)/gd(x0)
    i = i+1
    error = abs(x-anterior)
    anterior=x
  }
  cat("Res: ",formatMpfr(x),'\n')
  return(x)
  
}

metodoNewtonGeneralizado<-function(x0,tol, maxiter){
  f <- function(x) eval(ex2)
  ed<-D(ex2,'x')
  fd<- function(x) eval(ed)
  
  error=1
  x=mpfr(x0,128)
  anterior=mpfr(x0,128)
  i=1
  while(error>tol && maxiter>i){
    x0=mpfr(x,128)
    nom=f(x0)*fd(x0)
    denom=(fd(x0))^2-f(x0)*fd(x0)
    x=x0-(nom/denom)
    error=abs(x-anterior)
    anterior=x
    i=i+1
  }
  cat("Res: ",formatMpfr(x), '\n')
}

resolverAB<-function(c,x){
  b=c+c*exp(c)-3
  a=c-b
  r=a+(x*a+b)*exp(x*a+b)
  cat("c: ",formatMpfr(c), '\n')
  cat("b: ",formatMpfr(b), '\n')
  cat("a: ",formatMpfr(a), '\n')
  cat("Res: ",formatMpfr(r), '\n')
}



metodoNewton(ex1,1,10e-8,100)
resolverAB(metodoNewton(ex2,1,10e-8,100),2)
metodoNewtonGeneralizado(1,10e-16,100)
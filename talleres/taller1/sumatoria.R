library(printr)


convergencia <- function(e,tol){
  de=c()
  p=c()
  for(i in range(2,length(e))){
    de[i-1]=e[i]/e[i-1]
    for(i in range(1, length(de))){
      if (abs(log(de[i-1])) > tol){
        p=c(p,log(de[i])/log(de[i-1]))
      }
    }
  }
 p
}


Sumatoria <-function(incre,nm,tol){
  x<- c()
  y1<- c()
  sy1<- c()
  ite <- c()
  err<- c()
  cont=1

  x[cont]=incre
  y1[cont]=cos(1/cont)
  sy1[cont]=y[cont]
  ite[cont]=cont
  err[cont]=abs(nm-y[cont])
  
  while(nm - y1[cont] > tol){
    cont=cont+1
    ite[cont]=cont
    x=c(x,x[cont-1]+incre)
    y1=c(y1,cos(1/cont))
    sy1=c(sy1,sy1[cont-1]+y1[cont])
    err=c(err,abs(nm-y1[cont])) #errores
  } 

 # res=convergencia(err,tol)
  print("Sumatoria")
  plot(ite,err,type = "l",main = "Convergencia de Cos(1/n)", xlab = "Iteracion", ylab = "Error") #xlim=c(0,10),ylim = c(0.5,10)
  datos <- data.frame("iteracion"= ite,"x" = x,"f(x)" = y1,"Sumatoria"= sy1,"error"= err )
  datos
}

Sumatoria(0.7,1.0,1e-3)

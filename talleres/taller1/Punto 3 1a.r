library(Rmpfr)
options(digits = 22)
ex1 <- (expression)(sin(x)-log(x+2))
ex2 <- (expression)(-x*exp(x)+(x-x*exp(x)+3)*exp(x-x*exp(x)+3)-1)
ex3 <- (expression)(exp(x)-x-1)
#Punto 1.a
soluInter1 <- function(e,x0,x1){
  f <- function(x) eval(e)
  error = 1
  i = 0
  while(error >= 10^(-16)){
    den = f(x1)-f(x0)
    if(den == 0){
      break
    }
    x2 = mpfr(x1 - ((f(x1)*(x1-x0))/den),128)
    cat("Iteracion #", i ,"valor:",formatMpfr(x2),"\n")
    error = abs(x2 - x1)
    x0 = x1
    x1 = x2
    i = i + 1
  }
  val=1.631443596968884822896061387697825694063
}
soluInter1(ex1,0,-0.2)
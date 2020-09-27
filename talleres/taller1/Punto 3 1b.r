#Punto 1.b
soluInter2 <- function(e,x0,x1){
  f <- function(x) eval(e)
  error = 1
  i = 0
  while(error >= 10^(-8)){
    den = f(x1)-f(x0)
    if(den == 0){
      break
    }
    x2 = mpfr(x1 - f(x1)*((x1-x0)/den),128)
    cat("*Iteracion", i ,"resultado:",formatMpfr(x2),"\n")
    error = abs(x2 - x1)
    x0 = x1
    x1 = x2
    i = i + 1
  }
  val=mpfr(1.631443596968884822896061387697825694063,128)
}
soluInter2(ex1,0,-0.2)
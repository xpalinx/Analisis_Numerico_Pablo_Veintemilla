

aitken <-function(x0,x1,x2,tol){
  print("Aitken")
  r=c()
  e=c()
  it=c()
  er=0
  x=0
  xa=0
  while(abs(x2-xa) > tol){
  xa = x2
  x2 = x2-(((x2-x1)**2)/(x2-2*x1+x0))
  print(x2)
  x0 = x1
  x1 = xa
  x= x+1
  er = abs(x2-xa)
  e=c(e,er)
  r=c(r,x2)
  }
  
  datos <- data.frame("error" = e, "valores" = r)
  datos
  plot(e,r)
  
  }

aitken(-63662, 0 , 0.63662, 1e-16)


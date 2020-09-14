evaluate <- function(X, f, P, n_i) {
  summary <- data.frame(matrix(NA, 11, 4))
  colnames(summary) = c("x", "n", "f(x)", "P(x)")
  for(i in 1:11){
    n <- n_i + i - 1
    summary[i, 1] = X
    summary[i, 2] = n
    summary[i, 3] = eval(parse(text=gsub("X", X, f)))
    summary[i, 4] = eval(parse(text=paste0(P, "(", X, ",", n, ")")))
  }
  print(summary)
  par(mfrow=c(1, 2))
  curve(eval(parse(text = gsub("X", "x", f)), envir = list(x = x)),
        from = -1, to = 1, ylab = "f(x)", main = paste("Function =", f))
  y <- ifelse(n_i == 0, 2, 1)
  curve(eval(parse(text = gsub("X", "x", f)), envir = list(x = x)),
        from = -1, to = 1, ylab = "f(x)", 
        main = paste("Taylor Approximation at", X), 
        xlim = (c(X - 0.00000002, X + 0.00000002)), 
        ylim = (c(summary[y, 3] - 0.5, summary[y, 3] + 0.5)))
  points(X, summary[y, 4], col=2, pch=16)
  text(X + 0.25, summary[y, 4], "n=1")
  points(X, summary[(y + 9), 4], col=3, pch=16)
  text(X + 0.25, summary[(y + 9), 4], "n=10")  
  
  
}

reciprocal <- function(x, n) {
  sum((-(cos(x))^2 +sin(x))^(0:n) / factorial(0:n))
}

evaluate(0, "1 / (1 - X)", "reciprocal", 0)
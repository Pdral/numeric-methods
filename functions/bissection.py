def bisseccao(a, b, f, erromax, maxiter=50, iter=0, verro=[]):
    x = (a+b)/2
    iter += 1
    erro = abs((x-a)/x)
    verro.append(erro)
    if erro <= erromax or iter == maxiter or f(x)==0:
      return x, iter, verro
    if f(a)*f(x) < 0:
      return bisseccao(a, x, f, erromax, maxiter, iter, verro)
    return bisseccao(x, b, f, erromax, maxiter, iter, verro)  

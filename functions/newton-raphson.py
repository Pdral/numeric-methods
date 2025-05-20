def newtonraphson(xk, f, g, erromax, maxiter=50, iter=0, verro=[]):
  x = xk - (f(xk)/g(xk))
  erro = abs((x-xk)/x)
  verro.append(erro)
  iter += 1
  if erro <= erromax or iter == maxiter:
    return x, iter, verro
  return newtonraphson(x, f, g, erromax, maxiter, iter, verro)

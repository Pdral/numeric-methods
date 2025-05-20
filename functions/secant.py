def secante(xj, xk, f, erromax, maxiter=50, iter=0, verro=[]):
  x = (xj*f(xk)-xk*f(xj))/(f(xk)-f(xj))
  erro = abs((x-xk)/x)
  verro.append(erro)
  iter += 1
  if erro <= erromax or iter == maxiter:
    return x, iter, verro
  return secante(xk, x, f, erromax, maxiter, iter, verro)

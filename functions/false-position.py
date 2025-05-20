def falsaposicao(a, b, f, erromax, maxiter=50, iter=0, verro=[]):
    x = (a*f(b) - b*f(a))/(f(b)-f(a))
    iter += 1
    erro = abs((x-a)/x)
    verro.append(erro)
    if erro<=erromax or iter==maxiter or f(x)==0:
      return x, iter, verro
    if f(a)*f(x) < 0:
      return falsaposicao(a, x, f, erromax, maxiter, iter, verro)
    return falsaposicao(x, b, f, erromax, maxiter, iter, verro)

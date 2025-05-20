from gaussian-quadrature import quadratura_gaussiana

# Função para calcular uma integral imprópria indo de uma constante positiva à +infinito
def integral_impropria_duplopositivo(g, a):
  return quadratura_gaussiana(g, 0, 1/a) # Para isso, basta realizarmos uma alteração de variável em que 1/x = t
  # e integrarmos de 0 à 1/a

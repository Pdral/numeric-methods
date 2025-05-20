import numpy as np

from repeated-simpson import simpson_repetida

# Função para calcular uma integral dupla
def integral_dupla(f, intervalox, nx, intervaloy, ny):
  Y = np.linspace(intervaloy[0], intervaloy[1], ny)
  X = np.linspace(intervalox[0], intervalox[1], nx)
  integrais = [simpson_repetida([(x, f(x, y)) for x in X]) for y in Y ] 
  # Para cada valor de y, calculamos a integral em x
  pontos = [(Y[i], integrais[i]) for i in range(ny)]
  return simpson_repetida(pontos) # Calculamos a integral em y com os valores obtidos anteriormente

import pandas as pd

from possibility-vector import vetor_possibilidades
from reverse-function import f_inversa

# A função que realiza o método de Descartes propriamente dito.
# OBS: a ordem dos coeficientes será decrescente em todas as funções: [an, an-1, ..., a1, a0]
def regradesinal(coeficientes):
  grau = len(coeficientes)-1

  p = vetor_possibilidades(coeficientes)

  inv_coefic = f_inversa(coeficientes)
  
  n = vetor_possibilidades(inv_coefic)

  possibilidades = []
  for b in p:
    for a in n:
      possibilidade = [b,a]
      possibilidade.append(grau-a-b)
      possibilidades.append(possibilidade)
  return pd.DataFrame(possibilidades, columns=['Positivas', 'Negativas', 'Complexas conjugadas'])

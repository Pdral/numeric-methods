import numpy as np

from find-deltas import encontra_deltas

# Função que realiza o método de Bairstow propriamente dito.
def bairstow(coefic, r, s, erromax):
  x = []
  grau = len(coefic)-1
  while(grau>2):
    r, s, coefic = encontra_deltas(coefic, r, s, erromax, grau)
    delta = r**2 + 4*s
    if delta>=0:
      raiz_delta = np.sqrt(delta)
    else:
      raiz_delta = complex(0,np.sqrt(-1*delta))
    x.append((r + raiz_delta)/2)
    x.append((r - raiz_delta)/2)
    grau = len(coefic)-1
  if grau == 2:
    delta = coefic[1]**2 - 4*coefic[0]*coefic[2]
    if delta >= 0:
      raiz_delta = np.sqrt(delta)
    else:
      raiz_delta = complex(0,np.sqrt(-1*delta))
    x.append((-coefic[1] + raiz_delta)/2*coefic[0])
    x.append((-coefic[1] - raiz_delta)/2*coefic[0])
  else:
    x.append(-coefic[1]/coefic[0])
  return x

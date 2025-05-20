import numpy as np
import matplotlib.pyplot as plt

# Função para plotar o gráfico com as splines quadráticas
def plota_spline_quadratica(coefic, x):
  n = len(x)
  for i in range(n-1):
    if i == 0:
      X = np.linspace(x[i],x[i+1],100)
      y = coefic[0]*X + coefic[1]
    else:
      new_X = np.linspace(x[i],x[i+1],100)
      X = np.concatenate((X, new_X))
      vec = coefic[3*i-1]*(new_X**2) + coefic[3*i]*new_X + coefic[3*i+1]
      y = np.concatenate((y, vec))
  plt.grid()
  plt.plot(X, y)

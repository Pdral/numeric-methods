import numpy as np
import matplotlib.pyplot as plt

# Função para plotar o gráfico com as splines cúbicas
def plota_spline_cubica(coefic, x):
  n = len(x)
  for i in range(n-1):
    if i == 0:
      X = np.linspace(x[i],x[i+1],100)
      y = coefic[0]*(X**3) + coefic[1]*(X**2) + coefic[2]*X + coefic[3]
    else:
      new_X = np.linspace(x[i],x[i+1],100)
      X = np.concatenate((X, new_X))
      vec = coefic[4*i]*(new_X**3) + coefic[4*i + 1]*(new_X**2) + coefic[4*i + 2]*new_X + coefic[4*i + 3]
      y = np.concatenate((y, vec))
  plt.grid()
  plt.plot(X, y)

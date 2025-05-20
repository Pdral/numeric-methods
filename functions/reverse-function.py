import numpy as np

# Função responsável por calcular o resultado dos coeficientes ao substituir x por -1.
def f_inversa(coeficientes):
  coeficientes = np.array(coeficientes)[::-1]
  coefic = [(-1)**i * coeficientes[i] for i in range(len(coeficientes))]
  return np.array(coefic)[::-1]

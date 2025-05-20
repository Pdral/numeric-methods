import numpy as np

# Função para calcular o resíduo
def residuo(A, x, B):
  # A é a matriz de coeficientes do sistema, x é o vetor solução obtido por algum dos métodos e B é o vetor de termos independentes dos sistema
  return np.dot(A, x) - B

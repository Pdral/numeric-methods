import numpy as np

# Função para transformar uma matriz triangular superior em uma triangular inferior
def inverte_matriz(A):
  # A é uma matriz triangular superior
  new_A = []
  for array in A[::-1]: # Inverte a ordem das linhas de A
    new_A.append(array[::-1]) # Inverte a ordem dos elementos de cada linha de A
  return np.array(new_A)

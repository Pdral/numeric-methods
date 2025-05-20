import numpy as np

# Função para solucionar um sistema em que a matriz de coeficientes é do tipo triangular inferior
def sol_triang_inf(A, B):
  # A é uma matriz triangular inferior e B um vetor com os termos independentes do sistema
  n = len(B)
  X = []
  for line in range(n):
    b = B[line]
    for column in range(line):
      b -= A[line][column]*X[column]
    x = b/A[line][line]
    # Obtemos os valores de X por substiruições recursivas
    X.append(x)
  return np.array(X)
  # Retornamos o vetor X

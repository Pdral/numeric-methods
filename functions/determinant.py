import numpy as np

def determinante(A):
  # A é uma matriz quadrada 
  det = 0
  n = len(A)
  A = A.astype(np.float64) # Definindo o tipo dos dados como ponto flutuante, para ser possível operar sobre um vetor inteiro de uma só vez
  if n == 2:
    det = A[0][0]*A[1][1] - A[0][1]*A[1][0]
    # Fórmula para o cálculo do determinante de uma matriz quadrada de ordem 2
  else:
    for i in range(n):
      B = np.copy(A)
      B = np.delete(B, 0, 0)
      B = np.delete(B, i, 1)
      det += ((-1)**i)*A[0][i]*determinante(B)
      # Cálculo do determinante através do teorema de laplace recursivamente
  return det

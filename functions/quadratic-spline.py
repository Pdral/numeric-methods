import numpy as np

# Função para criar as matrizes do sistema linear obtido 
def spline_quadratica(x, fx):
  n = len(x) # Número de pontos
  ordem_matriz = 3*n-4
  A = np.zeros((ordem_matriz, ordem_matriz)) # inicializamos a matriz contendo apenas zeros

  # Condições de continuidade nos nós internos
  A[0][0] = x[1]
  A[0][1] = 1
  for i in range(n-3):
    coluna = 3*i+2
    linha = 2*i+1
    A[linha][coluna] = x[i+1]**2
    A[linha][coluna+1] = x[i+1]
    A[linha][coluna+2] = 1
    A[linha+1][coluna] = x[i+2]**2
    A[linha+1][coluna+1] = x[i+2]
    A[linha+1][coluna+2] = 1
  A[2*n-5][ordem_matriz-3] = x[n-2]**2
  A[2*n-5][ordem_matriz-2] = x[n-2]
  A[2*n-5][ordem_matriz-1] = 1

  # Condições de continuidade nos nós externos
  A[2*n-4][0] = x[0]
  A[2*n-4][1] = 1
  A[2*n-3][ordem_matriz-3] = x[n-1]**2
  A[2*n-3][ordem_matriz-2] = x[n-1]
  A[2*n-3][ordem_matriz-1] = 1

  # Continuidade das derivadas nos nós internos 
  j = -1
  for i in range(2*n-2, ordem_matriz):
    if j >=0:
      A[i][j] = 2*x[(j+4)//3]
    A[i][j+1] = 1
    A[i][j+3] = -2*x[(j+4)//3]
    A[i][j+4] = -1
    j +=3

  # Definindo o vetor de termos independentes
  B = np.zeros(ordem_matriz)
  for i in range(2*n-4):
    B[i] = fx[(i//2)+1]
  B[2*n-4] = fx[0]
  B[2*n-3] = fx[n-1]
  return A, B

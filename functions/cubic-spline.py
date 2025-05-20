import numpy as np

# Função para criar as matrizes do sistema linear obtido 
def spline_cubica(x, fx):
  n = len(x)
  ordem_matriz = 4*n-4
  A = np.zeros((ordem_matriz, ordem_matriz))
  B = np.zeros(ordem_matriz)

  # Condições de continuidade nos nós internos
  for i in range(n-2):
    coluna = 4*i
    linha = 2*i
    A[linha][coluna] = x[i+1]**3
    A[linha][coluna+1] = x[i+1]**2
    A[linha][coluna+2] = x[i+1]
    A[linha][coluna+3] = 1
    B[linha] = fx[i+1]
    A[linha+1][coluna+4] = x[i+1]**3
    A[linha+1][coluna+5] = x[i+1]**2
    A[linha+1][coluna+6] = x[i+1]
    A[linha+1][coluna+7] = 1
    B[linha+1] = fx[i+1]

  # Condições de continuidade nos nós externos
  A[2*n-4][0] = x[0]**3
  A[2*n-4][1] = x[0]**2
  A[2*n-4][2] = x[0]
  A[2*n-4][3] = 1
  B[2*n-4] = fx[0]
  A[2*n-3][ordem_matriz-4] = x[n-1]**3
  A[2*n-3][ordem_matriz-3] = x[n-1]**2
  A[2*n-3][ordem_matriz-2] = x[n-1]
  A[2*n-3][ordem_matriz-1] = 1
  B[2*n-3] = fx[n-1]

  # Continuidade das primeiras derivadas nos nós internos 
  j = 0
  for i in range(2*n-2, 3*n-4):
    A[i][j] = 3*x[(j//4)+1]**2
    A[i][j+1] = 2*x[(j//4)+1]
    A[i][j+2] = 1
    A[i][j+4] = -3*x[(j//4)+1]**2
    A[i][j+5] = -2*x[(j//4)+1]
    A[i][j+6] = -1
    j += 4

  # Continuidade das primeiras derivadas nos nós internos 
  j = 0
  for i in range(3*n-4, 4*n-6):
    A[i][j] = 6*x[(j//4)+1]
    A[i][j+1] = 2
    A[i][j+4] = -6*x[(j//4)+1]
    A[i][j+5] = -2
    j += 4

  # Segundas derivadas nos nós extremos
  A[4*n-6][0] = 6*x[0]
  A[4*n-6][1] = 2
  A[4*n-5][ordem_matriz-4] = 6*x[n-1]
  A[4*n-5][ordem_matriz-3] = 2
  return A, B

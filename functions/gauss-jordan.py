import numpy as np

from pivot import pivot

# Método de Gauss-Jordan
def gauss_jordan(A, B, pivotar=False):
  # A é a matriz de coeficientes do sistema, b um vetor com os termos independentes do sistema e pivotar é uma variável que indica se deve ou não se utilizada
  # a estratégia de pivoteamento simples 
  n = len(A)
  A = A.astype(np.float64) 
  B = B.astype(np.float64)
  # Definindo o tipo dos dados como ponto flutuante, para ser possível operar sobre um vetor inteiro de uma só vez
  inversa = np.identity(n) # Inicializando a matriz inversa de A como a identidade de ordem n
  for j in range(n): # Itera sobre as colunas de A
    if pivotar:
      A, B = pivot(A, B, j)
    else: 
      inversa[j] = inversa[j]/A[j][j] # Só faz sentido calcular a inversa se não houver pivoteamento
    B[j] = B[j]/A[j][j]
    A[j] = A[j]/A[j][j]
    # Definindo o termo da diagonal pertencente a linha j igual a 1
    for i in range(n): # Itera sobre as linhas de A
      if i != j:
        B[i] = B[i] - B[j]*A[i][j]
        inversa[i] = inversa[i] - inversa[j]*A[i][j]
        A[i] = A[i] - A[j]*A[i][j]
        # Definindo os termos que não são da dioganal principal pertencentes à coluna j iguais a 0
  if pivotar:
    return B
  return B, inversa # Retorna o vetor B (que é igual a X) e a matriz inversa obtida, se não for realizado pivoteamento

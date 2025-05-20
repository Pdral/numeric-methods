import numpy as np

from pivot import pivot
from sol-triang-sup import sol_triang_sup

# Método de Gauss
def gauss(A, b, pivotar=False, returnL = False):
  # A é a matriz de coeficientes do sistema, b um vetor com os termos independentes do sistema, pivotar é uma variável que indica se deve ou não se utilizada
  # a estratégia de pivoteamento simples e returnL indica se devem ser retornadas as matrizes L e U para o método LU
  n = len(A)
  A = A.astype(np.float64) 
  b = b.astype(np.float64)
  # Definindo o tipo dos dados como ponto flutuante, para ser possível operar sobre um vetor inteiro de uma só vez
  B = np.copy(b) # Criando uma cópia do vetor B para não alterar o original
  if returnL:
    L = np.identity(n)
  for j in range(n-1): # Itera sobre as colunas de A, exceto a última
    if pivotar:
      A, B = pivot(A, B, j)
    for i in range(j+1,n): # Itera sobre as linhas de A a partir de j+1
      fator = A[i][j]/A[j][j]
      B[i] = B[i] - B[j]*fator # Onde B[i] e B[j] são reais
      A[i] = A[i] - A[j]*fator # Onde A[i] e A[j] são vetores
      if returnL:
        L[i][j] = fator
  if returnL:
    return L, A # Retorna as matrizes L e U se returnL = True
  return sol_triang_sup(A, B) # Retorna a solução do sistema se returnL = False

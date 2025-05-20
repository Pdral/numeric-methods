import numpy as np

# Função para realizar o pivoteamento de uma coluna
def pivot(A, B, n):
  # A é a matriz de coeficientes do sistema, B um vetor com os termos independentes do sistema e n a coluna à qual será aplicado o pivoteamento
  index_pivo = abs(A[n:,n]).argsort()[-1] + n
  # Encontra a linha do elemento de maior módulo da coluna n buscando a partir da linha n
  aux = np.copy(A[n])
  A[n] = A[index_pivo]
  A[index_pivo] = aux
  # Troca a linha n e a linha com o novo pivô
  aux = B[n]
  B[n] = B[index_pivo]
  B[index_pivo] = aux
  # Aplica a mesma troca ao vetor B
  return A, B # Retorna a matriz A e o vetor B modificados

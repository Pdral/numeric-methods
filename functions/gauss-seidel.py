import numpy as np

# Método de Gauss-Seidel
def gauss_seidel(A, B, erromax, maxiter=50, X=np.zeros(3), iter=0):
  # A é a matriz de coeficientes do sistema, B um vetor com os termos independentes do sistema, erromax é o erro máximo tolerado, maxiter é o maior numero
  # de iterações permitido, X é o vetor solução atual e iter é o número de iterações realizadas
  A = A.astype(np.float64)
  B = B.astype(np.float64)
  # Definindo o tipo dos dados como ponto flutuante, para ser possível operar sobre um vetor inteiro de uma só vez
  n = len(A)
  if X.all() == 0:
    X = np.copy(B)
  X_antigo = np.copy(X)
  for i in range(n):
    X[i] = (-np.dot(A[i], X.T) + A[i][i]*X[i] + B[i])/A[i][i]
    # Calculando os novos valores de X, utilizando o vetor X já atualizado
  erro = max(abs(X_antigo - X))/max(abs(X)) # Calculando o erro obtido
  iter+=1
  if erro <= erromax or iter == maxiter:
    return X, iter # Retorna o vetor X que obteve erro tolerável ou foi obtido após o número máximo de iterações e o número de iterações realizadas
  return gauss_seidel(A, B, erromax, maxiter, X, iter) # Chama a própria função recursivamente caso os critérios de parada não tenham sido atingidos

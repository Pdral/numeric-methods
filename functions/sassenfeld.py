import numpy as np

def sassenfeld(A)
  A = A.astype(np.float64)
  A = abs(A)
  n = len(A)
  B = np.ones(n)
  for i in range(n):
    B[i] = (np.dot(A[i], B) - A[i][i]*B[i])/A[i][i]
  beta = max(B)
  if beta < 1:
    print('Critério cumprido')
  else:
    print('Critério não cumprido')

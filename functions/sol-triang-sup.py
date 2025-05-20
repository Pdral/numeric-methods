from sol-triang-inf import sol_triang_inf
from matrix-inversor import inverte_matriz

# Função para solucionar um sistema em que a matriz de coeficientes é do tipo triangular superior
def sol_triang_sup(A,B):
  # A é uma matriz triangular superior e B um vetor com os termos independentes do sistema
  A = inverte_matriz(A) # Transforma A em uma matriz triangular inferior
  B = B[::-1] # Inverte o vetor B
  return sol_triang_inf(A,B)[::-1] # Soluciona o sistema obtido e inverte os valores de X obtidos

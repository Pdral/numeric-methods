# Método de 1/3 de Simpson repetida
def simpson_repetida(pontos):
  # Pontos é uma lista de tuples, onde cada tuple representa o par ordenado (x, f(x))
  n = len(pontos)
  resp = 0
  for i in range(n):
    if i == 0 or i == n-1:
      fator = 1
    elif i % 2 == 0:
      fator = 2
    else:
      fator = 4
    resp += fator*pontos[i][1]
  return (pontos[n-1][0]-pontos[0][0])*resp/(3*(n-1))

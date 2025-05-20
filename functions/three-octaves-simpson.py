# Método de 3/8 de Simpson simples
def tresoitavossimpson(pontos):
  # Pontos é uma lista de tuples, onde cada tuple representa o par ordenado (x, f(x))
  return (pontos[3][0]-pontos[0][0])*(pontos[0][1] + 3*pontos[1][1] + 3*pontos[2][1] + pontos[3][1])/8

# Método da quadratura gaussiana para 3 pontos
def quadratura_gaussiana(f, a, b):
  # Onde f é a função a ser integrada, a é o limite inferior e b o superior
  t = [-0.7746, 0, 0.7746]
  A = [0.5556, 0.8889, 0.5556]
  # Parâmetros normalizados
  resp = 0
  for i in range(3):
    x = ((b-a)*t[i]+a+b)/2 # Convertendo para o intervalo [a,b]
    resp += A[i]*f(x)
  return (b-a)*resp/2

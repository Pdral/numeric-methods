from repeated-simpson import simpson_repetida
from three-octaves-simpson import tresoitavossimpson
from trapezium import trapezio

# Função para calcular de maneira otimizada a integral entre os pontos fornecidos
def newton_cotes(pontos):
  n = len(pontos)
  resp = 0
  i = 0 # i é a variável que representa o menor ponto do intervalo analisado na iteração atual
  while(i<n-1): # De acordo com a definição de i descrita acima, não faz sentido i = n-1, já que pontos[n-1] é o último elemento da lista
    j = i+1 
    count = 1
    # j é uma variável utilizada para contar, juntamente com count, quantos intervalos consecutivos possuem o mesmo tamanho
    # Dessa forma, j representa o menor valor do próximo intervalo e o laço a seguir testa se tal intervalo possui o mesmo tamanho do atual
    while j < n-1 and pontos[j+1][0]-pontos[j][0] == pontos[i+1][0]-pontos[i][0]:
      count += 1
      j += 1
    if count % 2 == 0:
      # Se o número de intervalos consecutivos de mesmo comprimento for par, podemos utilizar o método de 1/3 de Simpson repetido
      resp += simpson_repetida(pontos[i:i+count+1])
    elif count == 3:
      # Se o número de intervalos consecutivos de mesmo comprimento for 3, podemos utilizar o método de 3/8 de Simpson 
      resp += tresoitavossimpson(pontos[i:i+count+1])
    elif count > 3:
      # Se o número de intervalos consecutivos de mesmo comprimento for ímpar e maior que 3, podemos utilizar 
      # O método de 1/3 de Simpson repetido em todos os intervalos menos nos 3 últimos, nos quais vamos utilizar o método de 3/8 de Simpson
      resp += simpson_repetida(pontos[i:i+count-2]) + tresoitavossimpson(pontos[i+count-2:i+count+1])
      # Também é possível utilizar o método de 1/3 de Simpson repetido nos count-1 intervalos e o método do trapézio no último, 
      # porém foi escolhido o método acima, uma vez que o método de 3/8 de Simpson é mais preciso que o do trapézio
    else:
      # Se não houver nenhum intervalo subsequente de mesmo tamanho do atual, devemos aplicar o método do trapézio
      resp += trapezio(pontos[i][0], pontos[i][1], pontos[i+1][0], pontos[i+1][1])
    i += count # A variável i é atualizada para o menor valor do próximo intervalo com tamanho diferente do atual
  return resp

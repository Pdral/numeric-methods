# Função responsável por calcular os valores de p e n.
def vetor_possibilidades(coeficientes):
  v = 0
  coefic = [a for a in coeficientes if a != 0]
  tamanho = len(coefic)
  for i in range(tamanho-1):
    if coefic[i]*coefic[i+1]<0:
      v += 1
  return [i for i in range(v+1) if (v-i)%2==0]

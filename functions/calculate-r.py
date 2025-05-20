import numpy as np

# Função para calcular o raio da circunferência na qual encontram-se todas as raízes
def calcula_r(coeficientes):
  an = coeficientes[0]
  coefic = np.array(coeficientes)[1:]
  candidatos = [ai/an for ai in coefic]
  r = 1 + max(candidatos)
  return r

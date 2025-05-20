import itertools
def regradesinal(parametros):
  v = 0
  tamanho = len(parametros)
  for i in range(0, tamanho-1):
    x = i+1
    while(parametros[x]==0 and x<tamanho):
      x += 1
    if parametros[i]*parametros[x]<0:
      v += 1
  if v % 2 == 0:
    p = list(range(0,v+1,2))
  else:
    p = list(range(1,v+1,2))

  if tamanho % 2 == 0:
    for i in range(0, tamanho, 2):
      parametros[i]=-parametros[i]
  else:
    for i in range(1,tamanho,2):
      parametros[i]=-parametros[i]
  
  v=0
  for i in range(0, tamanho-1):
    x = i+1
    while(parametros[x]==0 and x<tamanho):
      x += 1
    if parametros[i]*parametros[x]<0:
      v += 1
  if v % 2 == 0:
    n = list(range(0,v+1,2))
  else:
    n = list(range(1,v+1,2))
  return p, n

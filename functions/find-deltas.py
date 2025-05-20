import numpy as np

# Função para encontrar os b's e c's para os quais |delta_r/r| e |delta_s/s| está dentro da tolerância desejada.
def encontra_deltas(coefic, r, s, erromax, grau):
  b = [coefic[0],coefic[1] + r*coefic[0]]
  for i in range(2, grau+1):
    b.append(coefic[i] + r*b[i-1] + s*b[i-2])
  c = [b[0], b[1] + r*b[0]]
  for i in range(2, grau):
    c.append(b[i] + r*c[i-1] + s*c[i-2])
  c.append(0)
  b_inv = np.array(b)[::-1]
  c_inv = np.array(c)[::-1]
  if c_inv[3] != 0:
    delta_r = (-b_inv[0] + (c_inv[2]*b_inv[1])/c_inv[3])/(c_inv[1]-(c_inv[2]**2/c_inv[3]))
    delta_s = (-b_inv[1] - c_inv[2]*delta_r)/c_inv[3]
  else:
    delta_r = -b_inv[1]/c_inv[2]
    delta_s = (-b_inv[0] - c_inv[1]*delta_r)/c_inv[2]
  # Se tanto c2 quanto c3 forem iguais a 0, o sistema é indeterminado.
  r += delta_r
  s += delta_s
  if abs(delta_r/r) <= erromax and abs(delta_s/s) <= erromax:
    return r, s, b[0:len(b)-2]
  return encontra_deltas(coefic, r, s, erromax, grau)

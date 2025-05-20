import numpy as np
import matplotlib.pyplot as plt

def plotagrafico(f, xmin, xmax, niter):
  x = np.linspace(xmin,xmax,niter)
  y = f(x)
  plt.grid()
  plt.plot(x, y)

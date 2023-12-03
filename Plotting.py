import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import Rectangle

def Plotting(corr_map, mode = '2D'):
  if mode == '2D':
    plt.imshow(corr_map, cmap='cividis', interpolation='nearest')
    plt.colorbar()
    plt.show()
  elif mode == '3D':
    x = np.arange(corr_map.shape[1])
    y = np.arange(corr_map.shape[0])
    X, Y = np.meshgrid(x, y)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection = '3d')
    surf = ax.plot_surface(X, Y, corr_map, cmap='hot')
    fig.colorbar(surf)
    plt.show()
  else:
    raise Exception("Invalid mode.")

def plotBox(corr_map, scene, slidingMat, threshold):
  BIASx, BIASy = 26, 20
  h1, w1 = slidingMat.shape
  fig, ax = plt.subplots()
  indices = [(i, j) for i in range(corr_map.shape[0]) for j in range(corr_map.shape[1]) if round(corr_map[i, j]) >= threshold]
  print(len(indices))
  plt.imshow(scene,cmap = 'cividis', interpolation = 'nearest',)
  plt.colorbar()

  for(i,j) in indices:
    plt.plot([j-(j+w1-j+1)//2+BIASx, j+w1, j+w1, j-(j+w1-j+1)//2+BIASx, j-(j+w1-j+1)//2+BIASx], [i - ((i+h1-i+1)//2)+BIASy, i - ((i+h1-i+1)//2)+BIASy, i+h1, i+h1, i - ((i+h1-i+1)//2)+BIASy],'r')
  plt.show()
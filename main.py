import os
import numpy as np
from PIL import Image
from time import time

from CrossCorrealtion import *
from Plotting import *

E_THRESHOLD = 6.75*10e6
O_THRESHOLD = 6*10e6

path = os.getcwd()
dataPath = os.path.join(path, "data")

ImgFile = ["Scene", "letter_e", "letter_o"]
fileExten = ".bmp"

DataArray = [np.mean(np.asarray(Image.open(os.path.join(dataPath, i + fileExten))),axis = 2) for i in ImgFile]

for i in DataArray:
  plt.imshow(i)
  plt.show()
  
corr_e = matched_filter(DataArray[0], DataArray[1], 0)
Plotting(corr_e, '2D')
Plotting(corr_e, '3D')

plotBox(corr_e, DataArray[0], DataArray[1], E_THRESHOLD)
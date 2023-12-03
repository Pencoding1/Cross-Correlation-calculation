import os
import time
import numpy as np
import scipy as sci
import matplotlib.pyplot as plt

from PIL import Image
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import Rectangle
from numpy.fft import fft2, ifft2, fftshift

def matched_filter(scene, template, thershold):
  t_rows, t_cols = template.shape
  
  correlation_map = np.zeros((scene.shape[0] - t_rows + 1, scene.shape[1] - t_cols + 1)) # Tạo mảng chứa kết quả khi tính tương quan

  for i in range(correlation_map.shape[0]):
    for j in range(correlation_map.shape[1]):
      w = scene[i:i+t_rows, j:j+t_cols] # tạo cửa sổ trượt
      
      correlation = np.sum(w * template) if np.sum(w * template) > thershold else 0 # Chỉ nhận các giá trị tương quan lớn hơn một ngưỡng nhất định (dùng để xác định ngưỡng cần tìm)
      
      correlation_map[i, j] = correlation

  return correlation_map


def FFTmatched_filter(bigMat, slidingMat, mode=1):
  if mode == 1:
    corr = sci.signal.fftconvolve(bigMat, np.flip(slidingMat))
    return corr
  elif mode == 2:
    h1, w1 = bigMat.shape
    h2, w2 = slidingMat.shape
    padded_template = np.zeros_like(bigMat)
    padded_template[:h2, :w2] = slidingMat # Thêm các cột và dòng 0 để đảm bảo shape của template = với shape của scene

    fftB = fft2(bigMat) # Biến đổi Fourier trên scene
    fftS = fft2(padded_template) # Biến đổi Fourier trên template

    corr = fftB * np.conjugate(fftS) # tính tương quan theo công thức f(x) * g(x) = IFFT(FFT(f(x) * FFT(g(x))))
    return np.real(ifft2(corr)) # Loại bỏ các giá trị ảo trong ma trận tương quan
  else:
    raise Exception("Invalid mode.")
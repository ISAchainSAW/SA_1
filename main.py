import copy

import matplotlib.pyplot as plt
import numpy as np
from pyemd import emd
from scipy.interpolate import splev, splrep
from scipy.signal import find_peaks
from func import invert, peak

data = [85.8, 85.64, 85.38, 85.54, 84.71, 84.86, 84.28, 83.59, 82.76, 82.96, 83.04, 82.98, 83.45, 83.74, 83.7, 83.65,
        83.91, 83.91, 83.1, 83.44, 83.56, 83.02, 82.83, 82.87, 82.84, 82.32, 82.51, 81.06, 80.58, 80.52, 80.92, 81.07,
        81.44, 81.87, 82.35, 82.41, 82.92, 83.09, 82.94, 82.98, 83.29, 83.29]
data2 = []  # Отрицательные значения
h = []
Flag = True
c = []
r = []

data2 = invert(data)
h, xx = peak(data, data2, False)
while (Flag):
    h, xx = peak(h, data2, False)
    data2 = invert(h)
    print(xx)
    if xx < 0.1:
        c = h.copy()
        Flag = False


for i in range(len(data)):
    r.append(data[i]-c[i])
plt.figure(1)
plt.title('c')
plt.plot(c, color="red")  # high frquency
plt.figure(2)
plt.title('r')
plt.plot(r, color="black")  # low frquency
plt.grid()
plt.show()


#r - новая функция, засунуть в peak и т.д., пока не станет монотонной

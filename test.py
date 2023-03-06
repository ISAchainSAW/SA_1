import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import splev, splrep
x = np.linspace(0,10,5) # Создать случайные точки
y = np.sin(x) # Заполнить точки значениями
spl = splrep(x, y)
x2 = np.linspace(0,10,200) # Создать набор точек на участке (0-10) в кол-ве 200 штук
y2 = splev(x2, spl) #Заполнить точки значениями, на основании уже созданных точек
plt.plot(x, y, 'o', x2, y2)
print(x)




#Снизу 2 точки, сверху 3
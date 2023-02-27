from scipy.interpolate import splev, splrep
from scipy.signal import find_peaks
import numpy as np
import matplotlib.pyplot as plt


def invert(data):
    dat2 = []
    for i in data:
        dat2.append(i * -1)
    return dat2


def peak(data, data2, flag):
    dd = []  # Индексы значений
    ddd = []  # Значения
    zz = []
    zzz = []
    # Найти пики
    for i in find_peaks(data2):
        for j in i:
            zz.append(j)

    # Взять значение пиков
    for i in range(len(data2)):
        for j in zz:
            if i == j:
                zzz.append(data[i])
    # Найти пики
    for i in find_peaks(data):
        for j in i:
            dd.append(j)

    # Взять значение пиков
    for i in range(len(data)):
        for j in dd:
            if i == j:
                ddd.append(data[i])
    # Сплайны
    spl = splrep(dd, ddd)
    x1 = np.linspace(0, 41, 42)
    y1 = splev(x1, spl)
    spl2 = splrep(zz, zzz)
    x2 = np.linspace(0, 41, 42)
    y2 = splev(x2, spl2)

    # Линия тренда
    m = []  # Средняя
    for i, j in zip(y1, y2):
        m.append((i + j) / 2)

    # Приближение
    h1 = []  # Приближение
    for i in range(len(data)):
        h1.append(data[i] - m[i])

    if flag == True:
        # Строим график
        plt.figure(1)
        plt.plot(data, color="red")  # data
        plt.plot(x1, m, color="blue", )  # avg
        plt.plot(x1, y1, color='black', )  # spline
        plt.plot(x2, y2, color='black', )  # spline
        plt.plot([dd], [ddd], color='blue', marker='o')  # max
        plt.plot([zz], [zzz], color='green', marker='o')  # min
        plt.legend(['data', 'avg', 'interpolate_max', 'interpolate_min', 'max_peak', 'min_peak'])
        plt.figure(2)
        plt.plot(h1, color="blue", )
        plt.grid()
        plt.show()

    tmp = 0  # Дельта
    for i in range(len(data)):
        # print(h1[i],data[i])
        tmp += (abs(h1[i] - data[i]) ** 2 / data[i] ** 2)
    return h1, tmp

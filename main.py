import matplotlib.pyplot as plt
from func import invert, peak
from Scrap import pay as data


# data = [85.8, 85.64, 85.38, 85.54, 84.71, 84.86, 84.28, 83.59, 82.76, 82.96, 83.04, 82.98, 83.45, 83.74, 83.7, 83.65,
#         83.91, 83.91, 83.1, 83.44, 83.56, 83.02, 82.83, 82.87, 82.84, 82.32, 82.51, 81.06, 80.58, 80.52, 80.92, 81.07,
#         81.44, 81.87, 82.35, 82.41, 82.92, 83.09, 82.94, 82.98, 83.29, 83.29]
def end(data):
    flag = True
    c = []  # Высокочастотная функция
    r = []  # Остаток -> новые данные
    data2 = invert(data)  # Отрицательные значения
    h, xx = peak(data, data2, False)  # xx -> Дельта h - приближение
    # Кол-во точек не равно, поэтому выбросы, концевой эффект
    print(xx)
    while flag:
        data2 = invert(h)
        # print(data2)
        # print(h)
        h, xx = peak(h, data2, False)
        # print(xx)
        if xx < 0.1:  # Эпсилон
            c = h.copy()
            flag = False

    # Вычисление функции r -> новых данных
    for i in range(len(data)):
        r.append(data[i] - c[i])
    plt.subplot(211)
    plt.title('c(t)')
    plt.plot(c, color="red")  # high frquency
    plt.grid()
    plt.subplot(212)
    plt.title('r(t)')
    plt.plot(r, color="black")  # low frquency
    plt.grid()
    plt.show()
    return r, c


tmp = []  # Собрать исходную функцию
a1, c1 = end(data)  # Избавиться от концевого эффекта
a2, c2 = end(a1)
a3, c3 = end(a2)
plt.plot(data, color='Black')
plt.plot(a1, color='red')
plt.plot(a2, color='brown')
plt.plot(a3, color='green')
plt.grid()
plt.show()
for i in range(len(data)):
    tmp.append(c1[i] + c2[i] + c3[i])
# print(c1)
# print(c2)
# print(c3)
# print(tmp)
# plt.plot(tmp)
# plt.grid()
# plt.show()
# Условие на выход из внешнего цикла, по недостатку пиковых точек min=3

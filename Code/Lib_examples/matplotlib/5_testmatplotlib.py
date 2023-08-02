from matplotlib import pyplot as plt
import numpy as np
"""
Рисуем рамку с двумя графиками на ней 
"""

fig, ax = plt.subplots()

x = np.arange(-5, 5.1, 0.1)
y = np.arange(-5, 5.1, 0.1) ** 2  # Создает массив ndarray из numpy значений от -5 до 5 с шагом 0.1 возведенных в ^2
x_abs = np.abs(np.arange(-5, 5.1, 0.1))


ax.plot(x, y)
ax.plot(x, x_abs)


plt.show()

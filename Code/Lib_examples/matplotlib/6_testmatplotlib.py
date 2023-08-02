from matplotlib import pyplot as plt
import numpy as np
"""
Рисуем рамку с 4 графиками на ней
"""

fig, axes = plt.subplots(2, 2)

x = np.arange(-5, 5.1, 0.1)
y = np.arange(-5, 5.1, 0.1) ** 2  # Создает массив ndarray из numpy значений от -5 до 5 с шагом 0.1 возведенных в ^2
x_abs = np.abs(np.arange(-5, 5.1, 0.1))
y_3 = np.arange(-5, 5.1, 0.1) ** 3
y_abs_root = np.power(np.abs(np.arange(-5, 5.1, 0.1)), 0.1)


axes[0, 0].plot(x, y)
axes[0, 1].plot(x, x_abs)
axes[1, 0].plot(x, y_3)
axes[1, 1].plot(x, y_abs_root)

plt.show()

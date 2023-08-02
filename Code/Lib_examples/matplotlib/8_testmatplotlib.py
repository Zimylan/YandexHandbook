from matplotlib import pyplot as plt
import numpy as np
"""
Маркеры
"""

fig, axes = plt.subplots(2, 3)

x = np.arange(-9, 10, 2)
y_pow_2 = np.arange(-9, 10, 2) ** 2  # Создает массив ndarray из numpy значений от -5 до 5 с шагом 0.1 возведенных в ^2

axes[0, 0].plot(x, y_pow_2, color="red", linestyle='-', marker='o')
axes[0, 1].plot(x, y_pow_2, color="green", linestyle='-', marker='^')
axes[0, 2].plot(x, y_pow_2, color="blue", linestyle='-', marker='*')
axes[1, 0].plot(x, y_pow_2, color="yellow", linestyle='-', marker='s')
axes[1, 1].plot(x, y_pow_2, color="pink", linestyle='-', marker='.')
axes[1, 2].plot(x, y_pow_2, color="magenta", linestyle='-', marker='+')


plt.show()
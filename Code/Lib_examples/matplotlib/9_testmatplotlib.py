from matplotlib import pyplot as plt
import numpy as np
"""
Прозрачность и толщина линий
"""

fig, axes = plt.subplots(2, 3)

x = np.arange(-9, 10, 2)
y_pow_2 = np.arange(-9, 10, 2) ** 2  # Создает массив ndarray из numpy значений от -5 до 5 с шагом 0.1 возведенных в ^2

axes[0, 0].plot(x, y_pow_2, color="gray", linestyle='-', marker='o', alpha=0.1, linewidth=3.5)
axes[0, 1].plot(x, y_pow_2, color="gray", linestyle='-', marker='^', alpha=0.3, linewidth=3.)
axes[0, 2].plot(x, y_pow_2, color="gray", linestyle='-', marker='*', alpha=0.5, linewidth=2.5)
axes[1, 0].plot(x, y_pow_2, color="gray", linestyle='-', marker='s', alpha=0.7, linewidth=2.)
axes[1, 1].plot(x, y_pow_2, color="gray", linestyle='-', marker='.', alpha=0.9, linewidth=1.5)
axes[1, 2].plot(x, y_pow_2, color="gray", linestyle='-', marker='+', alpha=1.0, linewidth=1.)


plt.show()
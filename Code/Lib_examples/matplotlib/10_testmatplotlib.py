from matplotlib import pyplot as plt
import numpy as np
"""
Пределы по осям
"""

fig, axes = plt.subplots(2, 3)

x = np.arange(-10, 10, 0.1)
y_sin = np.sin(np.arange(-10, 10, 0.1))  # Создает массив ndarray из numpy значений от -5 до 5 с шагом 0.1 возведенных в ^2

axes[0, 0].plot(x, y_sin, color="gray", linestyle='-')
axes[0, 0].set_xlim(0, 12)
axes[0, 1].plot(x, y_sin, color="gray", linestyle='-')
axes[0, 1].set_xlim(-12, 12)
axes[0, 2].plot(x, y_sin, color="gray", linestyle='-')
axes[0, 2].set_ylim(0, 2)
axes[1, 0].plot(x, y_sin, color="gray", linestyle='-')
axes[1, 0].set_ylim(-2, 2)



plt.show()
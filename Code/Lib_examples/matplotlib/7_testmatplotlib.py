from matplotlib import pyplot as plt
import numpy as np
"""
Рисуем цветные графики с разными стилями линий
"""

fig, axes = plt.subplots(2, 3)

x = np.arange(-5, 5.1, 0.1)
y_pow_2 = np.arange(-5, 5.1, 0.1) ** 2  # Создает массив ndarray из numpy значений от -5 до 5 с шагом 0.1 возведенных в ^2
y_is_x_abs = np.abs(np.arange(-5, 5.1, 0.1))
y_pow_3 = np.arange(-5, 5.1, 0.1) ** 3
y_abs_root = np.power(np.abs(np.arange(-5, 5.1, 0.1)), 0.1)
y_sin = np.sin(np.arange(-5, 5.1, 0.1))

axes[0, 0].plot(x, y_pow_2, color=(1.0, 0.2, 0.1), linestyle='-')
axes[0, 1].plot(x, y_is_x_abs, color='blue', linestyle='--')
axes[1, 0].plot(x, y_pow_3, color='g', linestyle=':')
axes[1, 1].plot(x, y_abs_root, color='0.75', linestyle='-.')
axes[0, 2].plot(x, y_sin, color='#FFDD44', linestyle=(0, (1, 5)))

plt.show()
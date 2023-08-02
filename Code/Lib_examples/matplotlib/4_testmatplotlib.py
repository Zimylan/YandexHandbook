from matplotlib import pyplot as plt
import numpy as np
"""
Рисуем график
"""

fig, ax = plt.subplots()

x = np.arange(-5, 5.1, 0.1)
y = np.arange(-5, 5.1, 0.1) ** 2  # Создает массив ndarray из numpy значений от -5 до 5 с шагом 0.1 возведенных в ^2



ax.plot(x, y)



plt.show()

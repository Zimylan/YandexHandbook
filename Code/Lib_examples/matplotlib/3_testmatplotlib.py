from matplotlib import pyplot as plt
import numpy as np
"""
Рисуем рамку графика с 4 графиками 2х2 другим способом
"""

fig = plt.figure()

ax1 = fig.add_subplot(2, 2, 1)  # расчерчиваем фигуру fig на 4 части 2х2 и вставляем в 1 область
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)


plt.show()

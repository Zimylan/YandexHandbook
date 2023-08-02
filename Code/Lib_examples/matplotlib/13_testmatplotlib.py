from matplotlib import pyplot as plt
import numpy as np
"""
Подписи, легенда и регулирование отступов
"""

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
N = 50

"""Координаты"""
x = np.random.uniform(-1, 1, (1, 50))
y = np.random.uniform(-1, 1, (1, 50))
z = np.random.uniform(-1, 1, (1, 50))


colors = np.random.rand(N)  # Цвет кружочков
area = (50 * np.random.rand(N)) ** 2  # Площадь кружочков


ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_zlim(-1.5, 1.5)

ax.set_xticks(np.arange(-1.5, 1.6, 0.5))
ax.set_yticks(np.arange(-1.5, 1.6, 0.5))
ax.set_zticks(np.arange(-1.5, 1.6, 0.5))

ax.scatter(x, y, z, s=area, c=colors, alpha=0.5, marker=".")


plt.show()
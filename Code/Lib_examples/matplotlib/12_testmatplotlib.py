from matplotlib import pyplot as plt
import numpy as np
"""
Подписи, легенда и регулирование отступов
"""

fig, axes = plt.subplots(2)
fig.tight_layout(h_pad=4)  # Регулирование отступов
fig.suptitle('График функции SIN', fontsize=20)  # Создание общего заголовка
plt.subplots_adjust(top=0.85, left=0.12, bottom=0.1)  # Регулирование отступа общего заголовка и вообще всех объектов



x = np.arange(-10, 10.1, 0.1)
y_pow_2 = np.arange(-10, 10.1, 0.1) ** 2  # Создает массив ndarray из numpy значений от -5 до 5 с шагом 0.1 возведенных в ^2
y_sin = np.sin(np.pi * np.arange(-10, 10.1, 0.1))

axes[0].plot(x, y_pow_2, color="r", label="x^2")
axes[0].set_title("Заголовок графика: x^2", fontsize=12)
axes[0].set_ylim(-20, 120)
axes[0].set_xlabel("Ось X")
axes[0].set_ylabel("Ось Y")
axes[0].legend(loc="upper right")

"""Строим график"""
axes[1].plot(x, y_sin, color="r", label="sin(x)")

"""Заголовок"""
axes[1].set_title("Заголовок графика: sin(x)", fontsize=12)

"""Ограничения по оси Y"""
axes[1].set_ylim(-1.5, 1.5)

"""Разбиение по осям X, Y"""
axes[1].set_xticks(np.arange(-10, 11, 10))
axes[1].set_yticks(np.arange(-1.5, 1.5, 0.5))

"""Добавление сетки"""
axes[1].grid(color='gray', linewidth=0.5, linestyle='-.')  # Добавление сетки

"""Убираем рамку"""
axes[1].spines['right'].set_visible(False)  # Убрать рамку справа
axes[1].spines['top'].set_visible(False)
axes[1].spines['bottom'].set_visible(False)
axes[1].spines['left'].set_visible(False)

"""Переносим оси X, Y в центр графика"""
axes[1].yaxis.set_ticks_position('left')  # Перенос оси
axes[1].xaxis.set_ticks_position('bottom')
axes[1].spines['left'].set_position(('data',0))  # Перенос в ноль
axes[1].spines['bottom'].set_position(('data',0))

"""Подписи осей X, Y"""
axes[1].set_xlabel("Ось X")
axes[1].set_ylabel("Ось Y")

"""Легенда"""
axes[1].legend(loc="lower left")


# fig.savefig("12.png", transparent=True)
plt.show()
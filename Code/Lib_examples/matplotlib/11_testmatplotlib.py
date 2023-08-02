from matplotlib import pyplot as plt
import numpy as np
"""
Подписи, легенда и регулирование отступов
"""

fig, axes = plt.subplots(2)
fig.tight_layout(h_pad=4)  # Регулирование отступов
fig.suptitle('Графики функций', fontsize=20)  # Создание общего заголовка
plt.subplots_adjust(top=0.85, left=0.12, bottom=0.1)  # Регулирование отступа общего заголовка и вообще всех объектов



x = np.arange(-10, 10.1, 0.1)
y_pow_2 = np.arange(-10, 10.1, 0.1) ** 2  # Создает массив ndarray из numpy значений от -5 до 5 с шагом 0.1 возведенных в ^2
y_sin = np.sin(np.pi * np.arange(-10, 10.1, 0.1))

# fig.set_title("Графики функций")  # Не работает так
axes[0].plot(x, y_pow_2, color="r", label="x^2")
axes[0].set_title("Заголовок графика: x^2", fontsize=12)
axes[0].set_ylim(-20, 120)
axes[0].set_xlabel("Ось X")
axes[0].set_ylabel("Ось Y")
axes[0].legend(loc="upper right")


axes[1].plot(x, y_sin, color="r", label="sinx")
axes[1].set_title("Заголовок графика: sinx", fontsize=12)
axes[1].set_ylim(-1.5, 1.5)
axes[1].set_xlabel("Ось X")
axes[1].set_ylabel("Ось Y")
axes[1].legend(loc="lower left")

fig.savefig("11.png", transparent=True)
# plt.show()
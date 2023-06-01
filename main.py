import math
import random
import matplotlib.pyplot as plt

# Функція, що обчислює точне значення інтегралу від тестової підінтегральної функції
def exact_value_g():
    return 1/4

# Функція, що обчислює точне значення інтегралу від основної підінтегральної функції
def exact_value_h():
    return (2*math.e - 3)/4

# Функція, що генерує випадкову точку на координатній площині
def generate_point():
    x = random.uniform(0, 1)
    y = random.uniform(0, 1)
    return (x, y)

# Функція, що повертає значення підінтегральної функції в заданій точці
def integrand_value(x, mode):
    if mode == "test":
        return x**3
    elif mode == "main":
        return math.sqrt(x) * math.exp(x)

num_points = 1000000

# Кількість точок, що потрапили під графік кривої
num_hits_g = 0
num_hits_h = 0

# Списки для зберігання координат точок, які потрапили під графік кривої
x_hits_g = []
y_hits_g = []
x_hits_h = []
y_hits_h = []

# Генерація випадкових точок та підрахунок кількості точок, що потрапили під графік кривої
for i in range(num_points):
    x, y = generate_point()
    if y <= integrand_value(x, "test"):
        num_hits_g += 1
        x_hits_g.append(x)
        y_hits_g.append(y)
    if y <= integrand_value(x, "main"):
        num_hits_h += 1
        x_hits_h.append(x)
        y_hits_h.append(y)

# Обчислення оцінки інтегралу за допомогою методу Монте-Карло
approx_value_g = num_hits_g / num_points
approx_value_h = num_hits_h / num_points

error_g = abs(approx_value_g - exact_value_g())
error_h = abs(approx_value_h - exact_value_h())

print(f"Наближене значення інтеграла для тестової функції: {approx_value_g:.6f}")
print(f"Точне значення інтеграла для тестової функції: {exact_value_g():.6f}")
print(f"Абсолютна похибка тестової функції: {error_g:.6f}\n")

print(f"Наближене значення інтеграла для основної функції: {approx_value_h:.6f}")
print(f"Точне значення інтеграла для основної функції: {exact_value_h():.6f}")
print(f"Абсолютна похибка для основної функції: {error_h:.6f}\n")

plt.figure(figsize=(8, 8))
plt.plot(x_hits_g, y_hits_g, "r.", markersize=1)
plt.plot([0, 1], [0, 1], "b-", linewidth=2)
plt.title("Test function")
plt.show()

plt.figure(figsize=(8, 8))
plt.plot(x_hits_h, y_hits_h, "r.", markersize=1)
plt.plot([0, 1], [0, math.e], "b-", linewidth=2)
plt.title("Main function")
plt.show()
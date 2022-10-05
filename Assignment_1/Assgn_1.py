import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 3 * np.pi, 1500)

radius = 1

a = radius * np.cos(theta)
b = radius * np.sin(theta)
x = [-1, 1, 0]
x1 = [0, 0.5, 1]
y1 = [0, 0, 0]
figure, axes = plt.subplots(1)

axes.plot(a, b)
axes.set_aspect(1)
plt.plot(x, y1)
plt.scatter(x1, y1, color="black", marker="x", s=100)
plt.title('Pole-Zero Diagram')
plt.show()

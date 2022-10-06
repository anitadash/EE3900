import numpy as np
import matplotlib.pyplot as plt

x = np.array([1.0, 2.0, 1.0])
y = np.array([0.0, -1.0, -2.0, 0.0, 2.0, 1.0])
x1 = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 3.0, 2.0, 1.0, 0.0])

y0 = np.array([0.0, 2.0, 1.0])
y1 = np.zeros(9)
y1[0] = -1
y1[1] = -2
y1[2] = y0[0] + 2 * (-1)
y1[3] = y0[1] + 2 * (-2)
y1[4] = y0[2] + 2 * (y0[0]) + (-1)
y1[5] = 2 * (y0[1]) + (-2)
y1[6] = 2 * (y0[2]) + y0[0]
y1[7] = y0[1]
y1[8] = y0[2]

plt.subplot(1, 2, 1)
plt.stem(range(-1, 2), x)
plt.title('Plot of $x_0(n)$')
plt.xlabel('$n$')
plt.subplot(1, 2, 2)
plt.stem(range(-3, 3), y)
plt.title('Plot of $y_0(n)$')
plt.xlabel('$n$')
plt.show()

plt.stem(range(0, 9), x1)
plt.title('Plot of $x_1(n)$')
plt.ylabel('$x_1(n)$')
plt.xlabel('$n$')
plt.show()
plt.stem(range(0, 9), y1)
plt.title('Plot of $y_1(n)$')
plt.ylabel('$y_1(n)$')
plt.xlabel('$n$')
plt.show()

import numpy as np
import matplotlib.pyplot as plt

x = open('x.txt', "r").read().splitlines()
y = open('y.txt', "r").read().splitlines()
x = np.asarray(x, dtype=float)
y = np.asarray(y, dtype=float)

plt.subplot(2, 1, 1)
plt.stem(range(0, 6), x)
plt.title('Digital Filter Input-Output')
plt.ylabel('$x(n)$')
plt.grid()

plt.subplot(2, 1, 2)
plt.stem(range(0, 20), y)
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()

plt.show()

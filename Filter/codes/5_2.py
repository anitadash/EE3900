import numpy as np
import matplotlib.pyplot as plt


def u(n):
    if n >= 0:
        return 1
    else:
        return 0


h = np.zeros(12)
for i in range(0, 12):
    h[i] = ((-1 / 2) ** i) * (u(i)) + ((-1 / 2) ** (i - 2)) * u(i - 2)
plt.stem(range(0, 12), h)
plt.title('Filter Impulse Response')
plt.xlabel('$n$')
plt.ylabel('$h(n)$')
plt.grid()
plt.show()

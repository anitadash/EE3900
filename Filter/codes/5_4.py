import numpy as np
import matplotlib.pyplot as plt


def delta(n):
    if n == 0:
        return 1
    else:
        return 0


h = np.zeros(12)
h[0] = 1
for i in range(1, 12):
    h[i] = delta(i) + delta(i - 2) - 0.5 * (h[i - 1])
plt.stem(range(0, 12), h)
plt.title('Impulse Response Definition')
plt.ylabel('$h(n)$')
plt.xlabel('$n$')
plt.grid()
plt.show()

import numpy as np
import matplotlib.pyplot as plt

h = np.zeros(14)
for i in range(len(h)):
    if i == 0:
        h[i] = 1.0
    elif i == 1:
        h[i] = -0.5
    else:
        h[i] = 5 * (-1 / 2) ** i

nh = len(h)
x = np.array([1.0, 2.0, 3.0, 4.0, 2.0, 1.0])
nx = len(x)

y = np.zeros(nx + nh - 1)

for k in range(0, nx + nh - 1):
    for n in range(0, nx):
        if 0 <= k - n < nh:
            y[k] += x[n] * h[k - n]

print(y)
# plots
plt.stem(range(0, nx + nh - 1), y)
plt.title('Filter Output using Convolution')
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()

plt.show()

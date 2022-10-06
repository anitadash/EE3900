import numpy as np
import matplotlib.pyplot as plt

x = np.zeros(10)
x[0] = 1
x[1] = 1
for i in range(2,10):
    x[i] = x[i-1] + x[i-2]

plt.stem(range(0, 10), x)
plt.title('Plot of $x(n)$')
plt.ylabel('$x(n)$')
plt.xlabel('$n$')
plt.show()
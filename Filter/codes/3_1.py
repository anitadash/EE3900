import numpy as np
import matplotlib.pyplot as plt

x = np.array([1.0, 2.0, 3.0, 4.0, 2.0, 1.0])
plt.stem(range(0, 6), x)
plt.title('Plot of $x(n)$')
plt.ylabel('$x(n)$')
plt.xlabel('$n$')
plt.grid()
plt.show()

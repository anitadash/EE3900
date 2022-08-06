import numpy as np
import matplotlib.pyplot as plt

x = np.array([1.0,2.0,3.0,4.0,2.0,1.0])
y = np.zeros(20)
y[0] = x[0];
y[1] = -0.5*y[0] + x[1]
for i in range(2,19):
	if(i<6):
		y[i] = -0.5*y[i-1] + x[i] +x[i-2]
	elif(i>5 and i<8):
		y[i] = -0.5*y[i-1] + x[i-2]
	else:
		y[i] = -0.5*y[i-1]

plt.stem(range(0,20),y)
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()
plt.show()
		
	

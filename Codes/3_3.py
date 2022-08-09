import numpy as np
import matplotlib.pyplot as plt

def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        words = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()
        return words

x = readFile('x.txt')
y = readFile('y.txt')
x = np.asarray(x, dtype=float)
y = np.asarray(y, dtype=float)

plt.subplot(2, 1, 1)
plt.stem(range(0,6),x)
plt.title('Digital Filter Input-Output')
plt.ylabel('$x(n)$')
plt.grid()


plt.subplot(2, 1, 2)
plt.stem(range(0,20),y)
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()

plt.show()

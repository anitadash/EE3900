import numpy as np
import matplotlib.pyplot as plt

def H(z):
	num = 1.0 + z**(-2)
	den = 1.0 + 0.5*(z**(-1))
	H = num/den
	return H
w = np.linspace(-3*np.pi,3*np.pi,100)
plt.plot(w,(H(np.exp(1j*w))))
plt.title("Filter Frequency Response")
plt.ylabel("$|H(e^{\jmath\omega})|$")
plt.xlabel("$\omega$")
plt.grid()
plt.show()





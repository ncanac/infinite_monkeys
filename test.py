import pylab as plt
import numpy as np
import sys
from scipy.stats import t

x = np.array([0.0, 1.0, 2.0, 3.0,  4.0,  5.0])
y = np.array([0.0, 0.8, 0.9, 0.1, -0.8, -1.0])
coeffs = np.polyfit(x, y, 3)

z = coeffs[0]*x**3 + coeffs[1]*x**2 + coeffs[2]*x + coeffs[3]

plt.plot(x,y)
plt.plot(x,z)
plt.show()

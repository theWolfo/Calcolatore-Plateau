import matplotlib.pyplot as plt
import numpy as np

t , p = np.loadtxt('pressione.dat', usecols=(0,1), unpack=True)

plt.plot(t, p)
plt.show()
import numpy as np
import math as mt
import matplotlib.pyplot as plt

x=np.arange(0, 2, 0.01)
y1=np.sin(2*mt.pi*x)
y2=1.2*np.sin(4*mt.pi*x)

plt.subplot(3, 1, 1)
plt.fill_between(x, 0, y1)

plt.subplot(3, 1, 2)
plt.fill_between(x, y1, 1)

plt.subplot(3, 1, 3)
plt.fill_between(x, y1, y2)

plt.show()
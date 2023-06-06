import numpy as np
import math as mt
import matplotlib.pyplot as plt
t=np.linspace(0, 2*mt.pi)
def A(t):
    x=np.cos(t)**3
    y=np.sin(t)**3
    return x, y
def B(t):
    x=t+2*np.sin(2*t)
    y=t+2*np.cos(5*t)
    return x, y
def C(t):
    x=np.sin(3*t)
    y=np.sin(4*t)
    return x, y


x, y=C(t)
plt.plot(x, y , color='m')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')

plt.show()

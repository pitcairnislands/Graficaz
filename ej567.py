import numpy as np
from numpy import sin, cos
import math as mt
import matplotlib.pyplot as plt

t=np.arange(0, 4*mt.pi, 0.001)
def A(t):
    r=2+sin(t)*(np.sqrt(abs(cos(t)))/(sin(t)+1.4) - 2)
    x=r*cos(t)
    y=r*sin(t)
    return x, y

def B(t):
    r=-250*sin(5*t)*cos(4*t)
    l=t + sin(r/100)
    x=320 + r*cos(l)
    y=-240 - r*sin(l)
    return x, y

def C(t):
    r=105 + 100*sin(4.5*t)
    l=t - cos(10*t)/10
    x=320 + r*cos(l)
    y=-240 - r*sin(l)
    return x, y

x, y=C(t)
plt.plot(x, y , color='m')
#plt.fill_between(x, y, color='r')
plt.axis('equal')
plt.axis('off')
#plt.xlabel('Eje X')
#plt.ylabel('Eje Y')

plt.show()
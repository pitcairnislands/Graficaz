import numpy as np
from numpy import sin, cos
import math as mt
import matplotlib.pyplot as plt
x=np.arange(-1,1, 0.01)
y=np.arange(-1,1, 0.01)
X,Y=np.meshgrid(x, y)
def A(x, y):
    z=x**2 - y**2
    return z

def B(x, y):
    return x*np.exp(-(x**2 + y**2))

def C(x, y):
    return np.sqrt(abs(cos(x) + cos(y)))

def D(x, y):
    return sin(abs(x) - abs(y))

def E(x, y):
    z=cos(abs(x) + abs(y))
    return z

def F(x, y):
    return cos(abs(x) + abs(y))*(abs(x) + abs(y))

a=plt.axes(projection='3d')
a=plt.gca()

a.plot_surface(X,Y,F(X, Y), color='#9014A6', linewidth=0)
plt.show()


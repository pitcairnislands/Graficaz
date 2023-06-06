import numpy as np
import matplotlib.pyplot as plt
x=np.arange(-10,10, 0.01)
y=np.arange(-10,10, 0.01)
x0,y0=np.meshgrid(x,y)
z=np.cos(abs(x0)+abs(y0))*(abs(x0)+abs(y0))
a=plt.axes(projection='3d')
a=plt.gca()
a.plot_surface(x0,y0,z, color='#98C7A0', linewidth=0)
plt.show()
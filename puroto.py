import numpy as np
import math as mt
import matplotlib.pyplot as plt
a=np.linspace(-6,2,200)
def A(x): #linspace -6,2,200 verde, titulo eje x
    return  5 - 4*x - x**2

b=np.linspace(-1,5,100)
def B(x): #-1,5,100 rojo, tamaño 10, titulo eje x eje y
    return  2*(x**2) - 8*x -11

c=np.linspace(-1,5,300)
def C(x): #-1,5,300 color k, tamaño 10, nombre eq
    return x*(np.exp(-2*x))

d=np.linspace(0,24,250)
def D(x): 
    return np.sin(2*x)*np.exp(-0.1*x)

e=np.linspace(0,4*mt.pi,200) #azul 
def E(x): 
    return np.sin(2*x) + np.cos(2*x)

#f=np.linspace(0,4*mt.pi,200) #rojo
def F(x): 
    return 3*np.cos(3*x) - 2*np.sin(2*x)

g=np.linspace(0,2,100) #cian
def G(x): 
    return x*np.exp(-3*x)

#h=np.linspace(0,2,100) #magenta
def H(x): 
    return (1-3*x*np.exp(-3*x))

i=np.linspace(0,4*mt.pi,100) #cian
def I(x): 
    return np.sin(3*x)*np.cos(2*x)

#j=np.linspace(0,4*mt.pi,100) #magenta
def J(x): 
    return (np.cos(x)+5*np.cos(5*x))/2
k=np.linspace(0,2*mt.pi,100) #cian
def K(x): 
    return (np.cos(x)*(1+np.sin(x)))
#l=np.linspace(0,2*mt.pi,200) #magenta
def L(x): 
    return (np.sin(x)*(1+2*np.sin(x)))
plt.plot(k, K(k), '.', color='c', markersize=10, label ='f(x)')
plt.plot(k, L(k), '.', color='m', markersize=10, label = 'g(x)')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('$f(x)=cos(x)(1+sin(x)),   g(x)=sin(x)(1+2sin(x))$')
plt.legend()
plt.show()

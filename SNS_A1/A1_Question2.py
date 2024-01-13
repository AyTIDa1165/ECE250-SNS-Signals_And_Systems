import numpy as np
import matplotlib.pyplot as plt

def fgraph(x, y):
    plt.grid(True, which='both')
    plt.axhline(y=0, color = 'k')
    plt.axvline(x=0, color = 'k')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')

def func(x, a):
    if x>=0:
        return 2*np.exp((-1)*a*x)
    return 0

def even(x, a):
    if x>=0:
        return np.exp((-1)*a*x)
    return np.exp(a*x)

def odd(x, a):
    if x>=0:
        return np.exp((-1)*a*x)
    return (-1)*np.exp(a*x)

a = 2
x = np.linspace(-3, 3, 1000)

y1 = [func(i, a) for i in x]
fgraph(x, y1)
plt.plot(x, y1)
plt.title("Plot for given function")
plt.show()

y2 = [even(i, a) for i in x]
fgraph(x, y2)
plt.plot(x, y2)
plt.title("Even part of the function")
plt.show()

y3 = [odd(i, a) for i in x]
fgraph(x, y3)
plt.plot(x, y3)
plt.title("Odd part of the function")
plt.show()
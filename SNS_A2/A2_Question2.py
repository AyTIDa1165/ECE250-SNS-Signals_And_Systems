import numpy as np
import matplotlib.pyplot as plt

def fgraph(x, y):
    plt.grid(True, which='both')
    plt.axhline(y=0, color = 'k')
    plt.axvline(x=0, color = 'k')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')

def input_func(x):
    if x>=0 and x <= 4:
        return 1
    return 0

def response_func(x, a):
    if x>=0 and x<=6:
        return pow(a, x)
    return 0

def convolution_func(n):
    sum = 0
    for k in range(-100, 100):
        sum += input_func(k)*response_func(n-k, a)
    return sum

a = 2
x = np.arange(-15, 16)

y1 = [input_func(i) for i in x]
fgraph(x, y1)
plt.stem(x, y1, linefmt='k', markerfmt='ko', basefmt='k')
plt.title("Plot for x[n]")
plt.show()

y2 = [response_func(i, a) for i in x]
fgraph(x, y2)
plt.stem(x, y2, linefmt='k', markerfmt='ko', basefmt='k')
plt.title("Plot for h[n]")
plt.show()

y3 = [convolution_func(i) for i in x]
fgraph(x, y3)
plt.stem(x, y3, linefmt='k', markerfmt='ko', basefmt='k')
plt.title("Plot for convolution")
plt.show()
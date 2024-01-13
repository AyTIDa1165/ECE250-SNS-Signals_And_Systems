import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from functools import partial

def fgraph(x, y, i, axes, givenTitle):
    axes[i].grid(True, which='both')
    axes[i].set_xlabel('k')
    # axes[i].set_ylabel('Coefficients')
    axes[i].axhline(y = 0, color='r')
    axes[i].axvline(x = 0, color='r')
    axes[i].set_title(givenTitle)

def input(x):
    if x >= -np.pi and x <= np.pi:
        return x + np.pi
    elif x < 0:
        return input(x + 2*np.pi)
    else:
        return input(x - 2*np.pi)

def integrand(t, k, flag):
    if(flag == 0):
        return (input(t) * np.cos((-2*np.pi*t*k)/T))
    else:
        return (input(t) * np.sin((-2*np.pi*t*k)/T))

def coefficient(k, flag):
    result, _ = quad(partial(integrand, k=k, flag=flag), -np.pi, np.pi)
    result /= T
    return result

fig, axes = plt.subplots(1, 3, figsize=(30, 5))

T = 2*np.pi
x = np.linspace(-3*np.pi, 3*np.pi, 1000)
x_fourier = np.arange(-10, 11)

y = [input(i) for i in x]
y_re = [coefficient(i, 0) for i in x_fourier]
y_im = [coefficient(i, 1) for i in x_fourier]

fgraph(x, y, 0, axes, "Plot for f(x)")
axes[0].plot(x, y)

fgraph(x, y_re, 1, axes, "Fourier Series on Real axis")
axes[1].stem(x_fourier, y_re, linefmt='k', markerfmt='ko')
axes[1].set_xticks(np.arange(-10, 11 , 1))

fgraph(x, y_im, 2, axes, "Fourier Series on Imaginary axis")
axes[2].stem(x_fourier, y_im, linefmt='k', markerfmt='ko')
axes[2].set_xticks(np.arange(-10, 11 , 1))

fig.suptitle('Fourier series representation of x(t)', fontsize=16)
plt.tight_layout()
plt.subplots_adjust(left = 0.02, wspace=0.2)
plt.show()
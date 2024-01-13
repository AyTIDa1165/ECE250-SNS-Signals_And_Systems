import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.integrate import quad
from functools import partial


def fgraph(x, y, i, j, axes, givenTitle):
    axes[i][j].grid(True, which='both')
    axes[i][j].set_xlabel('w')
    axes[i][j].set_ylabel('Value')
    axes[i][j].axhline(y = 0, color='r')
    axes[i][j].axvline(x = 0, color='r')
    axes[i][j].set_title(givenTitle)

def input(x):
    if x >= -1 and x <= 0:
        return 2
    elif x >= 0 and x <= 1:
        return 2-x
    elif x >= 1 and x <= 2:
        return x
    elif x >= 2 and x <= 3:
        return 2
    else:
        return 0

def integrand(t, w, flag):
    if(flag == 0):
        return np.real(input(t) * np.exp(-1j*w*t))
    else:
        return np.imag(input(t) * np.exp(-1j*w*t))

def fourierTransform(w, flag):
    result, _ = quad(partial(integrand, w=w, flag=flag), -np.inf, np.inf)
    return result

def magnitudeSpectrum(w):
    return np.sqrt(fourierTransform(w, 0)**2 + fourierTransform(w, 1)**2)

def phaseSpectrum(w):
    return np.arctan2(fourierTransform(w, 1), fourierTransform(w, 0))

def evenPart(f, t):
    return (f(t) + f(-t))/2.0

def inverseFourierTransform(t):
    return evenPart(input, t)
    
# def integrand2(w, t, flag):
#     if flag == 0:
#         return np.real((fourierTransform(w, 0)) * np.exp(1j*w*t))
#     else:
#         return np.imag((fourierTransform(w, 0)) * np.exp(1j*w*t))
    
# def inverseFourierTransform(t, flag):
#     result, _ = quad(partial(integrand2, t = t, flag = flag), -np.inf, np.inf)
#     result /= 2*np.pi
#     return result

fig, axes = plt.subplots(2, 2, figsize=(15, 15))
length = 20
x = np.linspace(-length, length, 1000)

y = [input(i) for i in x]
y_mag = [magnitudeSpectrum(i) for i in x]
y_phs = [phaseSpectrum(i) for i in x]
y_real = [fourierTransform(i, 0) for i in x]
y_imag = [fourierTransform(i, 1) for i in x]

fgraph(x, y_real, 0, 0, axes, "Re(X(jw))")
axes[0][0].plot(x, y_real)
# axes[0][0].set_xticks(np.arange(-length, length + 1 , 1))

fgraph(x, y_imag, 0, 1, axes, "Im(X(jw))")
axes[0][1].plot(x, y_imag)
# axes[0][1].set_xticks(np.arange(-length, length + 1 , 1))


fgraph(x, y_mag, 1, 0, axes, "|X(jw)|")
axes[1][0].plot(x, y_mag)
# axes[1][0].set_xticks(np.arange(-length, length + 1 , 1))

fgraph(x, y_phs, 1, 1, axes, "∡X(jw)")
axes[1][1].plot(x, y_phs)
# axes[1][1].set_xticks(np.arange(-length, length + 1 , 1))

fig.suptitle("Fourier Transform of x(t) {part a, b, c}", fontsize=16)
plt.tight_layout()
plt.subplots_adjust(left = 0.05, wspace=0.1, hspace=0.25, top= 0.9, bottom= 0.07)
plt.subplots_adjust()

plt.show()

length = 5
x = np.linspace(-length, length, 1000)
y_inv = [inverseFourierTransform(i) for i in x]

plt.figure(figsize=(8, 6))
plt.plot(x, y_inv)
plt.title('Inverse fourier transform of Re(X(jw))')
plt.xlabel('t')
plt.ylabel('x\'(t)')
plt.grid(True)
plt.xticks(np.arange(-length, length + 1 , 1))
plt.show()
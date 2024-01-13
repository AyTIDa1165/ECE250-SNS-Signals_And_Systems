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

def func1(n):
    return np.cos(np.pi*n)

def func2(n):
    return np.sin(np.pi*n/2)

def func3(n):
    if n%2 == 0:
        return 1
    else:
        return 0

def plotter(func, givenString):
    fig, axes = plt.subplots(2, 2, figsize=(15, 15))
    length = 10
    x_cont = np.linspace(-length, length, 1000)
    x_dis = np.arange(-length, length+1)

    def input(w):
        if w >= -np.pi/2 and w <= 0:
            return (2*w)/np.pi + 1
        elif w > 0 and w <= np.pi/2:
            return (-2*w)/np.pi + 1
        elif (w > np.pi/2 and w <= np.pi) or (w < -np.pi/2 and w >= -np.pi):
            return 0
        elif w < 0:
            return input(w + 2*np.pi)
        else:
            return input(w - 2*np.pi)
    def integrand_IFT(w, n):
        return input(w) * np.cos(w*n)
    
    def inverseFourierTransform(n):
        result, _ = quad(partial(integrand_IFT, n = n), -np.pi, np.pi)
        result /= 2*np.pi
        return result
    
    def fourierTransform(func, w, flag):
        integrand = 0
        for n in range(-15, 16): #can change for quicker results
            integrand += (inverseFourierTransform(n) * func(n) * np.exp(-1j*w*n))
        if(flag == 0):
            return round(np.real(integrand), 5)
        else:
            return round(np.imag(integrand), 5)

    fourierTransform(func, 2, 0)
    y = [input(w) for w in x_cont]
    y_inv = [inverseFourierTransform(n) for n in x_dis]
    y_FT_real = [fourierTransform(func, w, 0) for w in x_cont]
    y_FT_imag = [fourierTransform(func, w, 1) for w in x_cont]
    y_FT_mag = []
    y_FT_phs = []

    for i in range(len(y_FT_real)):
        y_FT_mag.append(np.sqrt(y_FT_real[i]**2 + y_FT_imag[i]**2))

        if(y_FT_real[i] == 0):
            y_FT_phs.append(np.pi/2*np.sign(y_FT_imag[i]))
        elif(y_FT_imag[i] == 0):
            y_FT_phs.append(0)
        else:
            y_FT_phs.append(np.arctan2(y_FT_imag[i], y_FT_real[i]))

    fgraph(x_cont, y_FT_real, 0, 0, axes, "Re(W(exp(jw)))")
    axes[0][0].plot(x_cont, y_FT_real)

    fgraph(x_cont, y_FT_imag, 0, 1, axes, "Im(W(exp(jw)))")
    axes[0][1].plot(x_cont, y_FT_imag)

    fgraph(x_cont, y_FT_mag, 1, 0, axes, "|W(exp(jw)|")
    axes[1][0].plot(x_cont, y_FT_mag)

    fgraph(x_cont, y_FT_phs, 1, 1, axes, "∡W(exp(jw)")
    axes[1][1].plot(x_cont, y_FT_phs)

    plt.subplots_adjust(left = 0.05, wspace=0.25, hspace=0.25, top= 0.9, bottom= 0.07)
    plt.suptitle(givenString, fontsize=16)
    plt.show()

plotter(func1, "(a) p[n] = cos(πn)")
plotter(func2, "(b) p[n] = sin(πn/2)")
plotter(func3, "(c) p[n] = ∑δ(n - 2k)")
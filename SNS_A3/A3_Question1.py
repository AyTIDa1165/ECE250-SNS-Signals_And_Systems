import numpy as np
import matplotlib.pyplot as plt

def fgraph(x, y, i, axes, givenTitle):
    axes[i].grid(True, which='both')
    axes[i].set_xlabel('k')
    axes[i].set_ylabel('Coefficients')
    axes[i].axhline(y=0, color='k')
    axes[i].axvline(x=0, color='k')
    axes[i].stem(x, y, linefmt='k', markerfmt='ko', basefmt='k')
    axes[i].set_title(givenTitle)
    # axes[i].set_xticks(np.arange(-20, 21 , 1))


def fourier(N1, N, givenTitle):
    x = np.arange(-20, 21)

    def input(x):
        if x>= -N1 and x<= N1:
            return 1
        elif N1<abs(x)<= (N-1)/2:
            return 0
        elif x>0:
            return input(x-N)
        else:
            return input(x+N)


    def coefficient(k , flag):
        sum = 0

        if flag == 0:
            for n in range(0, N):
                sum+= input(n)*np.cos((-2*np.pi*n*k)/N)
        else:
            for n in range(0, N):
                sum+= input(n)*np.sin((-2*np.pi*n*k)/N)
        sum = float(sum/N)
        return sum

    y_re = [round(coefficient(i, 0), 10) for i in x]
    y_im = [round(coefficient(i, 1), 10) for i in x]

    fig, axes = plt.subplots(1, 2, figsize=(10, 4))

    fgraph(x, y_re, 0, axes, "Real axis")
    fgraph(x, y_im, 1, axes, "Imaginary axis")

    fig.suptitle('Fourier series representation of x[n] for ' + givenTitle, fontsize=16)
    plt.tight_layout()
    plt.show()

N1 = 2
fourier(N1, 4*N1+1, "N=4N1+1")
fourier(N1, 8*N1+1, "N=8N1+1")
fourier(N1, 10*N1+1, "N=10N1+1")
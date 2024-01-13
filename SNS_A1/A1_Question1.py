import numpy as np
import matplotlib.pyplot as plt

fig, axs = plt.subplots(2, 2)

x_axes = []
y_axes = []
titles = []

x_axes.append(np.arange(-35, 35))
x_axes.append(np.arange(-35, 35))
x_axes.append(np.linspace(-35, 35, 1000))
x_axes.append(np.linspace(-35, 35, 1000))

y_axes.append(np.cos(x_axes[0]/6))
y_axes.append(np.sin((8*np.pi*x_axes[1])/31))
y_axes.append(np.cos(x_axes[2]/6))
y_axes.append(np.cos(x_axes[3]/6) + np.sin((2*np.pi*x_axes[3])/3))

titles.append("y[n] = cos[n/6]")
titles.append("y[n] = cos[8πn/31]")
titles.append("y(t) = cos(t/6)")
titles.append("y(t) = cos(t/6) + sin(2πt/3)")

count = 0
for i in range(2):
    for j in range(2):

        if i == 0:
            axs[i,j].stem(x_axes[count], y_axes[count])

        else:
            axs[i,j].plot(x_axes[count], y_axes[count])

        axs[i,j].set_title(titles[count])
        axs[i,j].grid(True, which='both')
        axs[i,j].axhline(y=0, color = 'k')
        axs[i,j].axvline(x=0, color = 'k')
        axs[i,j].set_xlabel('Time')
        axs[i,j].set_ylabel('Amplitude')

        count+= 1

for ax in axs.flat:
    x_ticks = np.arange(-35, 36, 10)
    ax.set_xticks(x_ticks)

plt.tight_layout()
plt.show()
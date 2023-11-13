import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.1, 2 * np.pi, 1000)

y = np.log(x) + np.cos(x)

plt.plot(x, y, label=r'$\log(x) + \cos(x)$')

plt.title('График функции $\\log(x) + \\cos(x)$')
plt.xlabel('$x$')
plt.ylabel('$y$')

plt.legend()

plt.show()
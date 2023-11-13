import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

y = np.sin(x) * np.cos(x)

plt.plot(x, y, label=r'$\sin(x) \cdot \cos(x)$')

plt.title('График функции $\\sin(x) \\cdot \\cos(x)$')
plt.xlabel('$x$')
plt.ylabel('$y$')

plt.legend()

plt.show()
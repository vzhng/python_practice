import array as arr
import numpy as np
from matplotlib import pyplot as plt

#x = np.array([1,2,3,4,5,6,7], dtype="i")
#x = np.array([1,2,3], [4,5,7], dtype="f")
x = np.arange(-20, 20)
y = 2 * x * x + 5

plt.plot(x, y)
plt.show()







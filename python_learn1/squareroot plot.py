import numpy as np
from matplotlib import pyplot as plt
import math

x = np.arange(1,100)
z = []
for i in x:
    y = math.sqrt(i)
    z.append(y)

plt.plot(x,z)
plt.show()
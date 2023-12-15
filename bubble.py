import matplotlib.pyplot as plt
import numpy as np
x = np.random.rand(90)
y = np.random.rand(90)
z = np.random.rand(90)
plt.scatter(x, y, s=z*1000,c="red")
plt.show()

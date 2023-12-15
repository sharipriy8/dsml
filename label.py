import numpy as np
import matplotlib.pyplot as plt

x = np.array([12,14,15,16,18])
y = np.array([100,200,250,400,300])

plt.plot(x, y)

plt.xlabel("person")
plt.ylabel("score")
plt.title("score/person")

plt.show()

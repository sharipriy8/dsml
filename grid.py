import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,2,6])
y = np.array([3,10,12])


plt.plot(x,y, marker = 'o')
plt.xlabel("person")
plt.ylabel("score")
plt.title("score/person")
plt.grid()
plt.show()


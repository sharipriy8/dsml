import matplotlib.pyplot as plt
import numpy as np
np.random.seed(5)
data = np.random.normal(10,20,30)
fig = plt.figure(figsize =(5,9))
plt.boxplot(data)
plt.show()


import matplotlib.pyplot as plt
import numpy as np
np.random.seed(5)
data1= np.random.normal(10,20,30)
data2=np.random.normal(20,30,40)
data=[data1,data2]
fig = plt.figure(figsize =(10,5))
plt.boxplot(data)
plt.show()

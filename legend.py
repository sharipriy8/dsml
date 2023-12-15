import matplotlib.pyplot as plt
x = [2,4,6,8,10]
y = [3,6,9,12,15]
z = [4,8,12,16,20]
plt.plot(x, y, 'g', label='Line y')
plt.plot(x, z, 'r', label='Line z')
plt.legend()
plt.show()


import matplotlib.pyplot as plt
y=['java', 'Python', 'C++']


x=[22.17,8.8,6.5]
plt.barh(y, x)


plt.ylabel("Programming Language")


plt.xlabel("Popularity")
plt.title("Horizontal bar graph")
plt.show()


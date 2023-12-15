import numpy as np
import matplotlib.pyplot as plt



data = {'Maths':30, 'physics':40, 'chemisrty':15,'Biology':25}
courses = list(data.keys())
values = list(data.values())

fig = plt.figure(figsize = (10, 5))


plt.bar(courses, values,width = 0.4)

plt.xlabel("Courses ")
plt.ylabel("No. of students enrolled")

plt.show()



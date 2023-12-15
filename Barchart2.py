import numpy as np
import matplotlib.pyplot as plt
 
  
# creating the dataset
data = {'Java':22.17, 'python':8.8, 'c++':6.5}
    
courses = list(data.keys())
values = list(data.values())
  
fig = plt.figure(figsize = (10, 5))
 
# creating the bar plot
plt.bar(courses, values, color ='red',
        width = 0.4)
 
plt.xlabel("Courses offered")
plt.ylabel("No. of students enrolled")
plt.title("Students enrolled in different courses")
plt.show()

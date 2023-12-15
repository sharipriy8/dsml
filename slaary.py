import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
dataset = pd.read_csv('Salary_Data.csv')

x = dataset[['YearsExperience']].values
y = dataset['Salary'].values

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 1/3, random_state = 0)

c_knn=KNeighborsClassifier(n_neighbors=3)
c_knn.fit(x_train, y_train)

y_pred = c_knn.predict(x_test)
print("knn Salary prediction")

a=float(input("Enter the years of Experience : "))
new_salary_pred = c_knn.predict([[a]])
print("The predicted salary" , a ,"experience ", new_salary_pred[0])



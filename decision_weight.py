import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics
dataset=pd.read_csv("dtheight.csv")
print(dataset)
print(dataset.shape)
print(dataset.head(5))
x=dataset.iloc[:,:-1].values
x
y=dataset.iloc[:,-1].values
y
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.20,random_state=0)


from sklearn.tree import DecisionTreeRegressor
model=DecisionTreeRegressor()
model.fit(x_train,y_train)
y_pred=model.predict(x_test)

print("Accuracy: ",metrics.accuracy_score(y_test,y_pred))
Age=int(input("enter the age "))
Height=int(input("enter the height "))
weight=[[Age,Height]]
Result=model.predict(weight)
print(Result)

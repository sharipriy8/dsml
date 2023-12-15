import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics
data=pd.read_csv("Iris.csv") 

print(dataset)
print(dataset.shape)
print(dataset.head(5))
x=dataset.iloc[:,:-1].values
x
y=dataset.iloc[:,-1].values
y
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.20,random_state=0)


from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(x_train,y_train)
house=model.coef_
print("co-efficient",house)
gj=model.intercept_
print("intercept",gj)

age=int(input("enter the age "))
hour=int(input("enter the hour "))
usage=int(input("enter the usage "))
price=[[age,hour,usage]]
Result=model.predict(price)
print(Result)

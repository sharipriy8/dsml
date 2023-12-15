from sklearn.model_selection import train_test_split

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
dataset=pd.read_csv('Salary_Data.csv')
x=dataset.iloc[:,:-1].values
y=dataset.iloc[:,:-1].values

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=1)


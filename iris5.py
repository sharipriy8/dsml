import csv
import pandas as pd
import numpy as np
data=pd.read_csv("Iris.csv")
X=data.iloc[:,:-1].values
print(X)
y=data.iloc[:,-1].values
print(y)


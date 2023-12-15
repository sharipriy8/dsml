import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error,r2_score
df=datasets.load_diabetes()
df['feature_names']
diabetes_X,diabetes_y=datasets.load_diabetes(return_X_y=True)
diabetes_X
diabetes_X=diabetes_X[:,np.newaxis,2]
diabetes_X.shape
diabetes_X
diabetes_X_train=diabetes_X[:-20]
diabetes_X_test=diabetes_X[-20:]
diabetes_X_test
diabetes_y_train=diabetes_y[:-20]
diabetes_y_test=diabetes_y[-20:]
diabetes_y_test
model=linear_model.LinearRegression()
model.fit(diabetes_X_train,diabetes_y_train)
diabetes_y_pred=model.predict(diabetes_X_test)
bmi=float(input("enter bmi: "))
s6=[[bmi]]
result=model.predict(s6)
print(result)
print ("coffient:\n",model.coef_)
print ("coffient of determination :%.2f"% r2_score(diabetes_y_test,diabetes_y_pred))

import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

diabetes = datasets.load_diabetes()
diabetes_X, diabetes_y = diabetes.data, diabetes.target

diabetes_X = diabetes_X[:, [0, 2, 3]]  
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]
diabetes_y_train = diabetes_y[:-20]
diabetes_y_test = diabetes_y[-20:]

regr = linear_model.LinearRegression()

regr.fit(diabetes_X_train, diabetes_y_train)

print("Coefficients: \n", regr.coef_)
print("Intercept: \n", regr.intercept_)

diabetes_y_pred = regr.predict(diabetes_X_test)

print("Mean squared error: %.2f" % mean_squared_error(diabetes_y_test, diabetes_y_pred))

print("Coefficient of determination: %.2f" % r2_score(diabetes_y_test, diabetes_y_pred))

bmi = float(input("Enter BMI: "))
bp = float(input("Enter Blood Pressure: "))
ldl = float(input("Enter Glucose: "))  
s6 = np.array([[bmi, bp, ldl]])
result = regr.predict(s6)
print("Predicted diabetes progression:", result)

import numpy as np
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
datasets=load_digits()
datasets
print(datasets.data)
print(datasets.target)
print(datasets.data.shape)
print(datasets.images.shape)
dataimageLength=len(datasets.images)
print(dataimageLength)
x=datasets.images.reshape((dataimageLength,-1))
x
y=datasets.target
y
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=0)
print(x_train.shape)
print(x_test.shape)
from sklearn import svm
model=svm.SVC()
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
from sklearn.metrics import accuracy_score
print("Accuracy of the model:{0}%".format(accuracy_score(y_test,y_pred)*100))
n=int(input("Enter the value "))
result=model.predict(datasets.images[n].reshape((1,-1)))
plt.imshow(datasets.images[n],cmap=plt.cm.gray_r,interpolation='nearest')
print(result)
print("\n")
plt.axis('off')
plt.title('%i'%result)
plt.show()

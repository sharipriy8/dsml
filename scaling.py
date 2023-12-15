import numpy as np
from sklearn import preprocessing 
input_data=np.array([
[2.1,-1.1,5.5],
[-1.5,2.4,3.5],
[0.5,-7.9,5.6],
[5.9,2.3,-5.6]
])
data_scaler_minmax=preprocessing.MinMaxScaler(feature_range=(0,1))
data_scaled_minmax=data_scaler_minmax.fit_transform(input_data)
print("\n min max scaled data:\n",data_scaled_minmax)


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('maths.csv' ,sep='\t')

x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values
y = y.reshape(-1,1)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=.1,random_state=0)

from sklearn.preprocessing import MinMaxScaler
sc_x = MinMaxScaler()
X_train = sc_x.fit_transform(x_train)
X_test = sc_x.transform(x_test)

sc_y = MinMaxScaler()
Y_train = sc_y.fit_transform(y_train)
Y_test  = sc_y.transform(y_test)


import keras
from keras.models import Sequential
from keras.layers import Dense,Dropout

model = Sequential()
model.add(Dense(units = 10, activation = 'relu', input_shape=(8,)))
model.add(Dense(units = 500, activation = 'relu'))
model.add(Dense(units = 300, activation = 'relu'))
model.add(Dense(units = 1, activation = 'sigmoid'))
model.compile(optimizer = 'adam', loss = 'mean_squared_error',metrics=['accuracy'])

model.fit(X_train,Y_train, batch_size = 5, epochs = 1000)
 
from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor(n_estimators = 300,random_state=0)
model.fit(X_train,Y_train)

dataset1 = pd.read_csv('maths - Copy.csv')
z = dataset1.iloc[1:,:].values
y_pred = model.predict(sc_x.transform(z))
Y_pred = sc_y.inverse_transform(y_pred)
Y_pred

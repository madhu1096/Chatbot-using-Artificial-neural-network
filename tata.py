import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('data.csv',header=None,sep='\t')
x = dataset.iloc[:,1].values
y = dataset.iloc[:,0].values


dataset1 = pd.read_csv('data - Copy.csv',header=None,sep='\t')
x1 = dataset1.iloc[:,1].values
y1 = dataset1.iloc[:,0].values

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
X = cv.fit_transform(x).toarray()

X1=cv.transform(x1).toarray()

'''from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, b, test_size = .5, random_state = 0)'''

a=len(X[1])
b=len(y)
b=b+1


import keras
from keras.models import Sequential
from keras.layers import Dense

# Initialising the ANN
classifier = Sequential()

# Adding the input layer and the first hidden layer
classifier.add(Dense(units = 10, activation = 'relu', input_dim = a))

# Adding the second hidden layer
classifier.add(Dense(units = 50, activation = 'relu'))

# Adding the output layer
classifier.add(Dense(units = b, activation = 'sigmoid'))

# Compiling the ANN
classifier.compile(optimizer = 'adam', loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])

# Fitting the ANN to the Training set
classifier.fit(X,y, batch_size = 10, epochs = 100)

# Part 3 - Making the predictions and evaluating the model

# Predicting the Test set results
y_pred = classifier.predict_classes(X1)
z=np.max(y_pred)


# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
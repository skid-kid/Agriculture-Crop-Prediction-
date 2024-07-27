import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import tensorflow as tf 
from tensorflow import keras
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

df = pd.read_csv("Crop_Recommendation.csv")

le = LabelEncoder()
y = df.Crop
y = le.fit_transform(y)
x = df.drop(['Crop'], axis='columns')

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=11)

model = keras.Sequential([
    keras.layers.Dense(100, activation='relu', input_shape=(X_train.shape[1],)),
    keras.layers.Dense(75, activation='relu'),
    keras.layers.Dense(50, activation='relu'),
    keras.layers.Dense(25, activation='relu'),
    keras.layers.Dense(len(np.unique(y)), activation='softmax')  # Ensure the output layer matches the number of classes
])

model.compile(optimizer='SGD',
              loss='sparse_categorical_crossentropy', 
              metrics=['accuracy'])

model.fit(X_train, y_train, epochs=100)

model.evaluate(X_test, y_test)

model.save('model.h5')

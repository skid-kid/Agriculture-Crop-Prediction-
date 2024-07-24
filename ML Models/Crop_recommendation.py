import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import tensorflow as tf 
from tensorflow import keras
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv("Crop_Recommendation.csv")

# Encode the target variable
le = LabelEncoder()
y = df.Crop
y = le.fit_transform(y)
x = df.drop(['Crop'], axis='columns')

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=11)

# Define the model architecture
model = keras.Sequential([
    keras.layers.Dense(100, activation='relu', input_shape=(X_train.shape[1],)),
    keras.layers.Dense(75, activation='relu'),
    keras.layers.Dense(50, activation='relu'),
    keras.layers.Dense(25, activation='relu'),
    keras.layers.Dense(len(np.unique(y)), activation='softmax')  # Ensure the output layer matches the number of classes
])

# Compile the model
model.compile(optimizer='SGD',
              loss='sparse_categorical_crossentropy', 
              metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=100)

# Evaluate the model
model.evaluate(X_test, y_test)

# Save the model
model.save('model.h5')

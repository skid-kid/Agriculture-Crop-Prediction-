import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('Crop_production.csv')
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
df1 = df.dropna()

print(df1.head(10))
print(df1.dtypes)
print(df1.shape)

X = df1.drop(['Area_in_hectares', 'Production_in_tons', 'Yield_ton_per_hec'], axis=1)
y = df1['Production_in_tons'] 

print(df1['State_Name'].unique())
print(df1['Crop_Type'].unique())
print(df1['Crop'].unique())

categorical_features = ['State_Name', 'Crop_Type', 'Crop']
numerical_features = ['N', 'P', 'K', 'pH', 'rainfall', 'temperature']

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_features),
        ('cat', OneHotEncoder(), categorical_features)])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', RandomForestRegressor(n_estimators=100, random_state=0))
])

pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)

from sklearn.metrics import mean_squared_error, r2_score
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
print(f"R^2 Score: {r2}")

'''plt.scatter(y_test, y_pred)
plt.xlabel("Actual Production")
plt.ylabel("Predicted Production")
plt.title("Actual vs Predicted Production")
plt.show()'''


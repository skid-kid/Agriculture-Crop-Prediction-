#importing necessary modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('Crop_production.csv')
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
df1 = df.dropna()

#print(df1.head(10))
#print(df1.dtypes)
#print(df1.shape)

#Data Cleaning
X = df1.drop(['Area_in_hectares', 'Production_in_tons', 'Yield_ton_per_hec'], axis=1)
y = df1['Production_in_tons'] 

#print(df1['State_Name'].unique())
#print(df1['Crop_Type'].unique())
#print(df1['Crop'].unique())

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

#Splitting into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', RandomForestRegressor(n_estimators=200,max_features='sqrt',max_depth=10,min_samples_leaf=1, random_state=0))
])

pipeline.fit(X_train, y_train)
import joblib
filename="model1.sav"
joblib.dump(pipeline, filename)
#y_pred = pipeline.predict(X_test)
"""
#Model evaluation using metrics
from sklearn.metrics import mean_squared_error, r2_score
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
print(f"R^2 Score: {r2}")
"""
#Used to find ideal parameters for model tuning
"""
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint

param_dist = {
    'regressor__n_estimators': randint(50, 200),
    'regressor__max_depth': randint(3, 10),
    'regressor__max_features': ['1.0', 'sqrt', 'log2'],
    'regressor__min_samples_leaf': randint(1, 5)
}

random_search = RandomizedSearchCV(estimator=pipeline, param_distributions=param_dist, n_iter=50, cv=5, scoring='neg_mean_squared_error', random_state=0)
random_search.fit(X_train, y_train)
print("Best Parameters:", random_search.best_params_)
print("Best MSE Score:", -random_search.best_score_)
"""
'''
Best Parameters: {'regressor__max_depth': 9, 'regressor__max_features': 'sqrt', 'regressor__min_samples_leaf': 1, 'regressor__n_estimators': 171}
Best MSE Score: 6962996575.035937
'''
"""
from sklearn.model_selection import GridSearchCV
param_grid = {
    'regressor__n_estimators': [50, 100, 200],
    'regressor__max_depth': [3, 5, 7, 10],
    'regressor__max_features': ['1.0', 'sqrt', 'log2'],
    'regressor__min_samples_leaf': [1, 3, 5]
}
grid_search = GridSearchCV(estimator=pipeline, param_grid=param_grid, cv=5, scoring='neg_mean_squared_error',n_jobs=-1)

grid_search.fit(X_train, y_train)
print("Best Parameters:", grid_search.best_params_)
print("Best MSE Score:", -grid_search.best_score_)
"""
'''
Best Parameters: {'regressor__max_depth': 10, 'regressor__max_features': 'sqrt', 'regressor__min_samples_leaf': 1, 'regressor__n_estimators': 200}
Best MSE Score: 6766679975.66408
'''
'''
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Production")
plt.ylabel("Predicted Production")
plt.title("Actual vs Predicted Production")
plt.show()
'''


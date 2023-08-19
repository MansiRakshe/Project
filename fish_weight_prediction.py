# -*- coding: utf-8 -*-
"""fish Weight Prediction

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IFeJLI0ivN7aqXW3boEBsN_PbQQBi86f

Fish Weight Prediction

# Step 1 : import library
"""

import pandas as pd

"""# Step 2 : import data"""

fish = pd.read_csv('https://github.com/ybifoundation/Dataset/raw/main/Fish.csv')

fish.head()

fish.info()

fish.describe()

"""# Step 3 : define target (y) and features (X)"""

fish.columns

y = fish['Weight']

X = fish[['Category','Height', 'Width', 'Length1',
       'Length2', 'Length3']]

"""# Step 4 : train test split"""

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, train_size=0.7, random_state=2529)

"""# check shape of train and test sample"""

X_train.shape, X_test.shape, y_train.shape, y_test.shape

"""# Step 5 : select model"""

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train,y_train)

model.intercept_

model.coef_

"""# Step 7 : predict model"""

y_pred = model.predict(X_test)

y_pred

"""# Step 8 : model accuracy"""

from sklearn.metrics import mean_absolute_error, r2_score

mean_absolute_error(y_test,y_pred)

r2_score(y_test,y_pred)
from keras.layers.core import Dense, Activation, Dropout
from keras.layers.recurrent import LSTM
from keras.models import Sequential
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
from pandas_datareader import data
import matplotlib.pyplot as plt
import datetime as dt
import urllib.request, json
import os
import numpy as np
from sklearn import preprocessing
from helper_methods import load_data, build_model
import math

# load training data
df = pd.read_csv('Stock CSV Files/stock_market_data-AMZN.csv')

# Sort DataFrame by date
df = df.sort_values('Date')

# normalize data
cols = [2,3,4,5,6,7]
df_subset = df[df.columns[cols]]
min_max_scaler = preprocessing.MinMaxScaler()
np_scaled = min_max_scaler.fit_transform(df_subset)
df_normalized = pd.DataFrame(np_scaled)

# Setting X and Y for training and testing
window = 5
X_train, y_train, X_test, y_test = load_data(df_normalized[::-1], window)
print("X_train", X_train.shape)
print("y_train", y_train.shape)
print("X_test", X_test.shape)
print("y_test", y_test.shape)

# Loading the model sequence structure
model = build_model([6,window,1])

# Executing the model
# Use the training set to train the model
model.fit(
    X_train,
    y_train,
    batch_size=512,
    epochs=500,
    validation_split=0.1,
    verbose=1)

# Calculate RMS/RMSE results
trainScore = model.evaluate(X_train, y_train, verbose=0)
print('Train Score: %.2f MSE (%.2f RMSE)' % (trainScore[0], math.sqrt(trainScore[0])))

testScore = model.evaluate(X_test, y_test, verbose=0)
print('Test Score: %.2f MSE (%.2f RMSE)' % (testScore[0], math.sqrt(testScore[0])))

# make a prediction
# creates states
predictions = model.predict(X_test)

# save trained model
model.save('Trained Stock Model/'+'stock_predictor.h5')

# Plot the predictions!
plt.plot(predictions ,color='red', label='Predicted Values')
plt.plot(y_test,color='blue', label='Actual Test Values')
plt.legend(loc='upper left')
plt.show()
from keras.layers.core import Dense, Activation, Dropout
from keras.layers.recurrent import LSTM
from keras.models import Sequential, load_model
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
from numpy import newaxis

# load training data
df = pd.read_csv('Stock CSV Files/stock_market_data-TWTR.csv')

# Sort DataFrame by date
df = df.sort_values('Date')

print(df)

# normalize data
cols = [2,3,4,5,6,7]
df_subset = df[df.columns[cols]]
min_max_scaler = preprocessing.MinMaxScaler()
np_scaled = min_max_scaler.fit_transform(df_subset)
df_normalized = pd.DataFrame(np_scaled)

# load trained mdel
model = load_model('Trained Stock Model/'+'stock_predictor.h5')

# compile model
model.compile(loss='mse',optimizer='rmsprop',metrics=['accuracy'])

window = 5
X_train, y_train, X_test, y_test = load_data(df_normalized[::-1], 5)
# make a prediction
# creates states
predictions = model.predict(X_test)
#print(X_test)

# Plot the predictions!
plt.plot(predictions ,color='red', label='Predicted Values')
plt.plot(y_test,color='blue', label='Actual Test Values')
plt.legend(loc='upper left')
plt.show()

'''
future = []
currentStep = X_test[:,:,:] #last step from the previous prediction


for i in range(50):
    currentStep = model.predict(X_test) #get the next step
    future.append(currentStep) #store the future steps    

predicted_values = future
print(predicted_values)

#after processing a sequence, reset the states for safety
model.reset_states()

# Plot the predictions!
plt.plot(predicted_values)
plt.show()
'''


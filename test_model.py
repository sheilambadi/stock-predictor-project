from keras.layers.core import Dense, Activation, Dropout
from keras.layers.recurrent import LSTM
from keras.models import Sequential, load_model
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
from pandas_datareader import data
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import datetime as dt
import urllib.request, json
import os
import numpy as np
from sklearn import preprocessing
from helper_methods import load_data, build_model
import math
from numpy import newaxis

# load training data
def getTickerClicked(ticker):
    # df = pd.read_csv('Stock CSV Files/stock_market_data-AAPL.csv')
    df = pd.read_csv('Stock CSV Files/stock_market_data-'+ ticker +'.csv')

    # Sort DataFrame by date
    df = df.sort_values('Date')

    # print(df)

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
    return [predictions, y_test]
    #print(X_test)

# Plot the predictions!
def plotPredictions(window, ticker):
    getTickerClicked(ticker)
    predictions1, y_test1 = getTickerClicked(ticker)
    fig = Figure(figsize=(6,4))
    a = fig.add_subplot(121)
    # The adjusted close accounts for stock splits, so that is what wes graph
    a.plot(predictions1 ,color='red', label='Predicted Values')
    a.plot(y_test1,color='blue', label='Actual Test Values')
    a.set_title(ticker + ' Model with Stock Prices Only')
    a.set_ylabel('Predicted Value (Normalized)');
    a.set_xlabel('No. of Days')
    a.legend(loc='upper left')
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.get_tk_widget().pack(side=tk.LEFT, expand=True)
    canvas.draw()


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


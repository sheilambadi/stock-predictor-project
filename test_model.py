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
    hybrid_columns = ['Date','Low','High','Close','Open','Volume', 'Adj Close', 'Polarity', 'Ticker']
    df = pd.read_csv('stock_polarity_data.csv', names = hybrid_columns)

    # Filter by stock ticker
    df = df.loc[df['Ticker'] == ticker]

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

    # Calculate RMS/RMSE results
    trainScore = model.evaluate(X_train, y_train, verbose=0)
    print('Train Score: %.2f MSE (%.2f RMSE)' % (trainScore[0], math.sqrt(trainScore[0])))

    testScore = model.evaluate(X_test, y_test, verbose=0)
    print('Test Score: %.2f MSE (%.2f RMSE)' % (testScore[0], math.sqrt(testScore[0])))
    return [predictions, y_test,testScore]

# Plot the predictions!
def plotPredictions(ticker):
    getTickerClicked(ticker)
    predictions1, y_test1, trainedScore = getTickerClicked(ticker)
    plt.plot(predictions1 ,color='red', label='Predicted Values')
    plt.plot(y_test1, color='blue', label='Actual Test Values')
    plt.title(ticker + ' Model with Stock Prices Only')
    plt.text(0.4,0.4,'RMSE is '+ str(round((math.sqrt(trainedScore[0]))*100,4))+'%', bbox=dict(facecolor='red', alpha=0.5))
    plt.ylabel('Predicted Value (Normalized)');
    plt.xlabel('No. of Days')
    plt.legend(loc='upper left')
    plt.show()
from keras.layers.core import Dense, Activation, Dropout
from keras.layers.recurrent import LSTM
from keras.models import Sequential, load_model
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
from pandas_datareader import data
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")
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

# columns
hybrid_columns = ['Date','Low','High','Close','Open','Volume', 'Adj Close', 'Polarity', 'Ticker']
# load training data
df = pd.read_csv('stock_polarity_data.csv', names = hybrid_columns)
# Sort DataFrame by date
df = df.sort_values('Date')

# normalize data
cols = [1,2,3,4,5,6,7]
df_subset = df[df.columns[cols]]
# print(df_subset)
min_max_scaler = preprocessing.MinMaxScaler()
np_scaled = min_max_scaler.fit_transform(df_subset)
df_normalized = pd.DataFrame(np_scaled)

# load trained mdel
model = load_model('Trained Stock Model/'+'hybrid_stock_predictor.h5')

# Loading the model sequence structure
window = 5
X_train, y_train, X_test, y_test = load_data(df_normalized[::-1], window)

# make a prediction
# creates states
predictions = model.predict(X_test)

def plotHybridPredictions(window):
    fig = Figure(figsize=(3,3))
    a = fig.add_subplot(122)
    # The adjusted close accounts for stock splits, so that is what wes graph
    a.plot(predictions ,color='red', label='Predicted Values')
    a.plot(y_test,color='blue', label='Actual Test Values')
    a.set_title('Stock Sentiment Hybrid Model')
    a.set_ylabel('Normalized Prices');
    a.set_xlabel('No. of Days')
    a.legend(loc='upper left')

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.get_tk_widget().pack()
    canvas.draw()
import numpy as np
from keras.models import Sequential
from keras.layers.recurrent import LSTM
from keras.layers.core import Dense, Dropout, Activation
import time

# configured to accept any amount of features.
# It is set to calculate the last feature as a result.
def load_data(stock, seq_len):
    amount_of_features = len(stock.columns)
    data = stock.as_matrix() #pd.DataFrame(stock)
    sequence_length = seq_len + 1
    result = []
    for index in range(len(data) - sequence_length):
        result.append(data[index: index + sequence_length])

    result = np.array(result)
    row = round(0.9 * result.shape[0])
    train = result[:int(row), :]
    x_train = train[:, :-1]
    y_train = train[:, -1][:,-1]
    x_test = result[int(row):, :-1]
    y_test = result[int(row):, -1][:,-1]

    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], amount_of_features))
    x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], amount_of_features))  

    return [x_train, y_train, x_test, y_test]

# build model
def build_model(layers):
    d = 0.2
    # Initialize the RNN
    model = Sequential()
    # Add the input layer and the LSTM layer
    model.add(LSTM(128, input_shape=(layers[1], layers[0]), return_sequences=True, stateful=True, batch_input_shape=(1,None,6)))
    model.add(Dropout(d))
    model.add(LSTM(64, input_shape=(layers[1], layers[0]), return_sequences=False, stateful=True))
    model.add(Dropout(d))
    # Add the output layer
    model.add(Dense(16,activation='relu',kernel_initializer='uniform'))        
    model.add(Dense(1,activation='relu',kernel_initializer='uniform'))
    # compile the RNN
    model.compile(loss='mse',optimizer='rmsprop',metrics=['accuracy'])
    return model
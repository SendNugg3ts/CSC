import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM
import pandas as pd
import numpy as np

#Dados
dadosTreino = pd.read_csv("training_data.csv")
dadosTeste = pd.read_csv("test_data.csv")
dadosTreino["record_date"] = pd.to_datetime(dadosTreino["record_date"])
dadosTreino = dadosTreino.sort_values(by='record_date', ascending=True)
dadosTreino = dadosTreino["record_date"],[""]
# Definir o modelo
seq_length = 7 # number of days to use for prediction
n_features = dadosTreino.shape[1] 
n_classes = 1

model = tf.keras.Sequential([
    tf.keras.layers.LSTM(64, input_shape=(seq_length, n_features)),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(n_classes)
])
# Compilar o modelo
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(x=dadosTeste[:-1], y=dadosTeste[1:], epochs=50, batch_size=32, verbose=1)
# Treinar o modelo
# Fazer previsões
predictions = model.predict(dadosTeste)
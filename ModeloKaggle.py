import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from datacleaner import *
bd = pd.read_csv(r"training_data.csv")

def tratar_dados(bd):
    bd = RoadsCleaner(bd)
    bd = data(bd)
    bd = valores_em_falta(bd)
    bd = eliminar(bd)
    bd = incidentsNumbers(bd)
    bd = luminosidade(bd)
    bd = rainNumbers(bd)
    bd = delayNumbers(bd)
    return bd

bd=tratar_dados(bd)

#Dados
bd = bd.sort_values(by='data', ascending=True)
bd
# Definir o modelo
seq_length = 7 # number of days to use for prediction
n_features = bd.shape[1] 
n_classes = 1

model = tf.keras.Sequential([
    tf.keras.layers.LSTM(64, input_shape=(seq_length, n_features)),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(n_classes)
])
# Compilar o modelo
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(x=bd[:-1], y=bd[1:], epochs=50, batch_size=32, verbose=1)
# Treinar o modelo
# Fazer previsões
predictions = model.predict(dadosTeste)
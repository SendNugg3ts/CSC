import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import importlib as imp
import datacleaner
imp.reload(datacleaner)

from datacleaner import *


tf.random.set_seed(1)
np.random.seed(1)
tf.keras.backend.clear_session()

bd = pd.read_csv(r"training_data.csv")

def tratar_dados(bd):
    bd = ordernar(bd)
    bd = RoadsCleaner(bd)
    #bd = data(bd)
    bd = valores_em_falta(bd)
    bd = eliminar(bd)
    bd = incidentsNumbers(bd)
    bd = luminosidade(bd)
    bd = rainNumbers(bd)
    bd = delayNumbers(bd)
    bd = removeOutlier(bd)
    indice_treino, indice_val=split_data(bd, perc=10)
    escala, bd = data_normalization(bd, norm_range=(-1, 1))
    return bd,indice_treino,indice_val,escala

bd,indice_treino,indice_val,escala=tratar_dados(bd)

#Dados
bd
serie(bd,"incidents")
newBd = bd[["incidents","record_date"]]

train, test = newBd[0:-600], newBd[-600:]


# Definir o modelo
seq_length = 7 # number of days to use for prediction
n_features = bd.shape[1] 
n_classes = 1



model_LSTM = tf.keras.Sequential([
    tf.keras.layers.LSTM(64, input_shape=(seq_length, n_features),stateful=True),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(n_classes)
])
# Compilar o modelo
model.compile(loss='mean_squared_error', optimizer='adam')

for i in range(len(dados_treino)):
    model.fit(x=bd[:-1], y=bd[1:], epochs=50, batch_size=32, verbose=1)
    model.reset_states()
    
# Treinar o modelo
# Fazer previsões
predictions = model.predict(dadosTeste)
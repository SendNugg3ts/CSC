import string
import pandas as pd
import datetime
import numpy as np 
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

bd = pd.read_csv(r"training_data.csv")


def ordernar(bd):
    bd["record_date"] = pd.to_datetime(bd["record_date"])
    bd = bd.sort_values(by='record_date', ascending=True)
    #bd["record_date"] = bd["record_date"].astype(str)
    return bd

def RoadsCleaner(bd):
    estradas=bd["affected_roads"]
    Municipal = []
    for i in estradas:
        contagem = str(i).count("EM")
        Municipal.append(contagem)

    Nacional= []
    for i in estradas:
        contagem = str(i).count("N")
        Nacional.append(contagem)
    

    Regional= []
    for i in estradas:
        contagem = str(i).count("R")
        Regional.append(contagem)    

    IC= []
    for i in estradas:
        contagem = str(i).count("IC")
        IC.append(contagem)

    bd["Estrada Nacional"]= Nacional
    bd["Estrada Regional"] = Regional
    bd["IC"] = IC
    bd ["Estrada Municipal"] = Municipal
    return bd

def data(bd):
    data=[]
    hora=[]

    for i in bd['record_date']:
        data_e_hora=datetime.datetime.strptime(i, '%Y-%m-%d %H:%M:00')
        print(data_e_hora)
        data.append(data_e_hora.date())
        hora.append(data_e_hora.time())
    bd["data"] = data
    bd["hora"]=hora
    return(bd)

def valores_em_falta(bd):
    for i in range(len(bd)):
        if bd['magnitude_of_delay'][i] == 'UNDEFINED':
            bd['magnitude_of_delay'][i] = None
    return(bd)

def eliminar(bd):
    bd.pop("city_name")
    bd.pop("avg_precipitation")
    bd.pop("affected_roads")
    #bd.pop("record_date")
    return bd


def incidentsNumbers(bd):
    bd["incidents"]= bd["incidents"].replace(["None","Low","Medium","High","Very_High"],[0,1,2,3,4])
    return bd

def luminosidade(bd):
    bd["luminosity"] = bd["luminosity"].replace(["LIGHT","LOW_LIGHT","DARK"],[0,1,2])
    return bd 

def rainNumbers(bd):
    bd["avg_rain"]= bd["avg_rain"].replace(["Sem Chuva","chuva moderada","chuva fraca","chuva forte"],[0,1,2,3])
    return bd

def delayNumbers(bd):
    bd["magnitude_of_delay"] = bd["magnitude_of_delay"].fillna("None").replace(["None","MODERATE","MAJOR"],[0,1,2])
    return bd

def split_data(training, perc=10):
    train_idx=np.arange(0,int(len(training)*(100-perc)/100))
    val_idx=np.arange(int(len(training)*(100-perc)/100+1),len(training))
    return train_idx, val_idx

def removeOutlier(bd):
    count= 0
    for valor in bd["delay_in_seconds"]:
        if valor > 5000:
            valor = 5000
            bd["delay_in_seconds"][count] = valor
        count += 1
    return bd


def serie(bd, coluna):
    plt.plot(bd["record_date"],bd[coluna])
    plt.show()

def data_normalization(bd, norm_range=(-1, 1)):
    temp = bd["record_date"]
    bd.pop("record_date")
    bd["record_date"]=temp
    numericBd=bd.iloc[:,0:-2]
    scaler = MinMaxScaler(feature_range=norm_range)
    numericBd = scaler.fit_transform(numericBd.values)
    bd.iloc[:,0:-2] = numericBd
    return scaler,bd

def datetoUnix(bd):
    listaDatas = []
    for data in bd["record_date"]:
        data =  datetime.datetime.strptime(str(data), '%Y-%m-%d %H:%M:00').timestamp()
        listaDatas.append(data)
    bd["record_date"] = listaDatas

    return bd
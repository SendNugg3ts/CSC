import string
import pandas as pd
import datetime

bd = pd.read_csv(r"training_data.csv")


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
        data_e_hora=datetime.datetime.strptime(i, '%Y-%m-%d %H:%M')
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
    return bd
import string
import pandas as pd

bd = pd.read_csv('training_data.csv')


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
    bd.drop("affected_roads")
    return bd

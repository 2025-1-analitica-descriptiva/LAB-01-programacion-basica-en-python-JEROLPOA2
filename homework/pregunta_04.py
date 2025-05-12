"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
    conteo = {}
    with open("files/input/data.csv") as f:
        for line in f:
            fecha = line.split("\t")[2]
            mes = fecha.split("-")[1]
            conteo[mes] = conteo.get(mes, 0) + 1
    return sorted(conteo.items())


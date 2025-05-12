"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    resultado = []
    with open("files/input/data.csv") as f:
        for line in f:
            partes = line.strip().split("\t")
            letra = partes[0]
            col4 = partes[3].split(",")
            col5 = partes[4].split(",")
            resultado.append((letra, len(col4), len(col5)))
    return resultado


"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    suma = {}
    with open("files/input/data.csv") as f:
        for line in f:
            partes = line.split("\t")
            letra = partes[0]
            valor = int(partes[1])
            suma[letra] = suma.get(letra, 0) + valor
    return sorted(suma.items())

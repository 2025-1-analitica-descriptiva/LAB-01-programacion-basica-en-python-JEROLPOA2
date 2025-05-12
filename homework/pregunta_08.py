"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08():
    resultado = {}
    with open("files/input/data.csv") as f:
        for line in f:
            letra, numero = line.strip().split("\t")[0], int(line.strip().split("\t")[1])
            if numero not in resultado:
                resultado[numero] = set()
            resultado[numero].add(letra)
    return sorted((k, sorted(list(v))) for k, v in resultado.items())


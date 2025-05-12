"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    conteo = {}
    with open("files/input/data.csv") as f:
        for line in f:
            col5 = line.strip().split("\t")[4]
            for par in col5.split(","):
                clave = par.split(":")[0]
                conteo[clave] = conteo.get(clave, 0) + 1
    return dict(sorted(conteo.items()))


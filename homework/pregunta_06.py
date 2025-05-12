"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    min_max = {}
    with open("files/input/data.csv") as f:
        for line in f:
            col5 = line.strip().split("\t")[4]
            for par in col5.split(","):
                clave, valor = par.split(":")
                valor = int(valor)
                if clave not in min_max:
                    min_max[clave] = [valor, valor]
                else:
                    min_max[clave][0] = min(min_max[clave][0], valor)
                    min_max[clave][1] = max(min_max[clave][1], valor)
    return sorted((k, v[0], v[1]) for k, v in min_max.items())


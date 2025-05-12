"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    suma_por_letra = {}
    with open("files/input/data.csv") as f:
        for line in f:
            partes = line.strip().split("\t")
            letra = partes[0]
            col5 = partes[4].split(",")
            suma = sum(int(par.split(":")[1]) for par in col5)
            suma_por_letra[letra] = suma_por_letra.get(letra, 0) + suma
    return dict(sorted(suma_por_letra.items()))


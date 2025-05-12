"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    suma_por_letra = {}
    with open("files/input/data.csv") as f:
        for line in f:
            partes = line.strip().split("\t")
            valor = int(partes[1])
            letras = partes[3].split(",")
            for letra in letras:
                suma_por_letra[letra] = suma_por_letra.get(letra, 0) + valor
    return dict(sorted(suma_por_letra.items()))


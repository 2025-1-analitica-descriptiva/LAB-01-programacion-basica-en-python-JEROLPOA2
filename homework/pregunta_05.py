"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    valores = {}
    with open("files/input/data.csv") as f:
        for line in f:
            partes = line.split("\t")
            letra = partes[0]
            valor = int(partes[1])
            if letra not in valores:
                valores[letra] = [valor, valor]
            else:
                valores[letra][0] = max(valores[letra][0], valor)
                valores[letra][1] = min(valores[letra][1], valor)
    return sorted((letra, maximo, minimo) for letra, (maximo, minimo) in valores.items())


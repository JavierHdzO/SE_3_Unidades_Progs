import numpy as np

archivo = open("Instancia_wine.csv","r")

normalizada = open("Norm_Instancia_Wine.csv", "w")
complementada = open("Comp_Instancia_Wine.csv", "w")

contenido = archivo.readlines()
lista = [linea.split(",") for linea in contenido]

data = np.array(lista).transpose()
data = data.tolist()
clases = data[-1]

data = data[:len(data)-1]



instancia = [list(map(float, dato[:])) for dato in data]
complemento = []


for vector in instancia:
    aux = []
    minValue = min(vector)
    maxValue = max(vector)

    for index in range(len(vector)):
        vector[index] = round((vector[index] - minValue)/(maxValue-minValue),3)
        aux.append(round(1-vector[index],3))

    complemento.append(aux)


# Volver a agregar las clases para cada instancia
instancia.append(clases)
complemento.append(clases)

## Hacer de nuevo la transpuesta de la matriz instancia (normalizada) y la matriz complemento generada

instancia = np.array(instancia).transpose().tolist()
complemento = np.array(complemento).transpose().tolist()

## Escribir los resultado en los archivos

for instan in instancia:
    aux = str(instan).replace("'","")
    print(aux)
    normalizada.write(aux[1:-3]+"\n")


for instan in complemento:
    aux = str(instan).replace("'","")
    print(aux)
    complementada.write(aux[1:-3]+"\n")

from enum import auto

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np

archivo = open("iris_completa.csv","r")
contenido = archivo.readlines()
lista = [linea.split(",") for linea in contenido]
data = np.array(lista).transpose().tolist()
data = data[:len(data)-1]
datos = [list(map(float, dato[:])) for dato in data]

print(datos)

columnas_Qi = []
columnas_IQR = []
columna_suave = []
columa_name = []

for columna in datos:
    print(f"Columna {len(columnas_Qi)+1}")
    #print(columna)
    columna_Ord = sorted(columna)
    #print(columna_Ord)
    temp_Qi = []
    temp_IQR = 0
    temp_suave = []
    columa_name.append(f"Atributo {len(columnas_Qi)+1}")
    for i in range(1,4):
        posQi_temp = (i * (len(columna)+1))/4

        print(f"PosQ{i} =  {posQi_temp}")
        parte_Entera = int(posQi_temp)
        parte_Decimal = posQi_temp - parte_Entera
        print(f"ParteEntera = {parte_Entera}")
        print(f"ParteDecimal = {parte_Decimal}")

        # el -1 es para ajustar los indices
        # al elemento que no se le resta es porque ya esta compenzado, la formula donde dice datos_ordenados[parte_entera +1] -  datos_ordenados[parte_entera]

        auxQi = round(columna_Ord[parte_Entera -1] + parte_Decimal * (columna_Ord[parte_Entera] - columna_Ord[parte_Entera -1] ),3)
        print(f"Q{i} = {auxQi}\n")
        temp_Qi.append(auxQi)

    columnas_Qi.append(temp_Qi)

    # Se calcula el IQR de la columa actual
    temp_IQR =round( temp_Qi[2]  - temp_Qi[0],3)
    # Se guara el IQR de la columna actual
    columnas_IQR.append(temp_IQR)

    #SE CALCULA SU limite suave
    auxSuaveQ1 = round(temp_Qi[0] - 1.5 * temp_IQR,3)
    auxSuaveQ3 = round(temp_Qi[2] + 1.5 * temp_IQR,3)
    print(f"Limite inferior = {auxSuaveQ1}")
    print(f"Limite superior = {auxSuaveQ3}")
    temp_suave.append(auxSuaveQ1)
    temp_suave.append(auxSuaveQ3)

    # Se guarda los limites de los outlers suaves
    columna_suave.append(temp_suave)
    print(" \n\n")





print(columnas_Qi)
print(columnas_IQR)
print(columna_suave)


gs = gridspec.GridSpec(1, 1)

plt.figure(figsize=(12, 7))

ax = plt.subplot(gs[0, :]) # row 0, span all columns
plt.boxplot(datos, labels=columa_name)
plt.title("Boxplot DEFAULT")
plt.show()









import math

archivo = open("Instancia_Iris.csv","r", encoding="utf-8-sig")
contenido = archivo.readlines()

lista = [linea.split(",") for linea in contenido]

u = []
for i in range(len(lista[0])-1):
    tempU = 0
    for j in range(len(lista)):
        tempU += float(lista[j][i])
    u.append((tempU/len(lista)))

o = []
for i in range(len(lista[0])-1):
    temp = 0
    for j in range(len(lista)):
        temp += math.pow( float(lista[j][i]) - u[i], 2)
    o.append(math.sqrt(temp/len(lista)))

Estandarizado = []
for i in range(len(lista[0])-1):
    temp = []
    for j in range(len(lista)):
        temp.append( (float(lista[j][i]) - u[i]) / o[i] )
    Estandarizado.append(temp)

archivo = open("EstandarizacionIris.txt","w", encoding="utf-8-sig")
for i in range(len(Estandarizado[0])):
    aux = ""
    for j in range(len(Estandarizado)):
        if(j == len(Estandarizado)-1):
            aux += str(Estandarizado[j][i]) + "," + str(lista[i][len(Estandarizado)])
        else:
            aux += str(Estandarizado[j][i]) + ","
    archivo.write(aux)
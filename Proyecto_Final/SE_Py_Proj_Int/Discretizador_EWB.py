archivo = open("iris_completa.csv")
contenido = archivo.readlines()
#############################################################################################
instancia = []
for i in contenido:
    instancia.append(i.split(","))
encabezados = instancia[0]
del instancia[0]
#############################################################################################

###GRUPOS A GENERAR
v_K = int(input("Ingresa la cantidad de Ks:"))
# Pagina de referencia comparativa ->>>>  https://orange.readthedocs.io/en/latest/reference/rst/Orange.feature.discretization.html#Orange.feature.discretization.Discretization

#############################################################################################
Resultados = [] #Arreglo para los atributos pero ya con las variables definidas
intervalos = []

for index_atributo in range(len(instancia[0])-1):
    auxiliar = []
    for index_registro in range(len(instancia)):
        auxiliar.append(float(instancia[index_registro][index_atributo]))
    v_max = max(auxiliar)
    v_min = min(auxiliar)
    v_width = round((v_max-v_min)/v_K, 4)

    ######################################################################
    #SE OBTIENEN LOS INTERVALOS

    temp = []
    control = round(v_min + v_width, 2)
    temp.append(control)
    for j in range(1, v_K - 1):
        control = round(control + v_width, 2)
        temp.append(control)
    intervalos.append(temp)

    ######################################################################

######################################################################
#SE DETERMINA LA VARIABLES

print(intervalos)

for i in range(len(instancia[0])-1):
    atributo = [] #Arreglo para las variables de los atributos
    for j in range(len(instancia)):

        valor = float(instancia[j][i])

        for k in range(v_K):
            if k == 0:
                if valor < intervalos[i][k]:
                    atributo.append(k+1)
            elif k == (v_K-1):
                if valor >= intervalos[i][k-1]:
                    atributo.append(k+1)
            else:
                if valor >= intervalos[i][k - 1] and valor < intervalos[i][k]:
                    atributo.append(k + 1)

    print(atributo)
    Resultados.append(atributo)

######################################################################
#SE CREA UN NUEVO ARCHIVO

archivo = open("DatosDiscretizadosIris.txt", "w")
for i in range(len(instancia)):
    cadena = ""
    for j in range(len(Resultados)):
        if(j == (len(Resultados)-1)):
            cadena += str(Resultados[j][i]) + "," + str(instancia[i][len(Resultados)])
        else:
            cadena += str(Resultados[j][i]) + ","
    archivo.write(str(cadena))

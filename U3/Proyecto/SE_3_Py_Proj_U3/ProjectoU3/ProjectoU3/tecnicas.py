import numpy as np

def KNN(pruebas, file):
    ### Corregirr el formato de casos prueba
    clasesAsignadas = []
    prueba = [[list(map(int, x[:-1]))] for x in pruebas]

    for i in range(len(prueba)):
        prueba[i].append(pruebas[i][-1])

    print(prueba)

    ###CARGAR INSTANCIA DE ENTRENAMIENTO

    archivo = open(file, "r")
    contenido = archivo.readlines()


    lista = [linea.split(",") for linea in contenido]



    instancia = [[list(map(float, x[:-1])), x[-1]] for x in lista]  # iris

    print(instancia)


    print("Total de datos de la Instancia", len(prueba))

    print("Instancia de prueba:")
    # VISUALIZA EL CONTENIDO DEL ARCHIVO
    # Impreso línea a línea
    for l in prueba:
        print(l)
    print("\n\n")

    ##############################################################################
    ###DEFINIR EL VALOR DE "K"  - Un número entre 1 y el total de registros de la instancia (entrenamiento)
    K = 10
    ##############################################################################

    contAciertos = 0  # contador de aciertos obtenidos en la clasificación

    for registroNC in prueba:  # para recorrer a todos los registros de prueba y aplicar al algoritmo K-NN
        print("Clasificación del registro: ")
        print(registroNC)  # registor de prueba procesado para su clasificacion

        NC = registroNC[0]  # vector de caracteristicas del registro actual de prueba

        estructuraDatos = {}  # inicializacion de la estructura de datos

        for NoCaso, i in enumerate(instancia):
            distancia_NC_i = Euclidiana(NC, i[0])
            # print(distancia_NC_i)
            estructuraDatos[NoCaso] = distancia_NC_i

        # print(estructuraDatos)  # La distancia de los registros con el registroNC

        ordenado = sorted(estructuraDatos.items(), key=lambda x: x[1])  # ordena los registros
        # de menor a mayor de acuerdo con la distancia con el registroNC
        # print(ordenado)

        temporalK = []
        for i in range(K):
            NoCaso = ordenado[i][0]
            # print(etiqueta)
            registro = instancia[NoCaso]
            # print(registro)
            temporalK.append(registro[1])  # obtencion de la etiqueta

        print("Clases de los vectores más cercanos al registro NC:")
        print(temporalK)  # los primeros K vectores
        print("\n\n")

        from statistics import \
            multimode  # <<<- realizado unicamente para fines academicos, no se recomienda poner la importacion aqui
        moda = multimode(temporalK)
        respKnn = moda[0]  # si existe más de una moda se queda con la primera de ellas

        print("Clase asignada por el KNN: " + str(respKnn))
        clasesAsignadas.append(respKnn)
        print("Clase Real: ", registroNC[1])#Clase del caso prueba
    return clasesAsignadas



def naiveBayes(prueba, file):

    ### Formateo de insntacia prueba
    print(prueba)

    for i in range(len(prueba)):
        for j in range(len(prueba[0])-1):
            prueba[i][j] = int(prueba[i][j])

    print(prueba)



    file2read = open(file, "r")
    file_content = file2read.readlines()
    clasesAsignadas = []
    #############################################################################################
    dataset = []
    for i in file_content:
        dataset.append((i.replace("\n", "")).split(","))
    # headers = dataset[0]
    # del dataset[0] #remove headers from dataset

    #############################################################################################
    ##count registers per class
    #############################################################################################

    probabilities = []
    auxiliar = {}
    for register_index in range(len(dataset)):
        label = dataset[register_index][-1]
        if label in auxiliar:
            auxiliar[label] += 1
        else:
            auxiliar[label] = 1
    probabilities.append(auxiliar)

    #############################################################################################
    ##count registers per attribute
    #############################################################################################
    for attribute_index in range(len(dataset[0]) - 1):
        auxiliar = {}
        for register_index in range(len(dataset)):
            v_label = dataset[register_index][attribute_index]
            v_class = dataset[register_index][-1]
            if (v_label, v_class) in auxiliar:
                auxiliar[(v_label, v_class)] += 1
            else:
                auxiliar[(v_label, v_class)] = 1
                # print(v_label, "  ", v_class)
        probabilities.append(auxiliar)
    #############################################################################################
    ##calculate probabilities per attribute
    #############################################################################################
    print(probabilities)
    for index in range(1, len(probabilities)):
        for c in probabilities[index]:  # per attribute
            # print(probabilities[0][c[1]])
            probabilities[index][c] = probabilities[index][c] / probabilities[0][c[1]]
        # print(probabilities[0][c])
    #############################################################################################
    ##calculate probabilities per class
    #############################################################################################
    for c in probabilities[0]:
        probabilities[0][c] = probabilities[0][c] / len(dataset)
        # print(probabilities[0][c])
    #############################################################################################
    ## TESTING
    #############################################################################################

    correct_classify = 0
    dataset = []
    for k in range(len(prueba)):
        register = prueba[k]
        sum = 0
        probabilities_per_class = {}
        for c in probabilities[0]:
            auxiliar = probabilities[0][c]
            for index in range(1, len(probabilities)):
                if (register[index - 1], c) in probabilities[index]:
                    auxiliar *= probabilities[index][(register[index - 1], c)]
                else:
                    auxiliar = 0  # nullify the product
            sum += auxiliar
            probabilities_per_class[c] = auxiliar

        max = -9999
        c_toAssign = ""
        for p in probabilities_per_class:
            if (sum != 0):
                probabilities_per_class[p] = probabilities_per_class[p] / sum
            else:
                probabilities_per_class[p] = 0

            if probabilities_per_class[p] > max:
                max = probabilities_per_class[p]
                c_toAssign = p

        print("Real Class: ", prueba[k][-1], "Assigned Class: ", c_toAssign, " Probability: ", round(max * 100, 4),
              "%")
        clasesAsignadas.append(c_toAssign)

        if prueba[k][-1] == c_toAssign:
            correct_classify += 1
    return clasesAsignadas
    print("\n\nCorrect Classify: ", correct_classify, " Total Evaluated: ", len(prueba), " Efficiency: ",
          round(correct_classify / len(dataset) * 100, 4), "%")


def asociadorLineal(prueba, numInstancia):
    ### Formato para casos prueba
    claseAsignadas = []
    for i in range(len(prueba)):
        for j in range(len(prueba[0])-1):
            prueba[i][j] = int(prueba[i][j])

    """
        Iris instance
        100 Iris-setosa
        010 Iris-versicolor
        001 Iris-virginica
        
        Cancer instance
        
        10 - 2
        01 - 4
        
        Wine instance
        100 - 1
        010 - 2
        001 - 3
        
        
        "Wine", "Iris", "Cancer"
    
    ## Segmento de código utilizado para codificar las instancias de prueba para cualquier instancia seleccionada
    if(numInstancia == "Iris"  or numInstancia == "Wine" ):
        for i in range(len(prueba)):
            if(prueba[i][-1] == "Iris-setosa" or prueba[i][-1] == "1" ):
                del prueba[i][-1]
                prueba[i] = prueba[i]+codificacion[0]
            elif(prueba[i][-1] == "Iris-versicolor" or prueba[i][-1] == "2"):
                del prueba[i][-1]
                prueba[i] = prueba[i]+codificacion[1]
            else:
                del prueba[i][-1]
                prueba[i] = prueba[i] +codificacion[2]
    else:
        for i in range(len(prueba)):
            if(prueba[i][-1] == "2" ):
                del prueba[i][-1]
                prueba[i] = prueba[i]+codificacion[0]
            elif(prueba[i][-1] == "4"):
                del prueba[i][-1]
                prueba[i] = prueba[i]+codificacion[1]

    prueba = [list(map(int, x[:])) for x in prueba]
    prueba = np.array(prueba).transpose().tolist()

    """
    ### Necitamos archivos ya codficados, por lo que se puede hacer un if, donde con base en la instancia
    ### se carga el archivo

    if(numInstancia == "Wine"):
        Clases = ["1", "2", "3"]
        archivo = open("codWine.csv")
    elif(numInstancia == "Iris"):
        Clases = ["Iris-setosa", "Iris-versicolor", "Iris-virginica"]
        archivo = open("codIris.csv")
    else:
        Clases = ["2", "4"]
        archivo = open("codCancer.csv")


    contenido = archivo.readlines()
    print(contenido)
    X = contenido[:(len(contenido) - len(Clases))]
    # print(X)
    X = [i.split(",") for i in X]
    X = [list(map(int, i)) for i in X]

    Y = contenido[(len(contenido) - len(Clases)):]
    Y = [i.split(",") for i in Y]
    Y = [list(map(int, i)) for i in Y]

    print(X)
    X = np.array(X)
    Y = np.array(Y)

    Paso1 = X.dot(X.T)
    Paso2 = np.linalg.inv(Paso1)
    Xpseudo = X.T.dot(Paso2)

    W = Y.dot(Xpseudo)

    print("X:")
    print(X)

    print("Y:")
    print(Y)

    print("W:")
    print(W)

    ###PRUEBA DE LA FUNCIOANLIDA DEL ASOCIADOR LINEA
    # VAMOS A PROBAR CADA UNO DE LOS CASOS PARA OBSERVAR SI LA RED ES CAPAZ DE
    # CLASIFICAR CORRECTAMENTE

    print("Prueba...")

    casosCorrectos = 0

    """
    Clases = ["Bueno", "Regular", "Malo"]
    
    for i in range(X.shape[1]):  # para cada uno de los casos/registros de prueba
        print("Prueba del Caso ", i + 1)
        casoi = X[:, i]
        print("Caso Analizado: ")
        print(casoi)

        Ycasoi = W.dot(casoi)
        print("Salidas Generadas: ")
        print(Ycasoi)

        print("Salidas Real: ")
        Yrealcasoi = Y[:, i]
        print(Yrealcasoi)

        IndexMaxYcasoi = list(Ycasoi).index(max(Ycasoi))
        IndexMaxYrealcasoi = list(Yrealcasoi).index(max(Yrealcasoi))

        if IndexMaxYcasoi == IndexMaxYrealcasoi:
            casosCorrectos += 1

        print("Clase Asignada: ", Clases[IndexMaxYcasoi])
        print("Clase Real: ", Clases[IndexMaxYrealcasoi])
        print()

    print("Total de Casos Analizados: ", X.shape[1])
    print("Total de Casos Correctos: ", casosCorrectos)
    
    print("Eficiencia del Asociador Lineal: ", casosCorrectos / X.shape[1] * 100.0)
"""

    # UTILIZACIÓN DEL ASOCIADOR LINEAL...
    for caso in prueba:
        print("\n\nPrueba de funcionamiento del asociador lineal: ")

        x = caso[:-1]
        y = caso[-1]  # <- lo calcule manualmente




        x = np.array(x)

        Ycasox = W.dot(x)

        print(Ycasox)
        IndexMaxYcasoi = list(Ycasox).index(max(Ycasox))

        print("Clase Asignada: ", Clases[IndexMaxYcasoi])
        claseAsignadas.append(Clases[IndexMaxYcasoi])
        print("Correcto " if Clases[IndexMaxYcasoi] == y else "Incorrecto")
    return  claseAsignadas

def Euclidiana(A, B):
    distancia = 0
    for i in range(len(A)):
        distancia += (A[i]-B[i])**2
    distancia = distancia ** (1/2)
    distancia = round(distancia, 2)
    return distancia




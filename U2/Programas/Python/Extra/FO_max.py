import numpy as np

m = int(input('Ingresa la cantidad de arreglos: '))
n = int(input('Ingresa la cantidad de elementos en cada arreglo: '))

VectorB = np.random.randint(0, 2, size = (m,n))

def MetodoFO(Vector):
    R = []
    for i in range(len(Vector)):
        cont = 0
        print("\n\nVector [{ite}]".format(ite = i+1))
        for j in range(len(Vector[i])):
            if Vector[i][j] == 1:
                cont+=1
            print(Vector[i][j].tolist(), end=' ')

        print("\nLa suma de 1s en el vector [{vect}] es: {conta}".format( vect = i+1, conta = cont))
        R.append(cont)

    data = str(Vector[R.index(np.max(R))])
    data = data[1:len(data)-1]
    data = data.replace(" ","")
    data = "A" + data + "G"
    print(data)
    return data


MetodoFO(VectorB)
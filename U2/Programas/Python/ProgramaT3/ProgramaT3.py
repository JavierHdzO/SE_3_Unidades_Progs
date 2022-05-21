import numpy as np

m = int(input('Ingresa la cantidad de arreglos: '))
n = int(input('Ingresa la cantidad de elementos en cada arreglo: '))

VectorB = np.random.randint(0, 2, size = (m,n))

def MetodoFO(Vector):
    for i in range(len(Vector)):
        cont = 0
        print("\n\nVector [{ite}]".format(ite = i+1))
        for j in range(len(Vector[i])):
            if Vector[i][j] == 1:
                cont+=1
            print(Vector[i][j], end=' ')
        print("\nLa suma de 1s en el vector [{vect}] es: {conta}".format( vect = i+1, conta = cont))

MetodoFO(VectorB)

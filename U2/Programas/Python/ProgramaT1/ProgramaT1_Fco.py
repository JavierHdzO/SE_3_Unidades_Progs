import random

def FO( params ):
    cont = 0
    for param in params:
        cont = cont + param
    return cont


n = int(input("Ingrese n datos: "))
array = []

for i in range(n):
    array.append(random.randrange(0,2))
    

print(array)
print( "Numeros uno encontrados: {0}".format(FO(array)) )
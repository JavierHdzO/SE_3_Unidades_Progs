
#Calcula la sumatoria de todos los nuemros comprendidos entre 1 y n, y anadelos a una lista
#Si n = 8
numeros = [1, 2, 3, 4, 5, 6, 7, 8]

n = int(input("ingresa el valor de n: "))
lista = []

#Forma clasica
for i in range(1, n+1):
    lista.append(i)
#print(lista)

#Forma con listas de comprension

n = int(input("ingresa el valor de n: "))
lista = [ i for i in range(i, n+1)]
print(lista)





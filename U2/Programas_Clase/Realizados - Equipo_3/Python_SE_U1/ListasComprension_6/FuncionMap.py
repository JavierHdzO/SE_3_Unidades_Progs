lista = [10, 15, 20, 45 ]

def checkPar(i):
    if i % 2 == 0:
        print("par")
    else:
        print("impar")


print(list(map(checkPar, lista)))

#for i in lista:
#    if i%2 == 0:
#        print("par")
#    else:
#       print("impar")





stri = "A497,430,419,373,330,238,241,230,235,232,235,240,236,tesejeG\r\n"
"""
print(stri[-3])
stri = stri[1:-3]
print(stri)
enteros = [list(map(int, stri.split(",")))]
print("array",enteros)

instancias = {"Wine.csv":"DatosDiscretizadosWine.txt", "Iris.csv": "DatosDiscretizadosIris.txt",
              "Cancer.csv":"breast-cancer-wisconsin.csv"}

print(instancias["Wine.csv"])

hola = stri.split(",")
print(hola)
"""

a = "aas\n"
print(a if a == "aas" else "no")



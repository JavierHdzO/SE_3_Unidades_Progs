import requests

def GET_SelectAllTestWine():
    #Get Instancia de pruebas de IRIS
    print("\nGET: ")
    url = "http://localhost:51744/api/Wine"
    response = requests.get(url)
    print(response.json())
    print(response.status_code)
    return response.json()

def GET_SelectAllTraininWine():
    #Get Instancia de entrenamiento de IRIS
    url = "http://localhost:51744/api/Wine/2"
    response = requests.get(url)
    print(response.json())
    print(response.status_code)
    return response.json()


def POST_InsertWine(casoPrueba):
    url = "http://localhost:51744/api/Wine"
    response = requests.post(url,json={
        "Var1": casoPrueba[0],
        "Var2": casoPrueba[1],
        "Var3": casoPrueba[2],
        "Var4": casoPrueba[3],
        "Var5": casoPrueba[4],
        "Var6": casoPrueba[5],
        "Var7": casoPrueba[6],
        "Var8": casoPrueba[7],
        "Var9": casoPrueba[8],
        "Var10": casoPrueba[9],
        "Var11": casoPrueba[10],
        "Var12": casoPrueba[11],
        "Var13": casoPrueba[12],
        "Resp": casoPrueba[13]
    })
    print(response.json())
    print(response.status_code)
    return response.json()

def DELETE_AllTestWine():
    url = "http://localhost:51744/api/Wine"
    response = requests.delete(url)
    print(response.json())
    print(response.status_code)
    return response.json()

import requests

def GET_SelectAllTestCancer():
    # Get Instancia de pruebas de CANCER
    url = "http://localhost:51744/api/cancer"
    response = requests.get(url)
    print(response.json())
    print(response.status_code)
    return response.json()


def GET_SelectAllTraininCancer():
    #Get Instancia de entrenamiento de CANCER
    url = "http://localhost:51744/api/cancer/2"
    response = requests.get(url)
    print(response.json())
    print(response.status_code)
    return response.json()


def POST_InsertCancer(v1,v2,v3,v4,v5,v6,v7,v8,v9,resp):
    ### AGREGA UN DATO A LA TABLA DE PRUEBAS CANCER
    #Post:
    url = "http://localhost:51744/api/cancer"
    response = requests.post(url,json={
        "Var1": v1,
        "Var2": v2,
        "Var3": v3,
        "Var4": v4,
        "Var5": v5,
        "Var6": v6,
        "Var7": v7,
        "Var8": v8,
        "Var9": v9,
        "Resp": resp
    })
    print(response.json())
    print(response.status_code)
    return response.json()


def DELETE_AllTestCancer():
    ### BORRA TODOS LOS DATOS DE LA TABLA CANCER ###
    #Delete
    url = "http://localhost:51744/api/cancer"
    response = requests.delete(url)
    print(response.json())
    print(response.status_code)
    return response.json()

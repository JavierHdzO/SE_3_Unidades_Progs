import requests

def GET_SelectAllTestIris():
    #Get Instancia de pruebas de IRIS
    url = "http://localhost:51744/api/Iris"
    response = requests.get(url)
    print(response.json())
    print(response.status_code)
    return response.json()

def GET_SelectAllTraininIris():
    #Get Instancia de entrenamiento de IRIS
    url = "http://localhost:51744/api/Iris/2"
    response = requests.get(url)
    print(response.json())
    print(response.status_code)
    return response.json()

def POST_InsertIris(v1,v2,v3,v4,resp):
    ### AGREGA UN DATO A LA TABLA DE PRUEBAS IRIS
    url = "http://localhost:51744/api/Iris"
    response = requests.post(url,json={
        "Var1": v1,
        "Var2": v2,
        "Var3": v3,
        "Var4": v4,
        "Resp": resp
    })
    print(response.json())
    print(response.status_code)

def DELETE_AllTestIris():
    ### BORRA TODOS LOS DATOS DE LA TABLA IRIS ###
    url = "http://localhost:51744/api/Iris"
    response = requests.delete(url)
    print(response.json())
    print(response.status_code)
    return response.json()
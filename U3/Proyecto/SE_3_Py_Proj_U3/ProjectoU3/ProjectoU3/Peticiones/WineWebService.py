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


def POST_InsertWine(v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,resp):
    url = "http://localhost:51744/api/Wine"
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
        "Var10": v10,
        "Var11": v11,
        "Var12": v12,
        "Var13": v13,
        "Resp": resp
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
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


def POST_InsertIris(casoPrueba):

    url = "http://localhost:51744/api/Iris"
    response = requests.post(url,json={
        "Var1": casoPrueba[0],
        "Var2": casoPrueba[1],
        "Var3": casoPrueba[2],
        "Var4": casoPrueba[3],
        "Resp": casoPrueba[4]
    })
    print(response.json())
    print(response.status_code)


def DELETE_AllTestIris():
    url = "http://localhost:51744/api/Iris"
    response = requests.delete(url)
    print(response.json())
    print(response.status_code)
    return response.json()
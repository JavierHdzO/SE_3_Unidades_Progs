import requests

def GET_SelectAllTestCancer():
    url = "http://localhost:51744/api/cancer"
    response = requests.get(url)
    print(response.json())
    print(response.status_code)
    return response.json()


def GET_SelectAllTraininCancer():
    url = "http://localhost:51744/api/cancer/2"
    response = requests.get(url)
    print(response.json())
    print(response.status_code)
    return response.json()


def POST_InsertCancer(casoPrueba):
    url = "http://localhost:51744/api/cancer"
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
        "Resp": casoPrueba[9]
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

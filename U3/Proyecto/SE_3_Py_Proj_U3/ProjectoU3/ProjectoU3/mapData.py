def mapeo(data):
    result =[]
    intervalos = [0, 102, 204, 306, 408, 510, 612, 714, 816, 918, 1023]

    for arreglo in data:
        temp = []
        for elemento in arreglo:
            indice = 0
            for i in range(len(intervalos)):
                if elemento >= intervalos[i]:
                    indice = i
                else:
                    break

            temp.append(indice + 1)
        result.append(temp)

    return result
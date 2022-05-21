
def Manhattan( A, B):
    d = 0;
    for i in range(len(A)):
        d += abs(A[i] - B[i])
    return d


def Euclidiana(A, B):
    d = 0
    for i in range(len(A)):
        d += (A[i] - B[i])**2
    d = d ** 0.5
    return d

def EuclidianaPro(A, B):
    d = 0
    for i in range(len(A)):
        d += (A[i] - B[i]) ** 2
    d = (d/len(A))**0.5
    return d

def DiferenciaCaracterPro(A, B):
    d = Manhattan(A, B) / len(A)
    print(d)
    return d

def  Canberra(A, B):
    d = 0
    for i in range (len(A)):
        d += abs(A[i]-B[i])/(abs(A[i])+abs(B[i]))
    return d

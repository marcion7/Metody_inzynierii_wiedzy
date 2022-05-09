import numpy as np
np.set_printoptions(suppress=True)
from numpy.linalg import matrix_rank
import math

#
#  LAB 7
#

listawek = [[0,2,1],[1,2,0]]

def QR(lista):
    A = np.array(lista)
    if matrix_rank(A) != len(A):
        raise SystemExit("Wektory są liniowo zależne!")
    else:
        listaU = [A[0]]
        for i in range(1, len(A)):
            suma_proj = 0
            for j in range(0, len(listaU)):
                proj = (np.dot(np.array(A[i]),listaU[j])/np.dot(listaU[j],listaU[j])) * listaU[j]
                suma_proj += proj
            ui = A[i] - suma_proj
            listaU.append(ui)
        Q = []
        for i in listaU:
            e = i/math.sqrt(np.dot(i.T,i))
            Q.append(e)
        Q = np.array(Q).T
        R = np.dot(Q.T, A.T)
        return Q,R
qr = QR(listawek)
#print(qr)

wektory = [[1,1,2,0],[0,-2,1,1],[2,3,0,-2],[2,0,1,0]]
#wektory = [[3,2,0],[2,0,1],[2,1,2]]
#wektory = [[1,2,5],[0,1,0],[2,5,3]]
#wektory = [[4,2,1],[3,2,2],[1,2,1]]
#wektory = [[3,2],[4,1]]

def wartosci_wlasne(lista):
    A = np.array(lista)
    if A.shape[0] == A.shape[1]:
        for _ in range(1000):
            Q = QR(A)[0]             
            Ak = Q.T @ A @ Q
            A = Ak
        return np.diag(Ak)
    else:
        raise SystemExit("Macierz nie jest kwadratowa!")

war_wlasne = wartosci_wlasne(wektory)
print(war_wlasne)
print(np.linalg.eigvals(wektory))

def wektory_wlasne(lista):
    B = []
    A = np.array(lista, float)
    war_w = wartosci_wlasne(lista)
    if A.shape[0] != A.shape[1]:
        raise SystemExit("Macierz nie jest kwadratowa!")
    else:
        for j in war_w:
            wek = np.array(lista)
            wek = wek - round(j,4) * np.eye(len(A))
            B.append(wek)
        X = []
        for a in range(len(B)):
            C = np.array(B[a])
            i = 0
            for _ in range(len(C)-1):                       
                pivot = C[i][i]
                t = i
                while pivot == 0:
                    t += 1
                    if t > (len(C)-1):
                        t = i
                    if t == i:
                        i += 1
                        pivot = C[i][i]
                        break
                    C[[i,t]] = C[[t,i]]
                    pivot = C[i][i]
                for j in range(len(C)):
                    C[i][j] /= pivot
                for k in range(len(C)):
                    if k==i or C[k][i] == 0:
                        continue
                    factor = C[k][i]
                    C[k] -= factor * C[i]
                #print(a, i, C)
                i += 1
            X.append(C)
    wek_wl = []
    for i in X:
        temp = []
        C = i
        for j in range(len(C)):
            tmp = 1
            flaga = 1
            for k in range(len(C)):
                if C[k][k] != 1:
                    flaga = 0
                tmp -= C[j][k]
            if flaga == 1:
                tmp = 1
            temp.append(round(tmp,2))
        wek_wl.append(temp)
    wek_wl = np.array(wek_wl)
    return wek_wl

wek_wlasne = wektory_wlasne(wektory)
print(wek_wlasne)
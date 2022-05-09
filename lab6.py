import numpy as np
np.set_printoptions(suppress=True)
from numpy.linalg import matrix_rank
import math

#
#  LAB 6
#

#regresja liniowa y=ax+b
#B = (xtx)-1 * xTy

# pkty
#  2 1
#  5 2
#  7 3
#  8 3

#B0 = 2/7 B1 = 5/14
#  2/7
#  5/14

# ostatni wyklad 17min albo 22min

pkty = [[2,1],[5,2],[7,3],[8,3]]

sep = ","
listapkt = []
with open('regresja.txt') as file:
    i = 0
    for line in file:
        wiersz = line.split(sep)
        listapkt.append(list(map(lambda a: float(a), wiersz)))

#print(listapkt)

def regresja_liniowa(lista):
    X = []
    Y = []
    for i in lista:
        X.append([1,i[0]])
        Y.append([i[1]])
    X = np.array(X)
    Y = np.array(Y)
    xTx = np.dot(X.T,X)
    xTy = np.dot(X.T,Y)
    B = np.array(np.dot(np.linalg.inv(xTx),xTy))
    wynik = "y = " + str(B[0]).strip("[]") + " + " + str(B[1]).strip("[]") + " * x"
    return wynik
      
reg = regresja_liniowa(listapkt)
print(reg)

listawek = [[0,2,1],[1,2,0]]

def QR(lista):
    A = np.array(lista)
    if matrix_rank(A) != len(A):
        raise SystemExit("Wetory są liniowo zależne!")
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
print(qr)

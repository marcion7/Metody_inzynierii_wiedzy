import numpy as np
np.set_printoptions(suppress=True)
import math

#
#  LAB 9
#

def wartosci_wlasne(lista):
    A = np.array(lista)
    if A.shape[0] == A.shape[1]:
        for _ in range(100):
            Q, R = np.linalg.qr(A)          
            Ak = np.dot(R,Q)
            A = Ak
        return np.diag(Ak)
    else:
        raise SystemExit("Macierz nie jest kwadratowa!")

def macierz_schodkowa(lista):
    A = np.array(lista, float)
    if A.shape[0] != A.shape[1]:
        raise SystemExit("Macierz nie jest kwadratowa!")
    else:
        C = np.array(A)
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
    return C

def wektor_wlasny(macierz):
    X = np.array(macierz)
    wek_wl = []
    for i in range(len(X)-1, -1, -1):
        if i == len(X)-1:
            wek_wl.append(1.0)
        else:
            tmp = 0
            for j in range(len(wek_wl)):
                tmp -= wek_wl[j] * X[i][i+j+1]
            tmp = round(tmp,2)
            wek_wl = [tmp] + wek_wl
    wek_wl = np.array(wek_wl)
    return wek_wl

# macierz = [[2,1,0],
#            [1,0,2],
#            [4,2,3],
#            [4,3,3]]

macierz = [[2,1,0],
           [1,0,2],
           [4,2,3]]

# macierz = [[2,1,0],
#            [1,0,2]]
       

def SVD(macierz):
    A = np.array(macierz)
    AAT = np.dot(A,A.T)
    ATA = np.dot(A.T,A)

    if np.shape(AAT)[0] > np.shape(ATA)[0]:
        war_wl = wartosci_wlasne(AAT)
        V = AAT
        U = ATA
    else:
        war_wl = wartosci_wlasne(ATA)
        V = ATA
        U = AAT

    sigmy = []
    for i in war_wl:
        sigmy.append(math.sqrt(i))

    V_znorm = []
    for i in range (len(war_wl)):
        macierz_minus_lambda = V - war_wl[i] * np.eye(len(war_wl))
        m_schodkowa = macierz_schodkowa(macierz_minus_lambda)
        wek_wl = wektor_wlasny(m_schodkowa)
        wek_wl_znorm = wek_wl/math.sqrt(np.dot(wek_wl.T,wek_wl))
        V_znorm.append(wek_wl_znorm)
    V_znorm = np.array(V_znorm)

    U_znorm = []
    if np.shape(AAT)[0] > np.shape(ATA)[0]:
        for i in range(np.shape(U)[0]):
            ui = (1/sigmy[i]) * np.dot(A.T,V_znorm[i])
            U_znorm.append(ui)
        U_znorm = np.array(U_znorm)
    else:
        for i in range(np.shape(U)[0]):
            ui = (1/sigmy[i]) * np.dot(A,V_znorm[i].T)
            U_znorm.append(ui)
        U_znorm = np.array(U_znorm)

    Sigma = np.zeros(np.shape(A))
    if np.shape(Sigma)[0] > np.shape(Sigma)[1]:
        dl = np.shape(Sigma)[1]
    else:
        dl = np.shape(Sigma)[0]
    for i in range(dl):
        Sigma[i][i] = sigmy[i]

    if np.shape(AAT)[0] > np.shape(ATA)[0]:
        #A_spr = V_znorm.T @ Sigma @ U_znorm
        return V_znorm.T, Sigma, U_znorm.T
    else:
        #A_spr = U_znorm.T @ Sigma @ V_znorm
        return U_znorm.T, Sigma, V_znorm.T
    
svd_A = SVD(macierz)
print(svd_A)

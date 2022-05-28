import numpy as np
np.set_printoptions(suppress=True)
import math

#
#  LAB 8
#

macierz = [[1, 1, 1, 0, 1, 0, 0, 0],
           [1, 1, 1, 0,-1, 0, 0, 0],
           [1, 1,-1, 0, 0, 1, 0, 0],
           [1, 1,-1, 0, 0,-1, 0, 0],
           [1,-1, 0, 1, 0, 0, 1, 0],
           [1,-1, 0, 1, 0, 0,-1, 0],
           [1,-1, 0,-1, 0, 0, 0, 1],
           [1,-1, 0,-1, 0, 0, 0,-1]]

wektor = [8,6,2,3,4,6,6,5]

def zmiana_bazy(wektor,macierz):
    B = np.array(macierz)
    BTB = np.dot(B.T,B)
    B_bez_przekanej = BTB - np.eye(len(BTB)) * np.diag(BTB) # odejmujemy od BTB wartości na głównej przekątnej
    if(B_bez_przekanej[np.where(B_bez_przekanej == 0)].size == B.shape[0] * B.shape[1]): # jeżeli liczba zer w tej macierzy jest równa ilości elementów w macierzy to znaczy że jest to macierz diagonalna
        B_znorm = []
        for w in B.T:
            dlugosc = math.sqrt(np.dot(w.T,w))
            wek_znorm = w/dlugosc
            B_znorm.append(wek_znorm)
        B_znorm = np.array(B_znorm)
        BTB_znorm = np.dot(B_znorm.T,B_znorm)
        BTB_znorm_bez_przekanej = BTB_znorm - np.eye(len(BTB_znorm)) # odejmujemy od BTB_znorm macierz jednostkową
        # zamiana bardzo małych liczb na 0
        for i in range(len(BTB_znorm_bez_przekanej)):
            for j in range(len(BTB_znorm_bez_przekanej)):
                if(np.isclose(BTB_znorm_bez_przekanej[i,j],0)):
                    BTB_znorm_bez_przekanej[i,j] = 0
        if(BTB_znorm_bez_przekanej[np.where(BTB_znorm_bez_przekanej == 0)].size == BTB_znorm.shape[0] * BTB_znorm.shape[1]): # jeżeli liczba zer w tej macierzy jest równa ilości elementów w macierzy to znaczy że jest to macierz jednostkowa
            x = np.array(wektor)
            wek_przep = np.dot(B_znorm,x)
            return wek_przep
        else:
            raise SystemExit("Macierz nie jest ortogonormalna!")        
    else:
        raise SystemExit("Macierz nie jest ortogonalna!")

wek_p = zmiana_bazy(wektor,macierz)
print(wek_p)
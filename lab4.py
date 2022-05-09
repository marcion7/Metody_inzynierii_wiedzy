import math
from asyncio.windows_events import NULL

#
# LAB 4
#

separator = ' '
lista1 = []
with open("australian.dat", "r") as file:
    for line in file:
        tmp = line.split(separator)
        lista1.append(list(map(lambda e: float(e), tmp)))


# x = [1..] x 15 klasa decyzyjna ostatni
x = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
def odleglosc(x,lista):
    listatmp = []
    suma = 0

    for i in range(len(lista)):
        for j in range(len(x)-1):
            suma += (x[j] - lista[i][j]) ** 2
        suma = math.sqrt(suma)
        #suma = round(suma,2)
        klucz = lista[i][-1]
        t = (klucz,suma)
        listatmp.append(t)
        suma = 0
    return listatmp

listatupli = odleglosc(x,lista1)
#print(listatupli)

# pogrupowac odleglosci, ktore sa przy do 0 i 1
# L<(c,odl)>
# 1. 0,1216
# 2. 0,160
# 3. 0,280
# L<(c,odl)> -> D<c,L<odl>>
# D<c,L<odl>> k-> D<c,odl> - k-nearest neigbors

def listaToSlownik(lista):
    wynik = {}
    for para in lista:
        c = para[0]
        if c not in wynik:
            wynik[c] = []
        wynik[c].append(para[1])
    return wynik

slownikLista = listaToSlownik(listatupli)
#print(slownikLista)

# wybierz k najmniejszych wartosci z kluczy i utworz nowy slownik z tymi wartosciami
# wyniki:
# 0 - 103.19
# 1 - 104.01
def k_najblizszychSasiadow(k,slownik):
    wynik = {}
    suma = 0
    for key in slownik:
        val = sorted(slownik[key])
        for j in range(k):
            suma += val[j]
        wynik[key] = suma
        suma = 0
    return wynik
    
sortslownik = k_najblizszychSasiadow(5,slownikLista)
print(sortslownik)

# 0-4 - bo najblizej
# 1-5
# 2-6

# w KNN jezeli 2 takie same wartosci to null
# DO DOMU - Napisz funkcja ktora przyjmuje c,lista,k z zad 3 i zwroci decyzje (ktora najmniejsza wartosc)

def najmniejsza_wartosc(c,lista,k):
    listatmp = []
    suma = 0
    for i in range(len(lista)):
        for j in range(len(x)-1):
            suma += (x[j] - lista[i][j]) ** 2
        suma = math.sqrt(suma)
        #suma = round(suma,2)
        klucz = lista[i][-1]
        t = (klucz,suma)
        listatmp.append(t)
        suma = 0
    slownik = {}
    for para in listatmp:
        c = para[0]
        if c not in slownik:
            slownik[c] = []
        slownik[c].append(para[1])
    wynik = {}
    suma = 0
    for key in slownik:
        val = sorted(slownik[key])
        for j in range(k):
            suma += val[j]
        wynik[key] = suma
        suma = 0
    wartosci = sorted(wynik.values())
    #print(wartosci)
    if wartosci[0] != wartosci[1]:
        return list(wynik.keys())[list(wynik.values()).index(wartosci[0])]
    else:
        return NULL

decyzja = najmniejsza_wartosc(x,lista1,15)
print(decyzja)

def odleglosc_wektorowa(lista1,lista2):
    wektortmp = []
    for i,j in zip(lista1[:-1],lista2[:-1]):
        wektortmp.append(j-i)
    wynik = 0
    for k in wektortmp:
        wynik += k**2
    wynik = math.sqrt(wynik)
    return wynik

odl_wek = odleglosc_wektorowa(lista1[0][:],lista1[1][:])
print(odl_wek)

def odl1(lista, x, k):
    slownik = {}
    wektortmp = []
    suma = 0
    for i in lista:
        for j,l in zip(i[:-1],x[:-1]):
            wektortmp.append(j-l)
        for m in wektortmp:
            suma += m**2
        tmp = math.sqrt(suma)
        kd = i[-1]
        if not kd in slownik:
            slownik[kd] = []
        slownik[kd].append(tmp)
        wektortmp = []
        suma = 0
    wynik = {}
    suma = 0
    for key in slownik:
        val = sorted(slownik[key])
        for j in range(k):
            suma += val[j]
        wynik[key] = suma
        suma = 0
    #wartosci = sorted(wynik.values())
    #print(list(wynik.keys())[list(wynik.values()).index(wartosci[0])])
    return wynik

odl_wek = odl1(lista1, x, 5)
print(odl_wek)
import math

#
# LAB 3
#

separator = ' '
lista1 = []
with open("australian.dat", "r") as file:
    for line in file:
        tmp = line.split(separator)
        lista1.append(list(map(lambda e: float(e), tmp)))

#print(lista1)

# Warunki dla funkcji metrycznej
# d(a,b) = 0 => a = b
# d(a,b) = d(b,a)
# d(a,b) + d(b,c) >= d(a,c)

# 0:1
# 0:2
# 0:3

def odl(lista1, lista2):
    wynik = 0
    for i in range(len(lista1) - 1):
        wynik += (lista1[i] - lista2[i]) ** 2
    return math.sqrt(wynik)


wynik = odl(lista1[0][:], lista1[1][:])
print(wynik)


# y = lista[0]
# d(y,x),gdzie x nalezy do listy bez indeksu 0 (bez odleglosci samego od siebie)
# zrob slownik, klucz - klasa decyzyjna, wartośc - lista z odleglosciami  dopisywac do klucza wartosci


def slownik_odl(lista):
    slownik = {}
    y = lista[0]
    for i in range(1, len(lista)):
        wynik = 0
        for j in range(len(y) - 1):
            wynik += (y[j] - lista[i][j]) ** 2
        odl = math.sqrt(wynik)
        slownik[i] = odl
    return slownik

slownik_dist = slownik_odl(lista1)
#print(slownik_dist)

def slownik_odleglosci(lista):
    tmp = []
    slownik = {}
    wynik = 0

    for i in range(len(lista)):
        for x in range(len(lista)):
            for y in range(len(lista[0])):
                wynik += math.sqrt((lista[i][y] - lista[x][y]) ** 2)
            tmp.append(round(wynik, 2))
            wynik = 0
        slownik[i] = tmp
        tmp = []
    return slownik

slownik = slownik_odleglosci(lista1)
#print(slownik)

with open("slownikodl.txt", 'w') as f:
     for key, value in slownik.items():
         f.write('%s:%s\n' % (key, value))


# obliczanie wyznacznika z macierzy kwadratowej (macierz = lista 2 wymiarowa)

def nowamacierz(macierz, i, j):
    return [wiersz[:j] + wiersz[j + 1:] for wiersz in (macierz[:i] + macierz[i + 1:])]


def wyznacznik(macierz):
    if (len(macierz) == 2):
        wynik = macierz[0][0] * macierz[1][1] - macierz[1][0] * macierz[0][1]
        return wynik

    suma = 0
    for kolumna in range(len(macierz)):
        znak = (-1) ** (kolumna)
        sub_det = wyznacznik(nowamacierz(macierz, 0, kolumna))
        suma += (znak * macierz[0][kolumna] * sub_det)

    return suma

macierz = [[3,2,0,6],[2,0,1,2],[2,1,2,0],[1,9,-2,8]]
print(wyznacznik(macierz))
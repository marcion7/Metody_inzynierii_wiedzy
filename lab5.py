import numpy as np
import math
import matplotlib.pyplot as plt

#
# LAB 5
#

separator = ' '
lista1 = []
with open("australian.dat", "r") as file:
    for line in file:
        tmp = line.split(separator)
        lista1.append(list(map(lambda e: float(e), tmp)))

lista = [2,5,6,4]
lista2 = [4,6,7,1]

# Metryka euklidesowa
def ME(lista1,lista2, utnij=False):
    if utnij:
        lista1 = lista1[:-1]
        lista2 = lista2[:-1]

    v1 = np.array(lista1)
    v2 = np.array(lista2)
    c = v1-v2
    iloczyns = np.dot(c,c)
    pierwiastek = math.sqrt(iloczyns)
    return pierwiastek

# wyklad z 28 lutego 1h 10 min

# pokoloruj losowo
# wyznacz srodek masy - oblicz dlugosc miedzy nimi,ten z najmniejszymi jest środkiem
# podmien jezeli odleglosc tej kropki jest blizej ten z klasa decyzyjna

def koloruj(lista,n,utnij=False):
    if utnij == True:
        for i in lista:
            i[-1] = np.random.randint(0,n)
    
    if utnij == False:
        for i in lista:
            i.append(np.random.randint(0,n))

    lista_kluczy = set()
    for key in lista:
        lista_kluczy.add(key[-1])
    
    for i in range(2):
        klucz_srmasy = {}
        for key in lista_kluczy:
            listatmp = []
            for j in lista:
                if j[-1] == key:
                    listatmp.append(j[:-1])

            listaodl = []
            for i in range(len(listatmp)):
                wynik = 0
                for k in range(len(listatmp)):
                    v1 = np.array(listatmp[i])
                    v2 = np.array(listatmp[k])
                    odl = ME(v1,v2)
                    wynik += odl
                listaodl.append(wynik)
            sr_masy = listatmp[listaodl.index(min(listaodl))]
            klucz_srmasy[key] = sr_masy

        for wektor in lista:
            odl_wektor_srmasy = {}
            for key in lista_kluczy:
                v1 = np.array(wektor[:-1])
                v2 = np.array(klucz_srmasy[key])
                odl = ME(v1,v2)
                odl_wektor_srmasy[key] = odl
            wektor[-1] = min(odl_wektor_srmasy, key=odl_wektor_srmasy.get)
        
    # kolorowanie środków masy
    # for wektor in lista:
    #     for key in klucz_srmasy:
    #         if (wektor[:-1] == klucz_srmasy[key]): 
    #             wektor[-1] = n
    return lista

# def koloruj2(lista,n,utnij=False):
#     if utnij == True:
#         for i in lista:
#             i[-1] = np.random.randint(0,n)
    
#     if utnij == False:
#         for i in lista:
#             i.append(np.random.randint(0,n))

#     lista_kluczy = set()
#     for key in lista:
#         lista_kluczy.add(key[-1])
    
#     klucz_srmasy = {}
#     for key in lista_kluczy:
#         listatmp = []
#         for j in lista:
#             if j[-1] == key:
#                 listatmp.append(j[:-1])

#         listaodl = []
#         for i in range(len(listatmp)):
#             wynik = 0
#             for k in range(len(listatmp)):
#                 v1 = np.array(listatmp[i])
#                 v2 = np.array(listatmp[k])
#                 odl = ME(v1,v2)
#                 wynik += odl
#             listaodl.append(wynik)
#         sr_masy = listatmp[listaodl.index(min(listaodl))]
#         klucz_srmasy[key] = sr_masy

#     for wektor in lista:
#         odl_wektor_srmasy = {}
#         for key in lista_kluczy:
#             v1 = np.array(wektor[:-1])
#             v2 = np.array(klucz_srmasy[key])
#             odl = ME(v1,v2)
#             odl_wektor_srmasy[key] = odl
#         wektor[-1] = min(odl_wektor_srmasy, key=odl_wektor_srmasy.get)
#     return lista


def ile(lista):
    klucze = set()
    for key in lista:
        klucze.add(key[-1])

    ile = {}
    for k in klucze:
        x = 0
        for i in lista:
            if i[-1] == k:
                x += 1
        ile[k] = x
    return ile


lista_kol = koloruj(lista1,2)
#print(lista_kol)

print(ile(lista_kol))

# oblicz pole powierzchi figury pod krzywa
# napisz funkcje ktora bedziez calkowala metoda monte carlo
# przejscie funkcji miedzy a do b i razy 2 dla pewnosci albo wyznacz maximum
# pkt(xa,ya)
# f(xa) = yfa
# rozlozyc pkt rownomiernie na prostokacie ile pkt jest nad pod i na
# wynik =  wspolczynnik (ile pod/ wszystkie)= (b-a) * y = calka f dx

def f(x):
    return x

def metoda_MC(a, b, n):
    dx = b - a
    wynik = 0
    for i in range(n):
        pkt = np.random.uniform(0,dx)
        wynik += f(a + pkt)
    wynik = dx * (wynik/n)
    return wynik

#pole = metoda_MC(0,1,10000)
#print(pole)

# metoda prostokątów lub trapezów dzielnie na ilosc czesci wiecej=lepiej

def metoda_prostokatow(a, b, n):
    dx = (b - a) / n
    wynik = 0
    x = a
    while x < b:
        x += dx
        pole_p = f(x) * dx
        wynik += pole_p
    return wynik

def metoda_trapezow(a, b, n):
    dx = (b - a) / n
    wynik = 0
    x = a
    while x < b:
        y = x
        x += dx
        pole_t = 1/2 * dx * (f(x) + f(y))
        wynik += pole_t
    return wynik

pole2 = metoda_prostokatow(3,17,1000)
pole3 = metoda_trapezow(3,17,1000)
#print(pole2)
#print(pole3)

# Test koloruj pyplot
lista_int = []
for i in range(100):
   lista_int.append(list(np.random.uniform(0, 1000, 2)))

test_lista = koloruj(lista_int,4)

x = []
y = []
x1 = []
y1 = []
x2 = []
y2 = []
x3 = []
y3 = []
x4 = []
y4 = []

#print(test_lista)
for i in test_lista:
    if i[-1] == 0:
        x.append(i[0])
        y.append(i[1])
    elif i[-1] == 1:
        x1.append(i[0])
        y1.append(i[1])
    elif i[-1] == 2:
        x2.append(i[0])
        y2.append(i[1])
    elif i[-1] == 3:
        x3.append(i[0])
        y3.append(i[1])
    else:
        x4.append(i[0])
        y4.append(i[1])

plt.scatter(x, y, c='coral')
plt.scatter(x1, y1, c='lightblue')
plt.scatter(x2, y2, c='pink')
plt.scatter(x3, y3, c='green')
plt.scatter(x4, y4, c='black')

plt.xlabel('x')
plt.ylabel('y')
plt.show()

# DO DOMU - metryka euklidesowa oparta o wektor i dzialania na wektorze

#iloczyn skalarny * 1
#wariancja 1/n(suma)(xi - sr(x))**2
#(wektor) * skalar(wektor(1))
#suma = aTa

def srednia_aryt(lista):
    v1 = np.array(lista)
    v2 = np.ones(len(lista))
    sr = np.dot(v1,v2)
    sr = sr/len(lista)
    return sr

sr = srednia_aryt(lista)
print(sr)
print(np.mean(lista))

# def srednia_aryt_l(lista):
#     v1 = np.array(lista)
#     srednia = 0
#     for i in range(len(v1)):
#         srednia += v1[i]
#     srednia /= len(v1)
#     return srednia
#print(srednia_aryt_l(lista))

def wariancja(lista):
    v1 = np.array(lista)
    v2 = srednia_aryt(lista) * np.ones(len(lista))
    v3 = v1 - v2
    v4 = np.dot(v3,v3.T)
    wynik = v4/len(lista)
    return wynik

war = wariancja(lista)
print(war)
print(np.var(lista))


# def wariancja_l(lista):
#     v1 = np.array(lista)
#     srednia = srednia_aryt_l(lista)
#     war = 0
#     for i in range(len(v1)):
#         war += (v1[i] - srednia)**2
#     war /= len(v1)
#     return war
#print(wariancja_l(lista))

def odchylenie_standardowe(lista):
    war = wariancja(lista)
    odchyl = np.sqrt(war)
    return odchyl

print(odchylenie_standardowe(lista))
print(np.std(lista))

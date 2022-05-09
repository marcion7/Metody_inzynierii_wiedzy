#
# LAB 2
#

def czySilne(haslo):
    dlugosc = False
    male = False
    duze = False
    wykrz = False
    if (len(haslo) >= 10):
        dlugosc = True
    z = set(haslo)
    for i in z:
        if ('A' <= i) and (i <= 'Z'):
            duze = True
        if ('a' <= i) and (i <= 'z'):
            male = True
        if i == '!':
            wykrz = True
    if dlugosc == True and male == True and duze == True and wykrz == True:
        return True
    else:
        return False


print(czySilne('P!olska21srgrsdgr'))

listanr = [3, 4, 99, 34, 86]

for i in listanr:
    if i == 99:
        continue
    print(i)


def czyNalezy(lista, i):
    j = 0
    flaga = False
    while j < len(lista):
        if lista[j] == i:
            flaga = True
        j += 1
    return flaga


print(czyNalezy(listanr, 34))

with open("plik.txt", "r") as file:
    for i in file:
        print(i, end='') # z end są odstępy bez nie ma

jezyki = ["Python", "C", "C++", "Java"]

with open("plik.txt","w") as plik:
    for i in jezyki:
        print(i, file=plik)

miasta = ["Olsztyn", "Warszawa", "Kraków", 'Białystok']

print(list(map(lambda i : i[:3], miasta)))

pliki = ["tekst.txt", "program.exe", "word.docx"]

def roz(lista, rozsz):
    lista2 = []
    for i in lista:
        if i.endswith('.' + rozsz):
            lista2.append(i)
    return lista2

def roz2(lista, rozsz):
    for i in lista:
        if i.endswith('.' + rozsz):
            yield i


for i in roz2(pliki, 'txt'):
    print(i)
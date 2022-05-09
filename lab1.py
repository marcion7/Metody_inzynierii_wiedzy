#
# LAB 1
#

print('Podaj swoje imię:') 
n = input()
print('Cześć ' + n)

lista = ["cos", "tam", "no", "ooo", "aaa"]
y = '#'.join(lista)
print(y)
x = y.split("#")
print(x)

print("{:s}, {:d}, {:f}".format('string', 56, 3))

text = "Metody Inżynierii Wiedzy Są Najlepsze"
print("{0}, {1}".format(text, len(text)))
x = text.lower()
print("{0}, {1}".format(x, len(x)))

bezpol = text.replace('ż', 'z').replace('ą', 'a').replace(" ", "")
print("{0}, {1}".format(bezpol, len(bezpol)))

z = set(bezpol)
print("{0}, {1}".format(z, len(z)))

string = "takiecos"
liczba = 50
razem = (string, liczba)
print(type(razem))

lista = ["C", "C++", "Python", "Java", "HTML"]
print(lista.index("Python"))

lista2 = ["1", "2", "3"]
print(lista)
print(lista2)
print(lista + lista2)
lista.extend(lista2)
print(lista)

lista2.insert(2, "Babcia")
print(lista2)

slownik = {
    "Polska": "Warszawa",
    "Niemcy": "Berlin",
    "Rosja": "Moskwa",
    "Litwa": "Wilno",
    "Białoruś": "Mińsk"
}

print(sorted(slownik))

# Do domu przesortuj słownik (w środku)

print(sorted(slownik.items()))

print(bool(" "))
print(bool(""))
print(bool("1"))
print(bool("0"))
print(bool(["", ""]))

zdanie = input('Wpisz zdanie: ')
z = set(zdanie)
if len(z)>15:
   print("Zdanie ma więcej niż 15 unikalnych znaków")
else:
   print("Zdanie nie ma więcej niż 15 unikalnych znaków")

if "j" in zdanie:
  print("Jest")

for i in range(10):
   print(i)

l = ["cos", "tam", "no", "ooo", "aaa"]
y = '#'.join(l)
print(y)
# x = y.split('#')
# print(x)

tmp = ''
for i in y:
    if i != '#':
        tmp += i
    else:
        print(tmp)
        i = ''
        tmp = ''
print(tmp)

tmp = ''
tmplista = []
for i in y:
    if i != '#':
        tmp += i
    else:
        tmplista.append(tmp)
        i = ''
        tmp = ''
tmplista.append(tmp)
print(tmplista)


# wyznacznik macierzy(kwadratowej)

def wyznacznik(macierz):
    if len(macierz) == 2 and len(macierz[0]) == 2:
        det = macierz[0][0] * macierz[1][1] - macierz[1][0] * macierz[0][1]
        return det

    if len(macierz) == 3 and len(macierz[0]) == 3:
        m11 = [macierz[1][1:], macierz[2][1:]]
        m12 = [macierz[1][0:3:2], macierz[2][0:3:2]]
        m13 = [macierz[1][:2], macierz[2][:2]]
        det = macierz[0][0] * wyznacznik(m11) - macierz[0][1] * wyznacznik(m12) + macierz[0][2] * wyznacznik(m13)
        return det

    if len(macierz) == 4 and len(macierz[0]) == 4:
        m11 = [macierz[1][1:], macierz[2][1:], macierz[3][1:]]
        m12 = [macierz[1][:1] + macierz[1][2:], macierz[2][:1] + macierz[2][2:], macierz[3][:1] + macierz[3][2:]]
        m13 = [macierz[1][:2] + macierz[1][3:], macierz[2][:2] + macierz[2][3:], macierz[3][:2] + macierz[3][3:]]
        m14 = [macierz[1][:3], macierz[2][:3], macierz[3][:3]]
        det = macierz[0][0] * wyznacznik(m11) - macierz[0][1] * wyznacznik(m12) + macierz[0][2] * wyznacznik(m13) - \
              macierz[0][3] * wyznacznik(m14)
        return det


macierz2x2 = [
    [1, 3],
    [-5, 6]]

macierz3x3 = [
    [1, 3, 7],
    [-5, 6, -4],
    [-6, 2, 10]]

macierz4x4 = [
    [1, 3, 7, 6],
    [-5, 6, -4, -7],
    [-6, 2, 10, -3],
    [4, -8, 3, 2]]


# print(wyznacznik(macierz2x2))
# print(np.linalg.det(macierz2x2))

# print(wyznacznik(macierz3x3))
# print(np.linalg.det(macierz3x3))

# print(wyznacznik(macierz4x4))
# print(np.linalg.det(macierz4x4))

from math import sqrt
dane = [list(map(int, w.strip().split())) for w in open('punkty.txt')]
#print(dane)

#zad4.1
licznik = 0
def czy_pierwsza(liczba):
    global licznik
    licznik = 0
    for x in range(1, liczba // 2):
        if liczba % x == 0:
            licznik += 1
    return licznik == 1
#print(czy_pierwsza(16))

#zad4.1
ile = 0
for x in dane:
    if czy_pierwsza(x[0]) and czy_pierwsza(x[1]):
        ile += 1
#print(ile)

#zad4.2
l1 = ()
l2 = ()
def czy_cyfropodobne(liczba1, liczba2):
    return set(str(liczba1)) == set(str(liczba2))

#print(czy_cyfropodobne(1234, 4123123))
ile2 = 0
for x in dane:
    if czy_cyfropodobne(x[0], x[1]):
        ile2 += 1
#print(ile2)

#zad4.3
#print(dane)
max_odl = 0
xy1 = []
xy2 = []
for x in dane:
    for y in dane:
        odl = sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)
        if odl > max_odl:
            max_odl = odl
            xy1 = x
            xy2 = y
print(f"max odległość: {round(max_odl, 0)} \nwspółrzędne 1 punktu: {xy1} \nwspółrzędne 2 punktu: {xy2}")

#zad4.4
wew = 0
boki = 0
zew = 0
for x in dane:
    if -5000 < x[0] < 5000 and -5000 < x[1] < 5000:
        wew += 1
    elif x[0] == 5000 or x[1] == 5000:
        boki += 1
    else:
        zew += 1
print(wew, boki, zew)
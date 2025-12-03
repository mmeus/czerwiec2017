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

ile = 0
for x in dane:
    if czy_pierwsza(x[0]) and czy_pierwsza(x[1]):
        ile += 1
print(ile)


n = 100
Czyjest = [False] * (n + 1)
i_2, i_3, i_5, i_9, ile_i = 0, 0, 0, 0, 0
def sitko(n):
    global Czyjest, i_2, i_3, i_5, i_9, ile_i
    for i in range(n + 1):
        Czyjest[i] = False
    j = 1
    while j * j < n:
        j += 1
    print(j)
    for i in range(2, j + 1):
        kw = i * i
        poz = kw
        while poz <= n:
            ile_i += 1
            if i == 2:
                i_2 += 1
            elif i == 3:
                i_3 += 1
            elif i == 5:
                i_5 += 1
            elif i == 9:
                i_9 += 1
            Czyjest[poz] = True
            poz = poz + kw

#zad1.1
'''sitko(10)
print(Czyjest[5])

sitko(100)
print(Czyjest[10], Czyjest[75])'''

#zad1.2
sitko(100)
print(i_2, i_3, i_5, i_9)

print(ile_i)
#odp: x, -, x, x

#zad1.3
def czy_kwadratowa(Czyjest, k):
    return Czyjest[k]
for k in range(n):
    sitko(n)
    czy_kwadratowa(Czyjest, k)
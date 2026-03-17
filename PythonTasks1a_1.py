"""
Zadania z pliku PythonTasks1a_1
"""
zadanie = 1
# 1.    Używając dwóch pętli for napisz funkcję, który wypisze tabliczkę mnożenia od 1 do 10 w formie tabeli.
print(f"Zadanie {zadanie}")
zadanie += 1
for i in range(1, 11):
    for j in range(1, 11):
        print(j * i, end="\t")
    print()
print()

# 2.    Używając dwóch pętli for napisz funkcję, która narysuje prostokąt z gwiazdek. Funkcja na wejściu ma przyjmować szerokość oraz wysokość prostokąta. Przykładowo height=3 i width=5
print(f"Zadanie {zadanie}")
zadanie += 1
def rysuj_prostokat(height = 3, width = 5):
    for i in range(height):
        for j in range(width):
            print("*",end='')
        print()
rysuj_prostokat()
print()

# 3.	Używając dwóch pętli for napisz funkcję, która narysuje przekątne w kwadracie o boku n, które są nieparzyste.
# 3a.   Dodatkowo, możesz obsłużyć liczby parzyste poprzez narysowanie przekątnych w poniższy sposób
print(f"Zadanie {zadanie}")
zadanie += 1
def rysuj_przekatne_kwadratu(n):
    # n jest nieparzyste i większe lub równe 3
    if n >= 3 and n % 2 != 0:
        przekatne = n + n - 1
        srodek = n - n // 2
        odleglosc = 1
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i == srodek and j == srodek:
                    # srodek
                    print("*", end='')
                    przekatne -= 1
                elif i < srodek and (j == i or j == n + 1 - i):
                    # przekatne
                    print('*', end='')
                    przekatne -= 1
                elif i > srodek and (srodek - odleglosc == j or srodek + odleglosc == j):
                    # przekatne
                    print('*', end='')
                    przekatne -= 1
                else:
                    print(' ', end='')
            if i > srodek:
                odleglosc += 1
            print()
        else:
            if przekatne != 0:
                print("Coś poszło nie tak")
    #  n jest parzyste i większe niż 3
    elif n > 3 and n % 2 == 0:
        przekatne = 2 * n
        odleglosc = 1
        srodek = n / 2
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if (i == srodek or i == srodek + 1) and (j == srodek or j == n + 1 - srodek):
                    #  srodek
                    print('*', end='')
                    przekatne -= 1
                elif i < srodek and (j == i or j == n + 1 - i):
                    # przekatne
                    print('*', end='')
                    przekatne -= 1
                elif i > srodek + 1 and (srodek - odleglosc == j or srodek + 1 + odleglosc == j):
                    # przekatne
                    print('*', end='')
                    przekatne -= 1
                else:
                    print(' ', end='')
            if i > srodek + 1:
                odleglosc += 1
            print()
        else:
            if przekatne != 0:
                print("Coś poszło nie tak")
    else:
        print("Podane n jest za małe by to narysować")

rysuj_przekatne_kwadratu(6)
print()

# 4.	Napisz funkcję, która dla liczby n wypisze piramidę z gwiazdek. Przykładowo dla n=3
print(f"Zadanie {zadanie}")
zadanie += 1
def rysuj_piramide(n = 3):
    if n > 3:
        if n % 2 != 0:
            odleglosc = n // 2
            znak = ' '
            for i in range(1, n + 1, 2):
                print(znak * odleglosc, '*' * i, znak * odleglosc, sep='')
                odleglosc -= 1
        else:
            odleglosc = (n - 2) // 2
            znak = ' '
            for i in range(2, n + 1, 2):
                print(znak * odleglosc, '*' * i, znak * odleglosc, sep='')
                odleglosc -= 1
    else:
        print("N jest za małe")

rysuj_piramide(8)
print()

# 5.	Napisz funkcję, która dla przekazanej na wejściu listy list obliczy sumę wszystkich elementów.
print(f"Zadanie {zadanie}")
zadanie += 1
def suma_listy(lista:list) -> int:
    suma = 0
    for elem in lista:
        suma += elem

    return suma

lista = [1,2,3,4,5]
print("Suma listy {} wynosi: {}".format(lista, suma_listy(lista)))
print()

"""
6.	Napisz funkcję, która narysuje szachownicę używając znaków „#” i „ ”.
# # # #
  # # # #
# # # # 
"""
print(f"Zadanie {zadanie}")
zadanie += 1
# def szachownica(n = 3):
#     for i in range(1, n + 1):
#         if i % 2 == 0:
#             print(' ', end='')
#         for j in range(1, n + 2):
#             if i % 2 != 0:
#                 print('#', end=' ')
#             else:
#                 if j < n + 1:
#                     print('#', end=' ')
#                 else:
#                     print('#', end='')
#         print()

def szachownica(n = 3):
    tab = ['#' for x in range(n)]
    for i in range(1, n + 1):
        if i % 2 != 0:
            print(" ".join(tab))
        else:
            print(" ", " ".join(tab), sep='')

szachownica()
print()

# 7.	Napisz funkcję, która narysuje bardziej zaawansowaną szachownicę. Użyj w tym celu znaków +, - i |.
print(f"Zadanie {zadanie}")
zadanie += 1
def zaawansowana_szachownica():
    numer_linii = 8
    znak = 65
    for i in range(1 , 19):
        for j in range(1, 19):
            if i % 2 == 0:
                if j == 1 and i != 18:
                    print(numer_linii, end='\t')
                    numer_linii -= 1
                elif j % 2 == 0 and i != 18:
                    print('|', end='')
                elif i == 18:
                    if j >= 3 and j % 2 != 1:
                        print(' ', chr(znak), '', sep='', end=' ')
                        znak += 1
                    elif j == 1:
                        print('\t', end='')
                    else:
                        print(' ', end='')
                else:
                    print('   ', end='')
            else:
                if j == 1 and i != 18:
                    print('\t', end='')
                elif j % 2 == 0:
                    print('+', end='')
                else:
                    print('---', end='')
        print()

zaawansowana_szachownica()
print()

"""
8.	Napisz funkcję do obliczania sumy wybranej kolumny, lub wiersza w macierzy. Przykładowo, dla wiersza 1 i kolumny 1 i macierzy:
[[1,2,3],
  [4,5,6],
  [7,8,9]]
Suma wiersza 1 = 6
Suma kolumny 1 = 12
"""
print(f"Zadanie {zadanie}")
zadanie += 1
def suma_kolumny_wiersza(macierz, wiersz, kolumna):
    suma_w = 0
    suma_k = 0
    if wiersz < len(macierz) and kolumna < len(macierz):
        for elem in range(len(macierz)):
            suma_w += macierz[wiersz - 1][elem]
            suma_k += macierz[elem][kolumna - 1]
    else:
        print("Podany wiersz/kolumna jest niepoprawna")

    return suma_w, suma_k

macierz = [[1,2,3],[4,5,6],[7,8,9]]
suma_w, suma_k = suma_kolumny_wiersza(macierz,1,1)
print("Macierz: {}\nSuma wiersza: {}\nSuma kolumny: {}".format(macierz, suma_w, suma_k))
print()

# 9.	Napisz funkcję, która dla liczby n wypisze piramidę z gwiazdek, która ma pusty środek. Przykładowo dla n=3
print(f"Zadanie {zadanie}")
zadanie += 1
def rysuj_piramida_pusty_srodek(n = 3):
    podstawa = n + n - 1
    odleglosc = n - 1
    znak = 1
    przerwa = 1
    if n % 2 != 0:
        for i in range(1, n + 1):
            if znak == 1:
                print(' ' * odleglosc, '*', ' ' * odleglosc, sep='')
                znak += 1
                odleglosc -= 1
            elif i == n:
                print('*' * podstawa)
            else:
                print(' ' * odleglosc, '*', ' ' * przerwa, '*', ' ' * odleglosc, sep='')
                przerwa += 2
                odleglosc -= 1
    else:
        print("N musi być nieparzyste")
rysuj_piramida_pusty_srodek(3)
print()

# 10.	Napisz funkcję, która dla liczby n wypisze piramidę z gwiazdek do góry nogami. Przykładowo dla n=3
print(f"Zadanie {zadanie}")
zadanie += 1
def rysuj_piramide_odwrotnie(n = 3):
    odleglosc = 0
    for i in range(n, 0, -2):
        print(' ' * odleglosc, '*' * i, ' ' * odleglosc, sep='')
        odleglosc += 1

rysuj_piramide_odwrotnie(5)
print()

"""
11.	Napisz funkcję, która wygeneruje trójkąt Pascala dla zadanej wysokości n. Wypisany trójkąt nie musi być przesuwany. Wypisz zwyczajnie wartości, np.
1
1 1
1 2 1
1 3 3 1
"""
print(f"Zadanie {zadanie}")
zadanie += 1
def rysuj_trojkat_Pascala(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            if j == 1:
                print(j, end=' ')
            elif j == i:
                print(1, end=' ')
            else:
                print(i - 1, end=' ')
        print()

# def rysuj_trojkat_Pascala(n):
#     for i in range(1, n + 1):
#         if i <= 2:
#             print('1' * i, sep=' ')
#         else:
#             print('1', f'{i - 1}' * (i - 1), '1', sep=' ')

rysuj_trojkat_Pascala(5)
print()

"""
12.	Napisz funkcję, która wypisze wszystkie możliwe kombinacje dla n rzuconych kostek sześciościennych. Dla n=2:
(1, 1) = 2
(1, 2) = 3
…
(6, 6) = 12
"""
print(f"Zadanie {zadanie}")
zadanie += 1
def kostka_kombinacja(n = 2):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print("({}, {}) = {}".format(i, j, i + j))

kostka_kombinacja(3)
print()

"""
13.	*Napisz funkcję, która utworzy spiralę liczb w kwadracie o boku n. Przykładowo dla n=3
1 2 3
8 9 4
7 6 5
"""
print(f"Zadanie {zadanie}")
zadanie += 1
def rysuj_spirale_liczb(n = 4):
    ilosc_liczb = n * n
    liczby = [[0] * n for x in range(n)]
    liczba = 1
    start = 0
    koniec = n - 1
    pierwszy_krok = True
    while ilosc_liczb:
        gora = start
        dol = koniec
        prawo = koniec
        lewo = start

        if n % 2 == 0:
            pierwszy_krok = True
        else:
            lewo -= 1

        # w prawo
        while lewo != prawo:
            if pierwszy_krok and n % 2 == 0:
                lewo = start
                pierwszy_krok = False
            elif pierwszy_krok and n % 2 != 0:
                lewo = start
                pierwszy_krok = False
            else:
                lewo += 1
            liczby[gora][lewo] = liczba
            liczba += 1
            ilosc_liczb -= 1

        lewo = start
        if ilosc_liczb == 0:
            break

        # w dół
        while gora != dol:
            gora += 1
            liczby[gora][prawo] = liczba
            liczba += 1
            ilosc_liczb -= 1

        gora = start + 1
        if ilosc_liczb == 0:
            break

        # w lewo
        while lewo != prawo:
            prawo -= 1
            liczby[dol][prawo] = liczba
            liczba += 1
            ilosc_liczb -= 1

        prawo = koniec - 1
        if ilosc_liczb == 0:
            break

        # w górę
        while dol != gora:
            dol -= 1
            liczby[dol][lewo] = liczba
            liczba += 1
            ilosc_liczb -= 1

        koniec -= 1
        start += 1

    for i in range(n):
        for j in range(n):
            print(liczby[i][j], end='\t')
        print()


rysuj_spirale_liczb(7)
print()

"""
14.	Napisz funkcję, która na wejściu przyjmie dowolny tekst i wyświetlając go otoczy go gwizdkami. Przykładowo dla tekst=”Hello World”
***********
*Hello World*
***********
"""
print(f"Zadanie {zadanie}")
zadanie += 1
def otocz_tekst_gwiazdkami(tekst):
    if type(tekst) is list:
        rozmiar = len(tekst)
        for i in range(rozmiar):
            if i == 0:
                gwiazdki = len(tekst)
            else:
                if gwiazdki < len(tekst[i]):
                    gwiazdki = len(tekst[i])

        gwiazdki += 5
        for i in range(rozmiar + 2):
            if i == 0 or i == rozmiar + 2 - 1:
                print('*' * gwiazdki)
            else:
                roznica = gwiazdki - len(tekst[i - 1]) - 5
                print('*', tekst[i - 1], ' ' * roznica, '*', sep=' ')
    elif type(tekst) is str:
        gwiazdki = len(tekst) + 4
        for i in range(3):
            if i != 1:
                print('*' * gwiazdki)
            else:
                print('*', tekst, '*', sep=' ')
    else:
        print("Podany argument nie jest napisem ani lista")


tekst = "Hello World"
otocz_tekst_gwiazdkami(tekst)
tekst = ["Hello World",
         "Dzisiaj robimy zadania z mentoringu"]
otocz_tekst_gwiazdkami(tekst)

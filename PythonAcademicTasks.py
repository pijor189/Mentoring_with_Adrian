"""
Zadania z pliku PythonAcademicTasks.py
"""
zadanie = 1

"""
1)	[SumSearch] Mając na wejściu dowolną listę liczb całkowitych zwróć indeksy liczb, które będą się składać na poszukiwaną sumę liczb. 
Możesz założyć, że w liście znajduję się tylko jedno rozwiązanie. 
Przykład: 
Dane wejściowe: liczby = [3, 5, 7, 12], poszukiwana suma = 10
Dane wyjściowe: [0, 2]
Ponieważ liczby[0] + liczby[2] = 10
"""
print(f"\nZadanie {zadanie}\n")
zadanie += 1

liczby = [3, 5, 7, 8, 12, 21, 4]
suma = 22                   # poszukiwana suma liczb

"""for key, value in enumerate(liczby):
    for i in range(key + 1, len(liczby)):
        if value + liczby[i] == suma:
            print(f"Liczby spod indeksów {key} oraz {i} dają wartość {suma}")
            break           # jeśli zakładamy, że ma się znajdować tylko jedno rozwiązanie"""

"""def znajdz_sume_liczb(liczby: list, suma: int) -> None:
    if suma in liczby:
        return print(f"Liczba spod indeksu {liczby.index(suma)} daje nam poszukiwaną sumę: {suma}")
    tmp = sorted(liczby.copy(), reverse=True)
    tmp2 = []
    for key, value in enumerate(tmp):
        if len(tmp2) > 1:
            break
        #   sprawdza czy wartość liczby spod tego indeksu jest większa niż poszukiwana suma
        if suma < value:
            #   sprawdzaj kolejną
            continue
        else:
            # reszta której szukamy
            tmp1 = suma - value
            # zapisz indeks pierwszej liczby w kombinacji
            tmp2 = [liczby.index(value)]
            if tmp1 in liczby:
                # suma dwóch liczb daje nam poszukiwaną wartość, wpisz indeks drugiej z liczb
                tmp2.append(liczby.index(tmp1))
                # zakładając, że jest tylko jedno rozwiązanie, przerwij dalsze poszukiwania
                break
            else:
                # jeśli kombinacja 3 lub więcej liczb daje poszukiwaną wartość
                tmp3 = sum(liczby) - suma
                if tmp3 in tmp:
                    # suma n - 1 liczb daje nam poszukiwaną wartość
                    tmp.pop(tmp.index(tmp3))
                    tmp2 = [liczby.index(x) for x in tmp]
                    # suma tych liczb daje nam wartość poszukiwaną, zakładając, że jest jedno rozwiązanie, przerwij dalsze poszukiwanie
                    break
                else:
                    # tutaj chyba trochę mogłem przekombinować, nie jest to zbyt zoptymalizowane, ale działa
                    for i in range(key + 1, len(tmp)):
                        for j in range(i + 1, len(tmp)):
                            if tmp[i] + tmp[j] == tmp1:
                                tmp2.append(liczby.index(tmp[i]))
                                tmp2.append(liczby.index(tmp[j]))
                                break
                        if len(tmp2) > 1:
                            break"""

def znajdz_sume_liczb(liczby: list, suma: int) -> None:
    if len(liczby) == 0:
        return print("Została przekazana pusta tablica, nie ma jak znaleźć poszukiwanej sumy")
    if suma == 0:
        return print("Suma nie może być 0")
    if suma in liczby:
        return print(f"Liczba spod indeksu {liczby.index(suma)} daje nam poszukiwaną sumę: {suma}")
    # poszukiwanie jednej nie pasującej liczby z ciągu do sumy
    reszta = sum(liczby) - suma
    # dla n - 1
    if reszta in liczby:
        tmp = [liczby.index(x) for x in liczby if x != reszta]
        return print(f"Liczby spod indeksów {tmp} dają wartość {suma}")
    # wykluczamy liczby większe od poszukiwanej sumy
    tmp = [x for x in liczby if x < suma]





    print(f"Liczby spod indeksów {0} dają wartość {suma}")


znajdz_sume_liczb(liczby, suma)

"""
2)	[StockPlayer] Mając do dyspozycji listę cen za złoto, napisz algorytm, który będzie w stanie kupować i sprzedawać je tak, aby zarobić jak najwięcej. 
W danej chwili możesz mieć tylko jeden zakup. 
Przykład:
Dane wejściowe: ceny złota = [7,1,5,3,6,4]
Dane wyjściowe: 7
Ponieważ kupno drugiego dnia (1) i sprzedaż trzeciego (5) to zysk 4zł. Następnie zakup czwartego dnia (3) i sprzedaż piątego (6) to kolejny zysk 3zł. Co łącznie daje 7zł zysku. 
"""
print(f"\nZadanie {zadanie}\n")
zadanie += 1

cena_zlota = [7,1,5,3,6,4]
srednia = sum(cena_zlota) / len(cena_zlota)
zysk = 0
zloto = 0
for cena in cena_zlota:
    # sprawdzamy czy warto kupić złoto tego dnia
    if cena <= srednia:
    # kupno
        zloto -= cena
    else:
        # sprawdzamy, czy mamy złoto, żeby je sprzedać
        if zloto != 0:
            # sprzedaż
            zloto += cena
# na koniec ostatniego dnia sprzedajemy, by obliczyć ostateczny zysk
if cena == cena_zlota[-1]:
    zloto += cena

print(f"Zysk z inwestycji w złoto: {zloto}")

"""
3)	[Palindrom] Napisz funkcje, która sprawdzi czy dany ciąg tekstowy jest palindromem.
Przykład: 
Dane wejściowe: tekst = [„Kajak”]
Dane wyjściowe: True

Dane wejściowe: tekst = [„Rower”]
Dane wyjściowe: False

Dane wejściowe: tekst = [„Ikar bada braki”]
Dane wyjściowe: True
"""
print(f"\nZadanie {zadanie}\n")
zadanie += 1

def czy_palindrom(tekst: list) -> bool:
    tmp = tekst[0]
    tmp = tmp.lower().replace(" ", "")
    if tmp[::] == tmp[::-1]:
        return True
    else:
        return False

tekst = ["Kajak"]
print(f"Czy tekst {tekst} jest palindromem?: {czy_palindrom(tekst)}")
tekst = ["Rower"]
print(f"Czy tekst {tekst} jest palindromem?: {czy_palindrom(tekst)}")
tekst = ["Ikar bada braki"]
print(f"Czy tekst {tekst} jest palindromem?: {czy_palindrom(tekst)}")

"""
4)	[FizzBuzz] Napisz funkcję która w danym ciągu liczbowym zastąpi liczby stringami według poniższej reguły
•	Jeśli liczba jest podzielna przez 3 i 5 napisz „FizzBuzz”
•	Jeśli liczba jest podzielna przez 3 napisz „Fizz”
•	Jeśli liczba jest podzielna przez 5 napisz „Buzz”
•	Jeśli liczba nie spełnia powyższych warunków, napisz ją w formie stringa


Przykład: 
Dane wejściowe: n = 15
Dane wyjściowe: ["0”, "1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
"""
print(f"\nZadanie {zadanie}\n")
zadanie += 1

"""def zadanie_fizz_bizz(n: int) -> list:
    lista = [0]
    for val in range(1, max(n + 1, 1)):
        if val % 3 == 0 and val % 5 == 0:
            lista.append("FizzBuzz")
        elif val % 3 == 0:
            lista.append("Fizz")
        elif val % 5 == 0:
            lista.append("Buzz")
        else:
            lista.append(str(val))

    return lista"""

"""def zadanie_fizz_bizz(n: int) -> None:
    for val in range(1, max(n + 1, 1)):
        if val % 3 == 0 and val % 5 == 0:
            print("FizzBuzz", end=' ')
        elif val % 3 == 0:
            print("Fizz", end=' ')
        elif val % 5 == 0:
            print("Buzz", end=' ')
        else:
            print(str(val), end=' ')"""

"""def adanie_fizz_bizz(n: int) -> None:
    napis = ""
    for val in range(1, max(n + 1, 1)):
        if val % 3 == 0:
            napis += "Fizz"
        if val % 5 == 0:
            napis += "Buzz"
        if val % 5 != 0 and val % 3 != 0:
            napis += str(val)
        napis += " "
    print(napis)"""

"""def zadanie_fizz_bizz(n: int) -> None:
    napis = ""
    for val in range(1, max(n + 1, 1)):
        napis += "Fizz" * (val % 3 == 0) + "Buzz" * (val % 5 == 0) + str(val) * (val % 3 != 0 and val % 5 != 0) + " "
    print(napis)"""

def zadanie_fizz_bizz(n: int) -> None:
    napis = ""
    for val in range(1, max(n + 1, 1)):
        napis += ("Fizz" * (val % 3 == 0) + "Buzz" * (val % 5 == 0) or str(val)) + " "
    print(napis)

n = 15
# print(f"Lista FizzBuzz dla wartości {n} wygląda następująco: {zadanie_fizz_bizz(n)}")
zadanie_fizz_bizz(n)
"""
5)	[PowerOfThree] Napisz funkcje, która będzie sprawdzać czy dana liczba n jest potęgą 3, tak że n == 3^x
Przykład: 
Dane wejściowe: n = 27
Dane wyjściowe: True
Ponieważ 27 = 3^3
Przykład: 
Dane wejściowe: n = 0
Dane wyjściowe: False
Ponieważ nie ma takiej liczby x gdzie 3^x byłoby równe 0
"""
print(f"\nZadanie {zadanie}\n")
zadanie += 1

def czy_potega_trojki(n: int) -> bool:
    # potegi = [x ** x for x in range(100)]
    # if n in potegi:
    #     return True
    # else:
    #     return False
    while n % 3 == 0 and n != 0:
        n = n / 3
        if n == 1:
            return True
    else:
        return False


n = 27
print(f"Czy liczba {n} jest potęgą 3?: {czy_potega_trojki(n)}")
n = 0
print(f"Czy liczba {n} jest potęgą 3?: {czy_potega_trojki(n)}")
n = 54
print(f"Czy liczba {n} jest potęgą 3?: {czy_potega_trojki(n)}")
n = 81
print(f"Czy liczba {n} jest potęgą 3?: {czy_potega_trojki(n)}")

"""
6)	[MergeTwoLists] Napisz funkcje która będzie łączyć dwie listy w sposób posortowany. 
Przykład: 
Dane wejściowe: lista1 = [1, 2, 3], lista2 = [2, 3, 4]
Dane wyjściowe: [1, 2, 2, 3, 3, 4]
Przykład: 
Dane wejściowe: lista1 = [], lista2 = []
Dane wyjściowe: []
"""
print(f"\nZadanie {zadanie}\n")
zadanie += 1

def zlacz_listy_sort(lista1: list, lista2: list) -> list:
    return list(sorted(lista1 + lista2))

lista1 = [1, 2, 3]
lista2 = [2, 3, 4]
print(f"Lista 1: {lista1}\nLista 2: {lista2}\nPosortowana lista: {zlacz_listy_sort(lista1,lista2)}")

lista1 = []
lista2 = []
print(f"Lista 1: {lista1}\nLista 2: {lista2}\nPosortowana lista: {zlacz_listy_sort(lista1,lista2)}")

"""
7)	[PlusOne] Do danej listy liczb dodaj 1. 
Przykład: 
Dane wejściowe: lista1 = [1, 2, 3]
Dane wyjściowe: [1, 2, 4]

Przykład: 
Dane wejściowe: lista1 = [9, 9]
Dane wyjściowe: [1, 0, 0]
"""
print(f"\nZadanie {zadanie}\n")
zadanie += 1

"""def inkrementuj_liste(lista: list) -> list:
    if len(lista) < 1:
        print("Lista nie może być pusta")
        return []
    tmp = -1
    if lista[tmp] == 9:
        while lista[tmp] == 9 and abs(tmp) != len(lista):
            lista[tmp] = 0
            tmp -= 1
        else:
            if abs(tmp) == len(lista):
                lista.append(0)
                lista[0] = 1
            else:
                lista[tmp] += 1
            return lista
    else:
        lista[tmp] += 1
        return lista"""

def inkrementuj_liste(lista: list) -> list:
    if len(lista) < 1:
        print("Lista nie może być pusta")
        return []
    for i in range(len(lista) - 1, -1, -1):
        if lista[i] == 9:
            lista[i] = 0
        else:
            lista[i] += 1
            return lista
    else:
        return [1] + lista


lista1 = [1, 2, 3]
print(f"Lista {lista1} po dodaniu wartości 1: {inkrementuj_liste(lista1)}")

lista1 = [9, 9]
print(f"Lista {lista1} po dodaniu wartości 1: {inkrementuj_liste(lista1)}")

lista1 = [9, 0, 9]
print(f"Lista {lista1} po dodaniu wartości 1: {inkrementuj_liste(lista1)}")

lista1 = [9, 9, 9]
print(f"Lista {lista1} po dodaniu wartości 1: {inkrementuj_liste(lista1)}")

lista1 = []
print(f"Lista {lista1} po dodaniu wartości 1: {inkrementuj_liste(lista1)}")

lista1 = [9]
print(f"Lista {lista1} po dodaniu wartości 1: {inkrementuj_liste(lista1)}")
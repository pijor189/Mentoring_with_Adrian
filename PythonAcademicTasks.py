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

liczby = [3, 5, 7, 12]
suma = 10
for key, value in enumerate(liczby):
    for i in range(key + 1, len(liczby)):
        if value + liczby[i] == suma:
            print(f"Liczby spod indeksów {key} oraz {i} dają wartość {suma}")
            break           # jeśli zakładamy, że ma się znajdować tylko jedno rozwiązanie

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
    # tak jak w opisie nie działamy w 1 i 6 dzień
    if cena != cena_zlota[0] and cena != cena_zlota[-1]:
        if cena <= srednia:
            # kupno
            zloto -= cena
        else:
            # sprzedaż
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
    tmp = str(tekst[0])
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

def zadanie_fizz_bizz(n: int) -> list:
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

    return lista

n = 15
print(f"Lista FizzBuzz dla wartości {n} wygląda następująco: {zadanie_fizz_bizz(n)}")

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

def inkrementuj_liste(lista: list) -> list:
    if len(lista) > 1:
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
            return lista
    else:
        print("Lista nie może być pusta")
        return []


lista1 = [1, 2, 3]
print(f"Lista {lista1} po dodaniu wartości 1: {inkrementuj_liste(lista1)}")

lista1 = [9, 9]
print(f"Lista {lista1} po dodaniu wartości 1: {inkrementuj_liste(lista1)}")
"""
Zadania z pliku PythonTasks - Tuple, Set
"""
zadanie = 1
# 1)	Utwórz tuple (1, 2, 3) na dwa sposoby (funkcja, nawiasy).
print(f"Zadanie {zadanie}")
zadanie += 1
tuple1 = (1, 2, 3)
print(type(tuple1))
print(tuple1)

tab = [1, 2, 3, 4]
tuple2 = tuple(tab)
print(type(tuple2))
print(tuple2)
print()

# 2)	Mając do dyspozycji dwie tuple (1, 2, 3) i (4, 5, 6) połącz je w jedną.
print(f"Zadanie {zadanie}")
zadanie += 1
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple3 = tuple1 + tuple2
print(type(tuple3))
print(tuple3)
print()

# 3)	Zamień listę [1, 2, 3, 4] na tuple.
print(f"Zadanie {zadanie}")
zadanie += 1
tuple1 = [1, 2, 3, 4]
print(type(tuple1))
tuple1 = tuple(tuple1)
print(type(tuple1))
print()

# 4)	Mają do dyspozycji tuple (1, 2, 3) przypisz wartości do zmiennych a, b, c w ramach jednego przypisania.
print(f"Zadanie {zadanie}")
zadanie += 1
tuple1 = (1, 2, 3)
a, b, c = tuple1
print("a = {}, b = {}, c = {}".format(a, b, c))
print()

# 5)	Mając listę [1, 2, 2, 3, 4, 4, 5] – utwórz tuple zawierającą unikalne wartości (set)
print(f"Zadanie {zadanie}")
zadanie += 1
lista1 = [1, 2, 2, 3, 4, 4, 5]
lista2 = set(lista1)
print(type(lista2))
print(lista2)
print()

# 6)	[Badanie] Sprawdź co wyświetli się, gdy zamienimy listę [0, True, 1] na set. Następnie, sprawdź [0, 1, True] i wyjaśnij różnicę.
print(f"Zadanie {zadanie}")
zadanie += 1
lista = [0, True, 1]
print(type(lista))
lista = set(lista)
print(type(lista))
print(lista)
lista = [0, 1, True]
print(type(lista))
lista = set(lista)
print(type(lista))
print(lista)
print()
# Wyświetla wartość, która się powtórzyła zachowując typ tej wartości, który był pierwszy, ponieważ True == 1

"""
7)	Mając set {1, 2, 3} dodaj jeden element i usuń (2 sposoby) jeden.
"""
print(f"Zadanie {zadanie}")
zadanie += 1
set1 = {1, 2, 3}
set1.add(6)
print(set1)
a = set1.remove(6)
print(set1)
b = set1.pop()
print(set1)
set1.add(1)
print(set1)
set1.clear()
print(set1)

print(a)
print(b)

"""
8)	Mając dwa zbiory A = {1, 2, 3, 4}, B = {3, 4, 5, 6} napisz funkcję, która wypisze:
a)	Sumę zbiorów
b)	Iloczyn zbiorów
c)	Różnicę zbiorów
d)	Różnicę symetryczną zbiorów

W Pythonie możemy wykonywać operacje na zbiorach (set'ach) - Działania na zbiorach,:
•	Suma zbiorów – operator |
•	Iloczyn zbiorów – operator &
•	Różnica zbiorów – operator -
•	Różnica symetryczna zbiorów – operator ^ (wszystkie elementy które nie są wspólne)
"""
print(f"Zadanie {zadanie}")
zadanie += 1
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
def operacje_na_set(a: set, b: set):
    print("Suma zbiorów {}, {}: {}".format(a, b, a | b))
    print("Iloczyn zbiorów {}, {}: {}".format(a, b, a & b))
    print("Różnica zbiorów {}, {}: {} {}".format(a, b, a - b, b - a))
    print("Różnica symetryczna zbiorów {}, {}: {}".format(a, b, a ^ b))

def operacje_na_set_metody(a: set, b: set):
    print("Suma zbiorów {}, {}: {}".format(a, b, a.union(b)))
    print("Iloczyn zbiorów {}, {}: {}".format(a, b, a.intersection(b)))
    print("Różnica zbiorów {}, {}: {} {}".format(a, b, a.difference(b), b.difference((a))))
    print("Różnica symetryczna zbiorów {}, {}: {}".format(a, b, a.symmetric_difference(b)))

operacje_na_set(A, B)
operacje_na_set_metody(A, B)
print()

# 9)	Napisz funkcję, która będzie sprawdzać czy zmienna „a” jest podzbiorem (<= lub issubset) zmiennej „b”. W celu testu przekaż do funkcji wartości a = {1,2} oraz b = {1,2,3,4}
print(f"Zadanie {zadanie}")
zadanie += 1
def sprawdz_czy_podzbior(a: set, b: set) -> bool:
    if a <= b:
        print("Zmienna {} jest podzbiorem zmiennej {}".format(a, b))
        return True
    else:
        print("Zmienna {} nie jest podzbiorem zmiennej {}".format(a, b))
        return False

def sprawdz_czy_podzbior_metoda(a: set, b: set) -> bool:
    if a.issubset(b):
        print("Zmienna {} jest podzbiorem zmiennej {}".format(a, b))
        return True
    else:
        print("Zmienna {} nie jest podzbiorem zmiennej {}".format(a, b))
        return False

a = {1, 2}
b = {1, 2, 3, 4}
sprawdz_czy_podzbior(a, b)
sprawdz_czy_podzbior_metoda(a, b)
print()

# 10)	Napisz funkcję, która usunie wszystkie elementy z setu
print(f"Zadanie {zadanie}")
zadanie += 1
def usun_wszystkie_elem_set(set1: set):
    set1.clear()
print(b)
usun_wszystkie_elem_set(b)
print(type(b))
print(b)
print()

# 11)	Sprawdź w jaki sposób zamieniane są stringi na set
print(f"Zadanie {zadanie}")
zadanie += 1
napis = 'abc'
print(type(napis))
print(napis)
napis = set(napis)
print(type(napis))
print(napis)

# 12)	Napisz funkcję, która przyjmie dwa argumenty „banana” i „bandana”. Funkcja ma zwrócić litery wspólne dla obu słów.
print(f"Zadanie {zadanie}")
zadanie += 1
def litery_wspolne(napis1: str, napis2: str):
    a = set(napis1)
    b = set(napis2)
    print("Litery wspólne dla napisów: {} oraz {} to: {}".format(napis1, napis2, a.intersection(b)))

    return a.intersection(b)

litery = litery_wspolne("banana", "bandana")
print(sorted(litery))
print()

"""
13)	Mając dwa zespoły niebiescy = {"Ala", "Ola", "Tomek"} i zieloni = {"Jan", "Piotr", "Ola"}, napisz funkcję, która:
a)	Wypisze osoby, które są częścią zespołu niebieskich, ale nie zielonych
b)	Wypisze osoby, które są częścią zespołu zielonych, ale nie niebieskich  
"""
print(f"Zadanie {zadanie}")
zadanie += 1
niebiescy = {"Ala", "Ola", "Tomek"}
zieloni = {"Jan", "Piotr", "Ola"}
def wypisz_wspolne(a: set, b: set):
    return a.difference(b)

print("Osoby będące częścią zespołu niebieskich, ale nie zielonych to: {}".format(wypisz_wspolne(niebiescy, zieloni)))
print("Osoby będące częścią zespołu zielonych, ale nie niebieskich to: {}".format(wypisz_wspolne(zieloni, niebiescy)))
print()

# 14)	Mając niemutowalną tuple, a = ([1, 2], [3, 4]), czy można zmienić jej wartości? Spróbuj zamienić 1 na 99 i wyjaśnij zjawisko.
print(f"Zadanie {zadanie}")
zadanie += 1
a = ([1, 2], [3, 4])
print(a)
print(type(a))
a[0][0] = 99
print(a)
print(type(a))
print(type(a[0]))
# Możemy zmienić wartość 1 na 99, ponieważ 1 jest elementem listy, która znowu jest elementem tuple, a lista jest mutowalna
print()

# 15)	Spróbuj zamienić powyższą kolekcję tak, aby byłą kompletnie niemutowalna.
print(f"Zadanie {zadanie}")
zadanie += 1
a = ([1, 2], [3, 4])
print(a)
print(type(a))
print(type(a[0]))
a = (tuple([1, 2]), tuple([3, 4]))
print(a)
print(type(a))
print(type(a[0]))
print()

"""
16)	Mając do dyspozycji maile emails = ["a@x.com", "b@x.com", "a@x.com", "c@x.com", "b@x.com"]. Napisz funkcję, która:
a)	Usunie duplikaty z zachowaniem kolejności (jak w listach)
b)	Usunie duplikaty bez zachowania kolejności (jak w set’cie)
"""
print(f"Zadanie {zadanie}")
zadanie += 1
emails = ["a@x.com", "b@x.com", "a@x.com", "c@x.com", "b@x.com"]
def usun_duplikat(a: list) -> list:
    a = set(a)
    return list(a)

print("Lista maili {} bez duplikatów (zachowana kolejność): {}".format(emails, sorted(usun_duplikat(emails))))
print("Lista maili {} bez duplikatów (brak zachowanej kolejności): {}".format(emails, usun_duplikat(emails)))
print()

"""
	Mając do dyspozycji słownik miasta = {
    ("Warszawa", 52.23, 21.01): 1793579,
    ("Kraków", 50.06, 19.94): 779115,
    ("Gdańsk", 54.35, 18.64): 486022
}
napisz funkcję, która przyjmie współrzędne (lat, lon) i zwróci nazwę najbliższego miasta (sprawdź, jak obliczyć odległość dwóch punktów w przestrzeni 2D). 
Możesz przykładowo użyć odległości euklidycznej:
odległość=√(〖(x2-x1)〗^2+ 〖(y2-y1)〗^2 )
"""
print(f"Zadanie {zadanie}")
zadanie += 1
miasta = {
    ("Warszawa", 52.23, 21.01): 1793579,
    ("Kraków", 50.06, 19.94): 779115,
    ("Gdańsk", 54.35, 18.64): 486022
}

def najblizsze_miasto(a: dict, lat: float, lon: float):
    odleglosc = []
    dane = list(a.keys())
    for key, value in enumerate(dane):
        x2 = value[1]
        y2 = value[2]
        odleglosc.append(0.5 ** ((x2 - lat) ** 2 + (y2 - lon) ** 2))
        if key != 0:
            if najblizej < odleglosc[key]:
                najblizej = odleglosc[key]
                position = key
        else:
            najblizej = odleglosc[key]
            position = key
    print("Najbliższe miasto jakiego się znajdujesz to: {} i jesteś w odległości: {}".format(dane[position][0], najblizej))

najblizsze_miasto(miasta, 50.81, 19.12)
print()

"""
18)	Mając listę punktów 2D – punkty = [(1, 2), (3, 4), (1, 2), (5, 6), (3, 4)]
a)	Znajdź wszystkie unikalne punkty
b)	Posortuj je według drugiej współrzędnej
"""
print(f"Zadanie {zadanie}")
zadanie += 1
punkty = [(1, 2), (3, 4), (1, 2), (5, 6), (3, 4)]
unikalne_punkty = set(punkty)
print(list(unikalne_punkty))
print(sorted(unikalne_punkty,reverse=True))
# przyznaje się, nie wiedziałem jaki mam podać argument do key, więc spytałem tutaj wujka Google i wyszło fajne zastosowanie tej lambdy o której gadaliśmy
print(sorted(unikalne_punkty, key=lambda x: x[1]))
print()

# 19)	Spróbuj utworzyć set, test = {(1, 2), (3, 4), [5, 6]} – opisz co się pojawiło, oraz znajdź informację, dlaczego.
print(f"Zadanie {zadanie}")
zadanie += 1
# test = {(1, 2), (3, 4), [5, 6]}
# print(type(test))
# print(type(test[0]))
# print(test)
print()
# Wywala TypeError: unhashable type: 'list' - rozumiem to tak, że set nie może przyjąć typu, który jest mutable,
# ponieważ ma posiadać jedynie elementy immutable, mimo, że set samo w sobie jest mutable

"""
20)	Mając listę słów, słowa = ["python", "ai", "data", "python", "ml", "data"], napisz funkcję, która utworzy słownik, 
gdzie kluczem będzie słowo, a wartością indeksy, w których występuje. Przykładowo {„data”: {2, 5}}
"""
print(f"Zadanie {zadanie}")
zadanie += 1
slowa = ["python", "ai", "data", "python", "data", "ml", "data", "data"]
def utworz_slownik(tab: lista) -> dict:
    slownik = {}
    for key, value in enumerate(tab):
        if value in slownik.keys():
            if type(slownik[value]) is set:
                tmp = list(slownik[value])
                tmp.append(key)
                slownik[value] = set(tmp)
            else:
                slownik[value] = {slownik[value],key}
        else:
            slownik[value] = key

    return slownik

print("Słownik powstały na podstawie słów: {} wygląda następująco: {}".format(slowa, utworz_slownik(slowa)))
print()

# 21)	Sprawdź na koniec czym jest frozenset. Czym różni się od zwykłego set. Który z tych dwóch opcji mógłby być kluczem w słowniku, oraz dlaczego?
# frozenset od set różni się tym, że jest immutable i nie możemy go modyfikować po utworzeniu
print(f"Zadanie {zadanie}")
zadanie += 1
tmp = {1, 2, 3, 4}
tmp2 = frozenset(tmp)
print(type(tmp))
print(type(tmp2))
print(tmp)
print(tmp2)
tmp.add(5)
# powoduje błąd
# tmp2.add(5)
print(tmp)
print(tmp2)
print()

"""
22)	Stwórz zbiór liczb od 1 do 1000 z krokiem 1 używając list comprehension oraz tuple comprehension.
a)	Sprawdź typ obu zmiennych (type())
b)	Spróbuj wyświetlić obie utworzone kolekcje   
c)	Sprawdź rozmiar (sys.getsizeof())
d)	Możesz poczytać o tym czym jest generator i czym różni się od listy. Jak będziesz miał czas i chęci możesz spróbować zaimplementować 
    własne funkcję z return’em oraz yield’em – niemniej jednak, omówimy sobie to na kolejnym spotkaniu :)
"""
print(f"Zadanie {zadanie}")
zadanie += 1
import sys

zbior_lista = [x for x in range(1, 1001)]
zbior_tuple = (x for x in range(1, 1001))
# a)
print(type(zbior_lista))
print(type(zbior_tuple))
# b)
print(zbior_lista)
print(zbior_tuple)
# c)
print(sys.getsizeof(zbior_lista))
print(sys.getsizeof(zbior_tuple))
# d)
def wypisz_wartosci_generator(a):
    print(next(a))

def wypisz_wartosci_yield(n):
    for i in range(1, n):
        yield i

wypisz_wartosci_generator(zbior_tuple)
wypisz_wartosci_generator(zbior_tuple)
wypisz_wartosci_generator(zbior_tuple)
wypisz_wartosci_generator(zbior_tuple)

wartosci = wypisz_wartosci_yield(1001)
print(type(wartosci))
print(sys.getsizeof(wartosci))
print(next(wartosci))
print(next(wartosci))
print(next(wartosci))
print(next(wartosci))
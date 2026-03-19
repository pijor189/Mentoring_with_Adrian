"""
Zadania z pliku PythonTasks - Zadania akademickie 2
"""

zadanie = 1
# 1.	Napisz funkcję, która odwróci podany string bez użycia [::-1]
print(f"\nZadanie {zadanie}\n")
zadanie += 1

def obroc_string(napis: str) -> str:
    return str([napis[x] for x in range(len(napis) - 1, -1, -1)])
print(f"Napis: {"string"} odwrócony: {obroc_string("string")}")

# 2.	Napisz funkcję, która przyjmuje dwa stringi. Funkcja ma zwracać True, jeśli słowa są Anagramem.
print(f"\nZadanie {zadanie}\n")
zadanie += 1

def anagram(text1: str, text2: str) -> bool:
    if sorted(text1.lower()) == sorted(text2.lower()):
        return True
    return False
text1 = "karta"
text2 = "krata"
print(f"Czy dwa stringi: {text1} oraz {text2} są anagramami?\n{anagram(text1, text2)}")
text1 = "karta"
text2 = "kraty"
print(f"Czy dwa stringi: {text1} oraz {text2} są anagramami?\n{anagram(text1, text2)}")

# 3.	Naszym zadaniem jest zamiana ciągu `a4b3r6` na `aaaabbbrrrrrr`.
print(f"\nZadanie {zadanie}\n")
zadanie += 1

ciag = 'a4b3r6'
tmp = ''
for i in range(0, len(ciag), 2):
    tmp += ciag[i] * int(ciag[i + 1])
print(tmp)

# 4.	Napisz dekorator, który wypisze „przed” przed wywołaniem funkcji i „po” po wywołaniu funkcji (musisz umieć dekoratory na swoją rozmowę)
print(f"\nZadanie {zadanie}\n")
zadanie += 1


def dekorator(func):
    def deko():
        print("przed")
        func()
        print("po")
    return deko

@dekorator
def show():
    print("To jest główna część")

show()

# 5.	Napisz funkcję, która zliczy litery w stringu.
print(f"\nZadanie {zadanie}\n")
zadanie += 1

def zlicz_litery(napis: str) -> int:
    licznik = 0
    for litera in napis:
        if litera.isalpha():
            licznik += 1

    return licznik

napis = 'abcdefgh567--!  '
print(f"W stringu {napis} jest {zlicz_litery(napis)} liter")

"""
6.	Napisz funkcję, która (użyj context managera):
1.	Otwiera plik tekstowy,
2.	Odczytuje jego zawartość jako liczbę,
3.	Dodaje do niej 100,
4.	Zapisuje wynik z powrotem do pliku.
"""
print(f"\nZadanie {zadanie}\n")
zadanie += 1

import os

def dopisz_do_pliku(plik, a):
    if not os.path.isfile(plik):
        return print(f"Błąd przy odczycie, sprawdz czy podałeś dobrze plik")
    with open(plik, "r") as f:
        tmp = f.read()
        print(f"Zawartość pliku przed zapisem {tmp}")
        number = int(tmp) + 100

    with open(plik, "w") as f:
        f.write(str(number))

    with open(plik, "r") as f:
        print(f"Zawartość pliku po nadpisaniu {f.read()}")

dopisz_do_pliku("plik_zad_6", 100)

"""7.	Stwórz własny generator, który będzie wypisywał liczby ciągu fibonaciego dla zadanego N oznaczającego, ile ma ich wygenerować.
wejście: 5
wyjście: 1, 1, 2, 3, 5
"""
print(f"\nZadanie {zadanie}\n")
zadanie += 1

def generuj_ciag_Fib(n: int) -> list:
    tab = []
    for i in range(n):
        if i < 2:
            tab.append(1)
        else:
            tab.append(tab[i - 2] + tab[i - 1])
    return tab

n = 10
print(f"Ciąg Fibonaciego dla podanego N = {n} -> {generuj_ciag_Fib(n)}")

"""
8.	Napisz funkcję, która dostając listę, znajdzie i zwróci najczęściej występujący element. 
wejście: [1, 2, 2, 3, 3, 3]
wyjście: 3
"""
print(f"\nZadanie {zadanie}\n")
zadanie += 1

def znajdz_elem(lista: list):
    tmp = set(lista)
    tmp1 = dict()
    for val in tmp:
        tmp1[val] = lista.count(val)

    for key, val in enumerate(tmp1):
        if tmp1[val] is max(tmp1.values()):
            return val

lista = [1, 2, 2, 3, 3, 3, 'a', 'a', 'a', 'a']
print(f"Najczęściej występujący element z listy {lista} to: {znajdz_elem(lista)}")

"""
9.	Napisz funkcję która będzie sprawdzać, czy kolejność nawiasów się zgadza:
„{}()[]” -> True 
„({[]})” -> True 
„(({((}})” -> False
"""
print(f"\nZadanie {zadanie}\n")
zadanie += 1

def czy_nawiasy_sa_ok(napis: str) -> bool:
    pary = {'}' : '{', ']': '[', ')': '('}
    tab = []
    for znak in napis.strip():
        if znak in pary.values():
            tab.append(znak)
        elif znak in pary:
            if tab[-1] == pary[znak]:
                tab.pop()
            else:
                return False
    return True

nawiasy = "{}()[]"
print(f"Czy kolejność nawiasów w tym przypadku {nawiasy} jest prawidłowa?: {czy_nawiasy_sa_ok(nawiasy)}")
nawiasy = "({[]})"
print(f"Czy kolejność nawiasów w tym przypadku {nawiasy} jest prawidłowa?: {czy_nawiasy_sa_ok(nawiasy)}")
nawiasy = "(({((}})"
print(f"Czy kolejność nawiasów w tym przypadku {nawiasy} jest prawidłowa?: {czy_nawiasy_sa_ok(nawiasy)}")

"""
10.	Napisz funkcję która doda do siebie dwie liczby zapisane jako stringi bez użycia int().
„120” + „80” -> „200”. 
"""
print(f"\nZadanie {zadanie}\n")
zadanie += 1

# przyznaje, nie miałem tutaj pomysłu jak to zrobić, myślałem o zastosowaniu ASCII, ale nie pomyślałem, by to zrobić jak z dodawaniem pod kreskę i wspomogłem się trochę
def dodaj_stringi(napis1: str, napis2: str) -> str:
    # obliczamy rozmiary stringów oraz rozmiar pętli
    len1 = len(napis1) - 1
    len2 = len(napis2) - 1
    size_of_loop = len(napis1) if len(napis1) > len(napis2) else len(napis2)
    reszta_dodawania = 0
    tab = []
    for i in range(size_of_loop, 0, -1):
        # zczytujemy pojedyńczo cyfry od końca i dodajemy do siebie jak w dodawaniu pod kreską
        # żeby je poprawnie zczytać, zamieniamy je na kod ASCII i odejmujemy wartość 0 w ASCII, by odzwierciedlić liczbę
        tmp1 = ord(napis1[len1]) - ord('0') if len1 >= 0 else 0
        tmp2 = ord(napis2[len2]) - ord('0') if len2 >= 0 else 0
        suma_dodawania = tmp1 + tmp2 + reszta_dodawania
        # jeśli suma większa niż 9, przenosimy resztę do kolejnej iteracji
        if suma_dodawania < 10:
            reszta_dodawania = 0
        else:
            reszta_dodawania = 1
            suma_dodawania = suma_dodawania - 10
        tab.append(str(suma_dodawania))
        len1 -= 1
        len2 -= 1

    return "".join(tab[::-1])

napis1 = "140"
napis2 = "80"
print(f"{napis1} + {napis2} = {dodaj_stringi(napis1, napis2)}")

"""
11.	Napisz funkcje sortującą krotki po drugim elemencie.
[(1,3),(2,1),(3,2)] -> [(2,1),(3,2),(1,3)]
"""
print(f"\nZadanie {zadanie}\n")
zadanie += 1

def sortuj_krotki_po_2_elemencie(a) -> tuple:
    return sorted(a, key=lambda x: x[1])

a = [(1,3),(2,1),(3,2)]
print(f"Krotki przed sortowaniem: {a}\nKrotki po sortowaniu po 2 elemencie: {sortuj_krotki_po_2_elemencie(a)}")
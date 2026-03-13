"""
Zadania z pliku PythonFullDict.py
"""
zadanie = 1
# 1)	Utwórz pusty słownik na 2 sposoby
print(f"\nZadanie {zadanie}\n")
zadanie += 1

slownik1 = {}
print(slownik1)
print(type(slownik1))
slownik2 = dict()
print(slownik2)
print(type(slownik2))
# 2)	Utwórz słownik z trzema parami klucz-wartość
print(f"\nZadanie {zadanie}\n")
zadanie += 1

slownik1 = {'a': 1, 'b': 2, 'c': 3}
print(slownik1)
# 3)	Dodaj nową parę klucz-wartość do istniejącego słownika
print(f"\nZadanie {zadanie}\n")
zadanie += 1

slownik1['d'] = 4
print(slownik1)
# 4)	Zmień wartość istniejącego klucza
print(f"\nZadanie {zadanie}\n")
zadanie += 1

slownik1['d'] = 5
print(slownik1)
# 5)	Usuń dodaną parę klucz-wartość ze słownika
print(f"\nZadanie {zadanie}\n")
zadanie += 1

slownik1.pop('d')
print(slownik1)
# 6)	Sprawdź czy dany klucz istnieje w słowniku
print(f"\nZadanie {zadanie}\n")
zadanie += 1

klucz = 'a'
if klucz in slownik1.keys():
    print(f"Klucz {klucz} istnieje w słowniku")
else:
    print(f"Nie ma takiego klucza jak {klucz} w słowniku")
# 7)	Wyświetl wartość wybranego klucza w słowniku
print(f"\nZadanie {zadanie}\n")
zadanie += 1

print(f"Wartość klucza {klucz} to {slownik1[klucz]}")
# 8)	Użyj metody .get() do pobrania wartości dla nieistniejącego klucza z wartością domyślną
print(f"\nZadanie {zadanie}\n")
zadanie += 1

klucz = 'd'
slownik1[klucz] = slownik1.get(klucz)
print(slownik1[klucz])
# 9)	Wyświetl wszystkie klucze w słowniku
print(f"\nZadanie {zadanie}\n")
zadanie += 1

for key in slownik1.keys():
    print(key, end= ' ')
print()
# 10)	Wyświetl wszystkie wartości w słowniku
print(f"\nZadanie {zadanie}\n")
zadanie += 1

for value in slownik1:
    print(slownik1[value])
# 11)	Wyświetl wszystkie part klucz-wartośc w słowniku
print(f"\nZadanie {zadanie}\n")
zadanie += 1

for value in slownik1:
    print(f"{value}: {slownik1[value]}")
# 12)	Wyświetl liczbę elementów w słowniku
print(f"\nZadanie {zadanie}\n")
zadanie += 1

print(len(slownik1))
# 13)	Wyczyść cały słownik
print(f"\nZadanie {zadanie}\n")
zadanie += 1

slownik1.clear()
print(slownik1)
print(len(slownik1))
# 14)	Napisz czym różni się pop() od get() – zarówno dla słownika jak i list
print(f"\nZadanie {zadanie}\n")
zadanie += 1

lista = [1, 2, 3]
slownik1 = {'a': 1, 'b': 2, 'c': 3}
b = lista.pop()
print(b, lista)
# nie ma get() dla listy, pop() zwraca i ściąga ją z listy

a = slownik1.get('a')
b = slownik1.pop('a')
print(a, b, slownik1)
# pop() zwraca wartość jednocześnie ściągając ją ze słownika, get() ją tylko zwraca

# 15)	Skopiuj słownik do nowej zmiennej
print(f"\nZadanie {zadanie}\n")
zadanie += 1

slownik2 = slownik1.copy()
print(slownik2)
# 16)	Połącz dwa słowniki w jeden np. a = {1: 9}, b = {2, 8}
print(f"\nZadanie {zadanie}\n")
zadanie += 1

a = {1: 9}
b = {2: 8}
a.update(b)
print(a)
# 17)	Utwórz słownik z listy tupli np. [(„a”, 1), („b”, 2)]
print(f"\nZadanie {zadanie}\n")
zadanie += 1

a = [("a", 1), ("b", 2)]
c = {}
for indeks in a:
    key, value = indeks
    c[key] = value
print(c)
# 18)	Napisz funkcję przypisującą wartość do klucza tylko jeśli nie ma on wartości
print(f"\nZadanie {zadanie}\n")
zadanie += 1
slownik2 = {'a': 1, 'b': 2, 'c': None}

def dopisz_wartosc_do_klucza(slownik: dict):
    for key, val in enumerate(slownik):
        if slownik[val] is None:
            slownik[val] = key + 1

print(slownik2)
dopisz_wartosc_do_klucza(slownik2)
print(slownik2)

# 19)	Opisz jak różni się metoda setdefault() dla istniejącego oraz nowego klucza
print(f"\nZadanie {zadanie}\n")
zadanie += 1

slownik1.setdefault('c', 100)
print(slownik1)
slownik1.setdefault('d', 100)
print(slownik1)
# setdefault() w przypadku kiedy klucz istnieje zwraca jego wartość ignorując wartość która mu podaliśmy, w przypadku kiedy klucz nie ma wartosci to przypisuje mu ta ktora podalismy

# 20)	Opisz czym różni się popitem() od pop()
print(f"\nZadanie {zadanie}\n")
zadanie += 1

print(slownik1)
a = slownik1.pop('d')
print(slownik1)
print(a)
a = slownik1.popitem()
print(slownik1)
print(a)

# pop() ściąga ze słownika podany klucz z wartością, jednocześnie zwracając wartość klucza, popitem() ściąga ostatni klucz ze słownika i zwraca klucz z wartością w formie tuple

"""
21)	Utwórz zagnieżdżony słownik dla 3 zwierząt, gdzie kluczem będzie jego imię. A wartością słownik z informacjami w stylu: 
•	wiek: 2000 
•	gatunek: „kot”
•	odgłos: „miau”
•	ilość nóg: 4
"""
print(f"\nZadanie {zadanie}\n")
zadanie += 1

zwierzeta = {'Luna': {'wiek': 2024, 'gatunek': 'pies', 'odgłos': 'hau', 'ilość nóg': 4},
             'Elvis': {'wiek': 2016, 'gatunek': 'pies', 'odgłos': 'hau', 'ilość nóg': 4},
             'Duncan': {'wiek': 2018, 'gatunek': 'kot', 'odgłos': 'miau', 'ilość nóg': 4}
             }
print(zwierzeta)

# 22)	Wyświetl imię oraz ilość nóg drugiego z zwierząt z powyższego zadania
print(f"\nZadanie {zadanie}\n")
zadanie += 1
imiona_zwierzat = list(zwierzeta.keys())
print(f"Imię: {imiona_zwierzat[1]}, ilość nóg: {zwierzeta[imiona_zwierzat[1]]['ilość nóg']}")
# 23)	Do utworzonego w zadaniu 3 słowniku, dodaj 4 zwierzę.
print(f"\nZadanie {zadanie}\n")
zadanie += 1

zwierzeta['Czarna'] = {'wiek': 2026, 'gatunek': 'pies', 'odgłos': 'hau', 'ilość nóg': 4}
print(zwierzeta['Czarna'])
# 24)	Napisz pętle wyświetlającą dane wszystkich zwierząt.
print(f"\nZadanie {zadanie}\n")
zadanie += 1

for zwierze in zwierzeta:
    print(zwierze, zwierzeta[zwierze])
# 25)	Mając słownik {‘e’: 5, ‘c’: 3, ‘a’:1, ‘b’:2}, posortuj go po wartościach
print(f"\nZadanie {zadanie}\n")
zadanie += 1

slownik = {'e': 5, 'c': 3, 'a': 1, 'b': 2}
print(slownik)
slownik = dict(sorted(slownik.items()))
print(slownik)
for value in slownik:
    print(value, ': ', slownik[value], sep='')
# 26)	Utwórz słownik dla N elementów, gdzie N będzie kluczem a N^2 wartością
print(f"\nZadanie {zadanie}\n")
zadanie += 1

# n = input(int("Podaj wartość n: "))
n = 3
slownik = dict()
for i in range(1, n + 1):
    slownik[i] = i * 2
print(slownik)

# 27)	Napisz funkcje, która zsumuje wszystkie wartości w słowniku (zakłądamy, że przekazany słownik zawsze będzie miał numeryczne wartości)
print(f"\nZadanie {zadanie}\n")
zadanie += 1

def suma_wartosci_slownika(slownik: dict) -> int:
    return sum(slownik.values())

print(f"Suma wartości słownika {slownik} wynosi: {suma_wartosci_slownika(slownik)}")

"""
28)	Połącz dwa słowniki poprzez zsumowanie wartości dla tych samych kluczy. 
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
wyjście = {'a': 400, 'b': 400, 'd': 400, 'c': 300}
"""
print(f"\nZadanie {zadanie}\n")
zadanie += 1

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
wszystkie_klucze = set(d1) | set(d2)
wyjscie = dict()
for i in wszystkie_klucze:
    wyjscie[i] = d1.get(i, 0) + d2.get(i, 0)
wyjscie = dict(sorted(wyjscie.items()))
print(wyjscie)

"""
29)	Napisz funkcję, która na wejściu będzie przyjmować tekst(może być kilku członowe). Na wyjście ma zwrócić słownik który będzie zawierał zliczone znaki alfabetyczne. 
Np. dla tekstu „FALA” zwrócony zostanie słowniki {‘F’: 1, ’A’: 2, ’L’: 1}
"""
print(f"\nZadanie {zadanie}\n")
zadanie += 1

def zwroc_slownik(tekst: str) -> dict:
    slownik = dict()
    for znak in tekst:
        slownik[znak] = slownik.get(znak, 0) + 1

    return slownik
tekst = "FALA"
print(f"Tekst {tekst} przerobiony na słownik: {zwroc_slownik(tekst)}")

# 30)	Napisz funkcję, która zliczy występujące słowa w zdaniu. split()
print(f"\nZadanie {zadanie}\n")
zadanie += 1

def zlicz_slowa(tekst: str) -> int:
    # ilosc = 0
    # for slowo in tekst.split():
    #     ilosc += 1
    # return ilosc
    return len(tekst.split())
tekst = "Robię sobie zadania z Python"
print(f"Ilość słów w zdaniu '{tekst}' wynosi: {zlicz_slowa(tekst)}")

"""
31)	Mając słownik {'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12} 
    napisz funkcję, która sprawdzi czy wszystkie wartości słownika są równe 12. Jeśli tak zwróć True, inaczej False
"""
print(f"\nZadanie {zadanie}\n")
zadanie += 1

slownik = {'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
def czy_wartosci_rowne(slownik: dict) -> bool:
    if len(set(slownik.values())) > 1:
        return False
    else:
        return True

print(f"Czy wartości w słowniku {slownik} są wszystkie równe?: {czy_wartosci_rowne(slownik)}")

"""
Mając do dyspozycji słownik 
students = { "Anna Kowalska": 5, "Celina Wiśniewska": 3, "Damian Wójcik": 2.5, "Iga Dąbrowska": 2, "Elżbieta Kamińska": 5, "Filip Zieliński": 4, "Gabriela Szymańska": 3, "Hubert Lewandowski": 5, "Jakub Kozłowski": 4, "Karolina Jankowska": 5, "Łukasz Mazur": 3.5,"Magdalena Krawczyk": 2, "Bartosz Nowak": 4.5, "Norbert Król": 4, "Oliwia Pawlak": 5}
32)	Podnieś wszystkim studentom ocenę o 1 z uwzględnieniem, że 5 jest oceną maksymalną
"""
print(f"\nZadanie {zadanie}\n")
zadanie += 1

students = { "Anna Kowalska": 5, "Celina Wiśniewska": 3, "Damian Wójcik": 2.5, "Iga Dąbrowska": 2, "Elżbieta Kamińska": 5,
             "Filip Zieliński": 4, "Gabriela Szymańska": 3, "Hubert Lewandowski": 5, "Jakub Kozłowski": 4, "Karolina Jankowska": 5,
             "Łukasz Mazur": 3.5,"Magdalena Krawczyk": 2, "Bartosz Nowak": 4.5, "Norbert Król": 4, "Oliwia Pawlak": 5}

for val in students:
    if students.get(val) <= 4:
        print(f"Student/ka {val} uzyskuje podwyższenie oceny z {students.get(val)} na {students.get(val) + 1}")
        students[val] = students.get(val) + 1
    elif students.get(val) == 4.5:
        print(f"Student/ka {val} uzyskuje podwyższenie oceny z {students.get(val)} na {students.get(val) + 0.5}")
        students[val] = students.get(val) + 0.5
    else:
        print(f"Student/ka {val} ma już maksymalną możliwą ocenę {students.get(val)}")
print(students)

# 33)	Wypisz uczniów z najniższą oceną
print(f"\nZadanie {zadanie}\n")
zadanie += 1

for val in students:
    if students.get(val) is min(students.values()):
        print(f"{val} ma najniższą ocenę {students.get(val)} ze studentów")
        
# 34)	Wyświetl wszystkich uczniów z oceną 5
print(f"\nZadanie {zadanie}\n")
zadanie += 1

for val in students:
    if students.get(val) == 5:
        print(f"{val} ma ocenę {int(students.get(val))}")
# 35)	Policz i wyświetl średnią ocen wszystkich uczniów
print(f"\nZadanie {zadanie}\n")
zadanie += 1

srednia = sum(students.values()) / len(students)
print(f"Średnia ocen wszystkich studentów wynosi: {srednia:.2f}")
# 36)	Usuń wszystkich uczniów z oceną mniejszą lub równą 3
print(f"\nZadanie {zadanie}\n")
zadanie += 1
tmp = students.copy()
for val in tmp:
    if students.get(val) <= 3:
        students.pop(val)
print(students)

# 37)	Posortuj słownik wg. Imienia
print(f"\nZadanie {zadanie}\n")
zadanie += 1

students = dict(sorted(students.items()))
print(students)
# 38)	*Posortuj słownik wg Nazwiska, zachowując słownik w tym samym stanie
print(f"\nZadanie {zadanie}\n")
zadanie += 1

tmp = students.copy()
students.clear()
dane = list(tmp.keys())
nazwiska = []
for x in dane:
    tmp2 = x.split()
    nazwiska.append(tmp2[1])
nazwiska = sorted(nazwiska)
for nazwisko in nazwiska:
    for val in tmp:
        if nazwisko in val:
            students[val] = tmp.get(val)

print(students)
# 39)	Na podstawie istniejącego słownika stwórz nowy, który będzie zawierał tylko Nazwiska jako klucze studentów
print(f"\nZadanie {zadanie}\n")
zadanie += 1

students_nazwiska = dict()
for nazwisko in nazwiska:
    for val in tmp:
        if nazwisko in val:
            students_nazwiska[nazwisko] = students.get(val)

print(students_nazwiska)
# 40)	 Wyświetl 3 studentów z najniższą oceną
print(f"\nZadanie {zadanie}\n")
zadanie += 1

tmp = dict(sorted(students.items(), key= lambda x: x[1]))
for key, value in enumerate(tmp):
    if key <= 2:
        print(f"Student: {value} ocena: {tmp[value]}")
    else:
        break

# 41)	Poszerz słownik o {„Adam Ondra”: None}. Napisz metodę usuwającą studentów bez oceny
print(f"\nZadanie {zadanie}\n")
zadanie += 1

students["Adam Ondra"] = None
print(students)
def usun_studenta_bez_oceny(students: dict):
    tmp = students.copy()
    for val in tmp:
        if tmp.get(val) is None:
            students.pop(val)

usun_studenta_bez_oceny(students)
print(students)
# 42)	Poszerz słownik o {None: 3}. Napisz metodę usuwającą studentów bez imienia i nazwiska
print(f"\nZadanie {zadanie}\n")
zadanie += 1

students[None] = 3
print(students)
def usun_studenta_None(students: dict):
    tmp = students.copy()
    for val in tmp:
        if val is None:
            students.pop(val)

usun_studenta_None(students)
print(students)
# 43)	Zamień miejscem klucze oraz wartości.
print(f"Zadanie {zadanie}")
zadanie += 1

tmp = students.copy()
students.clear()
for val in tmp:
    if tmp.get(val) in students.keys():
        tmp_1 = []
        if len(students[tmp.get(val)][1]) == 1:
            tmp_1.append(students[tmp.get(val)])
        else:
            tmp_1.extend(students[tmp.get(val)])
        tmp_1.append(val)
        students[tmp.get(val)] = tmp_1
    else:
        students[tmp.get(val)] = val

print(students)
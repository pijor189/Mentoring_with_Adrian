"""
Zadania z pliku Python Numpy Tasks 2
"""
zadanie = 1

# 1.	Zaimportuj bibliotekę NumPy i nadaj jej alias np.
print(f"\nZadanie {zadanie}\n")
zadanie += 1

import numpy as np

# 2.	Utwórz w jednej linii listę Pythona zawierającą liczby od 1 do 10 i przekonwertuj ją na tablicę NumPy.
print(f"\nZadanie {zadanie}\n")
zadanie += 1

collection = np.array([x for x in range(1,11)])
collection2 = np.array(range(1,11))
collection3 = np.arange(1,11)
print(collection)
print(collection2)
print(collection3)

# 3.	Sprawdź typ danych (dtype) i kształt (shape) utworzonej tablicy.
print(f"\nZadanie {zadanie}\n")
zadanie += 1

print(collection.dtype)
print(collection.shape)
print(collection2.dtype)
print(collection2.shape)
print(collection3.dtype)
print(collection3.shape)

# 4.	Utwórz tablicę 2D o wymiarach 3x3 z liczbami od 1 do 9.
print(f"\nZadanie {zadanie}\n")
zadanie += 1

collection4 = np.arange(1, 10).reshape(3, 3)
print(collection4)

# 5.	Utwórz tablicę jednowymiarową 10x1 zer oraz tablicę dwuwymiarową 3x4 wypełnioną zerami (np.zeros).
print(f"\nZadanie {zadanie}\n")
zadanie += 1

collection5 = np.zeros(10, dtype=int)
print(collection5)
collection6 = np.zeros(3 * 4, dtype=int).reshape(3,4)
print(collection6)

# 6.	Utwórz tablicę 10x1 jedynek oraz tablicę dwuwymiarową 5x4 wypełnioną jedynkami (np.ones).
print(f"\nZadanie {zadanie}\n")
zadanie += 1

collection7 = np.ones(10, dtype=int)
print(collection7)
collection8 = np.ones(5 * 4, dtype=int).reshape(5,4)
print(collection8)

# 7.	Utwórz tablicę z wartościami od 0 do 20 z krokiem co 2 (np.arange).
print(f"\nZadanie {zadanie}\n")
zadanie += 1

collection9 = np.arange(0, 21, 2)
print(collection9)

# 8.	Utwórz tablicę 5 liczb równomiernie rozmieszczonych między 0 a 1 (np.linspace).
print(f"\nZadanie {zadanie}\n")
zadanie += 1

collection10 = np.linspace(0.0, 1.0, num=5)
print(collection10)

# 9.	Utwórz macierz jednostkową 4x4 (np.eye).
print(f"\nZadanie {zadanie}\n")
zadanie += 1

collection11 = np.eye(4, 4, dtype=int)
print(collection11)

# 10.	Wygeneruj tablicę 10 losowych liczb całkowitych z przedziału 1–100 (np.random.randint).
print(f"\nZadanie {zadanie}\n")
zadanie += 1

import random

collection12 = np.random.randint(1, 101, size=10)
print(collection12)

# 11.	Utwórz dwie tablice: a = np.array([1, 2, 3]), b = np.array([4, 5, 6]). Oblicz ich sumę, różnicę, iloczyn i iloraz.
print(f"\nZadanie {zadanie}\n")
zadanie += 1

a = np.array([1,2,3])
b = np.array([4,5,6])
print(f"Suma tablic {a} oraz {b}: {a + b}")
print(f"Różnica tablic {a} oraz {b}: {a - b}")
print(f"Różnica tablic {b} oraz {a}: {b - a}")
print(f"Iloczyn tablic {a} oraz {b}: {a * b}")
print(f"Iloraz tablic {a} oraz {b}: {a / b}")
print(f"Iloraz tablic {b} oraz {a}: {b / a}")

# 12.	Podnieś wszystkie elementy tablicy a do kwadratu (np.power lub np.square).
print(f"\nZadanie {zadanie}\n")
zadanie += 1

print(np.power(a, 2))
print(np.square(a))

# 13.	Używając funkcji oblicz średnią, sumę, minimum i maksimum elementów tablicy b.
print(f"\nZadanie {zadanie}\n")
zadanie += 1

print(f"Średnia {b}: {np.average(b)}")
print(f"Suma {b}: {np.sum(b)}")
print(f"Minimum {b}: {np.min(b)}")
print(f"Maksimum {b}: {np.max(b)}")

# 14.	Oblicz pierwiastek kwadratowy z każdego elementu w b (np.sqrt).
print(f"\nZadanie {zadanie}\n")
zadanie += 1

print(np.sqrt(b))

"""
15.	Utwórz tablicę arr = np.arange(10, 20).
a.	Wypisz pierwszy, trzeci i ostatni element.
b.	Wypisz elementy od indeksu 2 do 7.
c.	Odwróć kolejność elementów.
"""
print(f"\nZadanie {zadanie}\n")
zadanie += 1

arr = np.arange(10, 20)
print("a:", arr[0], arr[2], arr[-1])
print("b:", arr[2:8])
print("c:", arr[::-1])

"""
16.	Dla macierzy m = np.array([[1, 2, 3], [4, 5, 6], 7, 8, 9]])
a.	Wypisz pierwszy wiersz.
b.	Wypisz drugą kolumnę.
c.	Wypisz element z drugiego wiersza i trzeciej kolumny.
d.	Wypisz wszystkie elementy większe od 5.
"""
print(f"\nZadanie {zadanie}\n")
zadanie += 1

m = np.array([[1,2,3], [4,5,6], [7, 8, 9]])
print("a:", m[0])
print("b:", m[:, 1])
print("c:", m[1, 2])
print("d:", [int(y) for x in m for y in x if y > 5])
print("d:", m[m > 5])

"""
17.	Utwórz tablicę x = np.arange(1, 21).
a.	Wyświetl wszystkie liczby podzielne przez 3.
b.	Zastąp liczby większe od 10 wartością 99.
c.	Policz, ile elementów jest mniejszych od 8.
d.	Oblicz sumę tylko tych elementów, które są parzyste.
"""
print(f"\nZadanie {zadanie}\n")
zadanie += 1

x = np.arange(1, 21)
print("a:", x[x % 3 == 0])
print("b:", np.where(x <= 10, x, 99))
x[x > 10] = 99
print("b:", x)
print("c:", np.sum(x < 8))
print("c:", (x < 8).sum())
print("d:", np.sum([d for d in x if d % 2 == 0]))
print("d:", np.sum(x[x % 2 == 0]))

"""
18.	Użyj np.where do stworzenia nowej tablicy na postawie x, w której:
a.	liczby większe od 10 zostaną zamienione na 1,
b.	liczby mniejsze lub równe 10 – na 0.
c.	Warunki a i b są jednocześnie spełnione.
"""
print(f"\nZadanie {zadanie}\n")
zadanie += 1

x = np.arange(1, 21)
tmp = np.where(x > 10, 1, 0)
print(tmp)

# 19.	Wygeneruj losową tablicę 15 liczb całkowitych z przedziału 1–100. Wypisz elementy, które są większe niż średnia tablicy.
print(f"\nZadanie {zadanie}\n")
zadanie += 1

x = np.random.randint(1, 101, size=15)
print(np.average(x))
print(x[x > np.average(x)])

"""
20.	Dla tablicy arr = np.array([3, -7, 0, 5, -2, 9]):
a.	Zamień wszystkie liczby ujemne na 0.
b.	Zamień wszystkie liczby większe od 5 na 5.
"""
print(f"\nZadanie {zadanie}\n")
zadanie += 1

arr = np.array([3, -7, 0, 5, -2, 9])
print(arr)
arr = np.where(arr < 0, 0, arr)
print("a:", arr)
arr = np.where(arr > 5, 5, arr)
print("b:", arr)

"""
21.	Stwórz tablicę 2D 4×4 z losowymi liczbami całkowitymi z przedziału 1–10.
a.	Zamień wszystkie liczby nieparzyste na -1.
b.	Zamień wszystkie liczby parzyste na 1.
"""
print(f"\nZadanie {zadanie}\n")
zadanie += 1

arr = np.random.randint(1, 11, size= 4 * 4).reshape(4, 4)
print(arr)
arr[arr % 2 != 0] = -1
print("a:", arr)
arr[arr % 2 == 0] = 1
print("b:", arr)

"""
22.	Utwórz macierz 3×3 zawierającą liczby od 1 do 9.
a.	Oblicz sumę elementów w każdym wierszu (np.sum(axis=1)) i każdej kolumnie (axis=0).
b.	Znajdź element maksymalny i minimalny w całej macierzy.
c.	Oblicz średnią dla każdego wiersza osobno.
"""
print(f"\nZadanie {zadanie}\n")
zadanie += 1

arr = np.arange(1, 10).reshape(3, 3)
print(arr)
print("a:", np.sum(arr, axis=1), np.sum(arr, axis=0))
print("b:", np.max(arr), np.min(arr))
print("c:", np.mean(arr, axis=1))

"""
23.	Dla macierzy - A = np.array([[2, 4],[1, 3]]) i B = np.array([[5, 2],[3, 6]])
a.	Oblicz A + B, A - B, A * B (elementwise) 
b.	*Zrób to zadanie, jeśli miałeś styczność z mnożeniem macierzy na matematyce. A @ B (mnożenie macierzowe np.matmul).
c.	*Zrób to zadanie, jeśli miałeś styczność z odwrotnością macierzy na matematyce. Oblicz odwrotność macierzy A i sprawdź, czy A @ A⁻¹ daje macierz jednostkową(np.eye).
"""
print(f"\nZadanie {zadanie}\n")
zadanie += 1

from linalg import inv

a = np.array([[2, 4],[1, 3]])
b = np.array([[5, 2],[3, 6]])
print("a:", a + b, a - b, a * b, sep='\n')
print("b:", np.matmul(a, b))
print("b:", a @ b)
a_inv = np.linalg.inv(a)
print("c:", a_inv, np.allclose(a @ a_inv, np.eye(2)))

"""
24.	Utwórz macierz 4×4 z liczbami od 1 do 16.
a.	Wypisz elementy z przekątnej (np.diag).
b.	Odwróć wiersze i wyświetl.
c.	Odwróć kolumny i wyświetl.
d.	Zamień wiersze miejscami (pierwszy z ostatnim).
e.	Zamień tablicę dwuwymiarową na jedno wymiarową 
"""
print(f"\nZadanie {zadanie}\n")
zadanie += 1

arr = np.arange(1, 17).reshape(4, 4)
print("a:", np.diag(arr))
print("b:", arr[::-1])
print("c:", arr[:, ::-1])
arr_tmp = arr.copy()
arr_tmp[[0, -1]] = arr_tmp[[-1, 0]]
print("d:", arr_tmp)
print("e:", arr.reshape(arr.size))
print("e:", arr.flatten())
print("e:", arr.ravel())
print("e:", arr.reshape(-1))

# 25.	*Zrób to zadanie, jeśli miałeś styczność z normalizacją zbiorów danych. Stwórz jednowymiarową macierz 10 losowych liczb i wykonaj normalizację do zakresu 0-1.
print(f"\nZadanie {zadanie}\n")
zadanie += 1

arr = np.random.randint(0, 100, dtype= int, size = 10)
print(arr)
a_norm = (a - a.min()) / (a.max() - a.min())
print(a_norm)

"""
26.	Wygeneruj tablicę 20 liczb losowych z rozkładu jednostajnego (np.random.rand).
a.	Oblicz średnią, medianę, wariancję i odchylenie standardowe.
b.	Znajdź element najbliższy średniej.
"""
print(f"\nZadanie {zadanie}\n")
zadanie += 1

arr = np.random.rand(20)
print(arr)
print("a:", np.mean(arr), np.median(arr), np.var(arr), np.std(arr))
print("b:", arr[np.abs(arr - np.mean(arr)).argmin()])

"""
27.	Utwórz tablicę 2D o wymiarach 3×5 z losowych wartości i:
a.	oblicz średnią dla każdej kolumny (axis=0),
b.	oblicz sumę dla każdego wiersza (axis=1).
"""
print(f"\nZadanie {zadanie}\n")
zadanie += 1

arr = np.random.randint(0, 10, dtype=int, size=3 * 5).reshape(3, 5)
print("a:", np.mean(arr, axis=0))
print("b:", np.sum(arr, axis=1))

"""
28.	Wygeneruj tablicę 100 losowych wartości z rozkładu normalnego (np.random.randn(100)).
a.	Sprawdź, ile wartości mieści się w przedziale (-1, 1).
b.	Oblicz procent takich wartości.
"""
print(f"\nZadanie {zadanie}\n")
zadanie += 1

arr = np.random.randn(100)
print(arr)
print("a:", np.sum((arr > -1) & (arr < 1)))
print("b:", np.sum((arr > -1) & (arr < 1)) / arr.size * 100)

# 29.	Utwórz tablicę 10×10 z wartościami losowymi 0–100. Znajdź element minimalny, maksymalny oraz ich pozycje (np.argmax, np.argmin).
print(f"\nZadanie {zadanie}\n")
zadanie += 1

arr = np.random.randint(0, 100, size=10 * 10).reshape(10,10)
print(arr)
print(np.min(arr), np.unravel_index(np.argmin(arr), arr.shape), np.max(arr), np.unravel_index(np.argmax(arr), arr.shape))
print(np.where(arr == np.argmin(arr)))

"""
30.	Dla cen prices = np.array([9.99, 12.49, 7.50, 14.90, 3.99])
a.	Oblicz średnią i medianę ceny.
b.	Dodaj 23% VAT do każdej ceny.
c.	Sprawdź, które produkty kosztują więcej niż 10 zł po doliczeniu VAT.
"""
print(f"\nZadanie {zadanie}\n")
zadanie += 1

prices = np.array([9.99, 12.49, 7.50, 14.90, 3.99])
print(prices)
print(np.mean(prices), np.median(prices))
prices_with_taxes = prices * 1.23
print(prices_with_taxes)
prices_above_10 = prices_with_taxes > 10
print(prices_above_10)

"""
31.	Dla wyników uczniów scores = np.array([56, 78, 45, 89, 90, 67, 73, 100, 59])
a.	Znajdź średni wynik.
b.	Zwiększ wszystkie wyniki poniżej 60 o 10 punktów.
c.	Policz, ilu uczniów ma wynik powyżej 80.
d.	Oblicz procent zdawalności (przyjmij, że próg to 50 punktów).
"""
print(f"\nZadanie {zadanie}\n")
zadanie += 1

scores = np.array([56, 78, 45, 89, 90, 67, 73, 100, 59])
print(scores)
print(np.average(scores))
scores = np.where(scores < 60, scores + 10, scores)
print(scores)
top_students = np.sum(scores > 80)
print(top_students)
scores = np.array([56, 78, 45, 89, 90, 67, 73, 100, 59])
per_pass = np.sum(scores >= 50) / scores.size * 100
print(per_pass)

"""
32.	Dla danych pogodowych temps = np.array([[22, 25, 21], [18, 20, 19], [25, 27, 26], [23, 22, 24]])
a.	Oblicz średnią temperaturę każdego dnia (axis=1).
b.	Znajdź najcieplejszy i najchłodniejszy dzień.
c.	Przeskaluj wszystkie temperatury z Celsjusza na Fahrenheita.
"""
print(f"\nZadanie {zadanie}\n")
zadanie += 1

temps = np.array([[22, 25, 21], [18, 20, 19], [25, 27, 26], [23, 22, 24]])
print(temps)
aver = np.mean(temps, axis=1)
print(aver)
print(np.argmin(aver) + 1, temps[np.argmin(aver)], np.argmax(aver) + 1, temps[np.argmax(aver)])
temps = temps * 1.8 + 32
print(temps)

# 33.	Wygeneruj 1000 losowych rzutów monetą (0 = orzeł, 1 = reszka). Oblicz, ile było orłów i ile reszek.
print(f"\nZadanie {zadanie}\n")
zadanie += 1

arr = np.random.randint(0, 2, dtype=int, size=1000)
print(np.sum(arr == 0), np.sum(arr == 1))

# 34.	Zasymuluj 100 rzutów sześcienną kostką (np.random.randint(1, 7, 100)). Policz, ile razy wypadła każda liczba (użyj np.bincount).
print(f"\nZadanie {zadanie}\n")
zadanie += 1

arr = np.random.randint(1, 7, 100)
print(np.bincount(arr))

# 35.	Wylosuj 6 unikalnych liczb z przedziału 1–49. W tym celu znajdź funkcję z np.random która Ci to umożliwi.
print(f"\nZadanie {zadanie}\n")
zadanie += 1

arr = np.random.choice(range(1, 50), size=6, replace=False)
print(arr)

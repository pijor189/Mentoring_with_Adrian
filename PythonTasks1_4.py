"""
Zadania z pliku PythonTasks1 4
"""
from numpy.ma.core import append

# 1)	Napisz pętle, która utworzy listę liczb od 1 do 100
liczby = [x for x in range(1, 101)]
print(liczby)

# 2)	Napisz pętle, która utworzy listę liczb od 1 do 100 z krokiem 2
liczby = [x for x in range(1, 101, 2)]
print(liczby)

# 3)	Napisz pętle, która utworzy listę liczb od -1 do -100
liczby = [x for x in range(-1, -101, -1)]
print(liczby)

# 4)	Napisz pętle, która utworzy listę liczb od -1 do -100 z krokiem -3
liczby = [x for x in range(-1, -101, -3)]
print(liczby)

# 5)	Napisz pętle, która utworzy listę liczb od 100 do 1
liczby = [x for x in range(100, 0, -1)]
print(liczby)

# 6)	Napisz pętle, która utworzy listę liczb od 1000 do 10 z krokiem -10
liczby = [x for x in range(1000, 9, -10)]
print(liczby)

# 7)	Napisz pętle, która utworzy listę liczb od 1 do 100, jeśli są one podzielne przez 3
liczby = [x for x in range(1, 101) if x % 3 == 0]
print(liczby)

# 8)	Napisz pętle, która utworzy listę liczb od 1 do 100, jeśli są one parzyste
liczby = [x for x in range(1, 101) if x % 2 == 0]
print(liczby)

"""
9)	Napisz zagnieżdżoną pętle która utworzy tablicę 100 na 100 jak poniżej
1	2	3	4	5	6	7	8
2	3	4	5	6	7	8	9
3	4	5	6	7	8	9	10
4	5	6	7	8	9	10	11
5	6	7	8	9	10	11	12
6	7	8	9	10	11	12	13
7	8	9	10	11	12	13	14
8	9	10	11	12	13	14	15
"""
liczby = [print(y, end='\t') if y != x + 100 else print() for x in range(1, 101) for y in range(x, x + 101)]

# 10)	Napisz pętlę, która utworzy listę kwadratów liczb od 1 do 10
liczby = [x**x for x in range(1, 11)]
print(liczby)

# 11)	Napisz pętle od 1 do 10 z pomięciem 3 i 7
liczby = [x for x in range(1, 11) if x != 3 and x != 7]
print(liczby)

# 12)	Utwórz 100 elementową listę zawierającą same 0
liczby = [0 for x in range(1, 101)]
print(liczby)

"""
55)	Napisz funkcję, z pętlą która wyświetli liczby w poniższy sposób dla danego N. N jest liczbą naturalną do 10.
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""
def rysuj_trojkat_54(n: int):
    if n <= 10:
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                print(j, end=' ')
            print()
    else:
        print("Podane N jest za duże")

rysuj_trojkat_54(10)
print()

"""
56)	Napisz funkcję, z pętle która wyświetli liczby w poniższy sposób dla danego N. W poniższym przykładzie N = 3
1
1 2
1 2 3
1 2
1
Napisz pętle która wyświetli daną liczbę 
"""
def rysuj_trojkat_55(n: int):
    rozmiar = n + n - 1
    for i in range(1, rozmiar + 1):
        if i <= n:
            for j in range(1, i + 1):
                print(j, end=' ')
            print()
        else:
            for j in range(1, rozmiar + 2 - i):
                print(j, end=' ')
            print()

rysuj_trojkat_55(5)
print()

# 57)	Napisz funkcję zliczającą, ile razy zmieniła się kolejna wartość w liście [1, 1, 4, 2, 3, 3, 2, 1, 4]
def zmiana_wartosci(lista: list) -> int:
    licznik = 0
    for i in range(len(lista) - 1):
        if lista[i] != lista[i + 1]:
            licznik += 1

    return licznik

lista = [1,1,4,2,3,3,2,1,4]
print("W liście: {} wartości następujące po sobie zmieniały się: {} razy".format(lista, zmiana_wartosci(lista)))

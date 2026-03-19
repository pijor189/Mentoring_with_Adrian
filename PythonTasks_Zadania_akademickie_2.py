"""
Zadania z pliku PythonTasks - Zadania akademickie 2
"""

zadanie = 1
# 1.	Napisz funkcję, która odwróci podany string bez użycia [::-1]
print(f"\nZadanie {zadanie}\n")
zadanie += 1

def reverse_string(text: str) -> str:
    return str([text[x] for x in range(len(text) - 1, -1, -1)])
print(f"Text: {"string"} reversed text: {reverse_string("string")}")

# 2.	Napisz funkcję, która przyjmuje dwa stringi. Funkcja ma zwracać True, jeśli słowa są Anagramem.
print(f"\nZadanie {zadanie}\n")
zadanie += 1

def is_anagram(text1: str, text2: str) -> bool:
    if sorted(text1.lower()) == sorted(text2.lower()):
        return True
    return False

text1 = "karta"
text2 = "krata"
print(f"Are two string {text1} and {text2} anagrams?\n{is_anagram(text1, text2)}")
text1 = "karta"
text2 = "kraty"
print(f"Are two string {text1} and {text2} anagrams?\n{is_anagram(text1, text2)}")

# 3.	Naszym zadaniem jest zamiana ciągu `a4b3r6` na `aaaabbbrrrrrr`.
print(f"\nZadanie {zadanie}\n")
zadanie += 1

sequence = 'a4b3r6'
tmp = ''
for i in range(0, len(sequence), 2):
    tmp += sequence[i] * int(sequence[i + 1])
print(tmp)

# 4.	Napisz dekorator, który wypisze „przed” przed wywołaniem funkcji i „po” po wywołaniu funkcji (musisz umieć dekoratory na swoją rozmowę)
print(f"\nZadanie {zadanie}\n")
zadanie += 1

def decorator(func):
    def d():
        print("Before")
        func()
        print("After")
    return d

@decorator
def show():
    print("Hello")

show()

# 5.	Napisz funkcję, która zliczy litery w stringu.
print(f"\nZadanie {zadanie}\n")
zadanie += 1

def count_letters(text: str) -> int:
    counter = 0
    for letter in text:
        if letter.isalpha():
            counter += 1

    return counter

text = 'abcdefgh567--!  '
print(f"There are {count_letters(text)} letters in the {text}")

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

def append_to_file(file, content):
    if not os.path.isfile(file):
        return print(f"Error while reading, check if you provided the correct file")
    with open(file, "r") as f:
        tmp = f.read()
        print(f"File contents before saving {tmp}")
        number = int(tmp) + content

    with open(file, "w") as f:
        f.write(str(number))

    with open(file, "r") as f:
        print(f"File contents after saving {f.read()}")

append_to_file("plik_zad_6", 100)

"""7.	Stwórz własny generator, który będzie wypisywał liczby ciągu fibonaciego dla zadanego N oznaczającego, ile ma ich wygenerować.
wejście: 5
wyjście: 1, 1, 2, 3, 5
"""
print(f"\nZadanie {zadanie}\n")
zadanie += 1

def generate_Fib_seq(n: int) -> list:
    tab = []
    for i in range(n):
        if i < 2:
            tab.append(1)
        else:
            tab.append(tab[i - 2] + tab[i - 1])
    return tab

n = 10
print(f"Fibonacci sequence for the given N ={n} -> {generate_Fib_seq(n)}")

"""
8.	Napisz funkcję, która dostając listę, znajdzie i zwróci najczęściej występujący element. 
wejście: [1, 2, 2, 3, 3, 3]
wyjście: 3
"""
print(f"\nZadanie {zadanie}\n")
zadanie += 1

"""def znajdz_elem(lista: list):
    tmp = set(lista)
    tmp1 = dict()
    for val in tmp:
        tmp1[val] = lista.count(val)

    for key, val in enumerate(tmp1):
        if tmp1[val] is max(tmp1.values()):
            return val"""

def find_elem(collection: list):
    # lista z unikalnymi wartościami
    tmp = list(set(collection))
    # pierwszy element do porównań, obecnie traktowany jako najczęściej występujący
    tmp1 = collection.count(tmp[0])
    # indeks elementu z unikalnej listy, która występuje najczęściej w liście podanej jako parametr funkcji
    tmp2 = 0
    for i in range(1, len(tmp)):
        if tmp1 < collection.count(tmp[i]):
            tmp1 = collection.count(tmp[i])
            tmp2 = i

    return tmp[tmp2]

collection = [1, 2, 2, 3, 3, 3, 'a', 'a', 'a', 'a']
print(f"The most frequent element in the list {collection} is: {find_elem(collection)}")

"""
9.	Napisz funkcję która będzie sprawdzać, czy kolejność nawiasów się zgadza:
„{}()[]” -> True 
„({[]})” -> True 
„(({((}})” -> False
"""
print(f"\nZadanie {zadanie}\n")
zadanie += 1

def are_brackets_ok(string: str) -> bool:
    pairs = {'}' : '{', ']': '[', ')': '('}
    tab = []
    for char in string.strip():
        if char in pairs.values():
            tab.append(char)
        elif char in pairs:
            if tab[-1] == pairs[char]:
                tab.pop()
            else:
                return False
    return True

string = "{}(a)b[]"
print(f"Is the order of brackets correct in this case {string}?: {are_brackets_ok(string)}")
string = "({[]})"
print(f"Is the order of brackets correct in this case {string}?: {are_brackets_ok(string)}")
string = "(({((}})"
print(f"Is the order of brackets correct in this case {string}?: {are_brackets_ok(string)}")

"""
10.	Napisz funkcję która doda do siebie dwie liczby zapisane jako stringi bez użycia int().
„120” + „80” -> „200”. 
"""
print(f"\nZadanie {zadanie}\n")
zadanie += 1

# przyznaje, nie miałem tutaj pomysłu jak to zrobić, myślałem o zastosowaniu ASCII, ale nie pomyślałem, by to zrobić jak z dodawaniem pod kreskę i wspomogłem się trochę
def add_strings(string1: str, string2: str) -> str:
    # obliczamy rozmiary stringów oraz rozmiar pętli
    len1 = len(string1) - 1
    len2 = len(string2) - 1
    size_of_loop = len(string1) if len(string1) > len(string2) else len(string2)
    rest_of_sum = 0
    tab = []
    for i in range(size_of_loop, 0, -1):
        # zczytujemy pojedynczo cyfry od końca i dodajemy do siebie jak w dodawaniu pod kreską
        # żeby je poprawnie zczytać, zamieniamy je na kod ASCII i odejmujemy wartość 0 w ASCII, by odzwierciedlić liczbę
        tmp1 = ord(string1[len1]) - ord('0') if len1 >= 0 else 0
        tmp2 = ord(string2[len2]) - ord('0') if len2 >= 0 else 0
        sum_of_addition = tmp1 + tmp2 + rest_of_sum
        # jeśli suma większa niż 9, przenosimy resztę do kolejnej iteracji
        if sum_of_addition < 10:
            rest_of_sum = 0
        else:
            rest_of_sum = 1
            sum_of_addition = sum_of_addition - 10
        tab.append(str(sum_of_addition))
        len1 -= 1
        len2 -= 1

    return "".join(tab[::-1])

string1 = "140"
string2 = "80"
print(f"{string1} + {string2} = {add_strings(string1, string2)}")

"""
11.	Napisz funkcje sortującą krotki po drugim elemencie.
[(1,3),(2,1),(3,2)] -> [(2,1),(3,2),(1,3)]
"""
print(f"\nZadanie {zadanie}\n")
zadanie += 1

def sort_tuples_on_sec_elem(a):
    return sorted(a, key=lambda x: x[1])

a = [(1,3),(2,1),(3,2)]
print(f"Tuples before sorting: {a}\nTuples after sorting on the second element: {sort_tuples_on_sec_elem(a)}")
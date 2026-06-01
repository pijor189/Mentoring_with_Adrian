"""
Zadania z pliku Python Pandas 2
"""
import pandas as pd

exercise = 1
print(f"Exercise {exercise}")
exercise += 1
# 1)	Wczytaj dane z pd.read_csv() i je wyświetl.
# 2)	Czy zauważyłeś coś dziwnego? – mamy zdublowane indeksy. Znajdź w dokumentacji argument, który pozwoli
# zadeklarować, która kolumna posłuży nam za indeksy i wczytaj jeszcze raz tabelę.
# 3)	Sprawdź co robią funckje head(), info() i describe() na wczytanym dataframie.
# 4)	info(), nie jest w stanie rozpoznać wszystkich typów danych. Korzystając raz jeszcze z dokumentacji, znajdź
# argument, który pozwoli Ci na zadeklarowanie typów, podczas czytania string’ów.
# 5)	Zduplikuj plik klienci.csv. Otwierając go w dowolnym edytorze tekstowym, zamień separatory z ‘,’ przecinka
# na ‘;’ średnik. Tak zmieniony plik zapisz i wczytaj używając pd.read_csv() z odpowiednim argumentem.
# 6)	Wczytaj plik z użyciem argumentów dtype i parse_dates
data = pd.read_csv("materialy/dane_pandas_1_.csv", sep=';', index_col="customer_id",
                   dtype={"last_purchase": str}, parse_dates=True)
# nie dało się zrobić bezpośrednio w dtype na float, więc trzeba usunąć spacje i zmienić , na . i dopiero, potrzebne
# to było do zadania 9 m.in.
data['total_spend'] = data['total_spend'].str.strip()
data['total_spend'] = data['total_spend'].str.replace(',', '.')
data['total_spend'] = pd.to_numeric(data['total_spend'])
print(data)
print("\nZastosowanie head()\n")
print(data.head(2))
print("\nZastosowanie info()\n")
print(data.info())
print("\nZastosowanie describe()\n")
print(data.describe())
print()

"""
7)	Wyświetl
a)	Pierwsze 3 wiersze
b)	Ostatnie 2 wiersze
"""
exercise = 7
print(f"\nExercise {exercise}\n")
exercise += 1
print("\nPierwsze 3 wiersze\n")
print(data.head(3))
print("\nOstatnie 2 wiersze\n")
print(data.tail(2))
# 8)	Wyświetl średni wiek klientów
print(f"\nExercise {exercise}\n")
exercise += 1
print(data['age'].mean())
# 9)	Minimalną i maksymalną wartość w total_spend
print(f"\nExercise {exercise}\n")
exercise += 1
print(data['total_spend'].min(), data['total_spend'].max())
# 10)	Wyświetl tylko kolumny name i city
print(f"\nExercise {exercise}\n")
exercise += 1
print(data[['name','city']])
# 11)	Posortuj klientów rosnąco według total_spend
print(f"\nExercise {exercise}\n")
exercise += 1
print(data['total_spend'].sort_values(ascending=True, inplace=False))
# 12)	Wyświetl wszystkich klientów powyżej 30lat
print(f"\nExercise {exercise}\n")
exercise += 1
print(data[data['age'] > 30])
# 13)	Wyświetl tylko dane klientów z miasta Gdańsk lub Warszawa
print(f"\nExercise {exercise}\n")
exercise += 1
print(data[data['city'].isin(['Gdansk', 'Warszawa'])])
# 14)	Wyświetl tylko klientów, których total_spend jest większy niż 1000
print(f"\nExercise {exercise}\n")
exercise += 1
print(data[data['total_spend'] > 1000])
"""
15)	Dodaj nową kolumnę spend_category, zdefiniuj ją według reguły
•	„mało” jeśli wydali mniej niż 1000
•	„średnio” jeśli wydali pomiędzy 1000 a 2000
•	„dużo” jeśli wydali ponad 2000
"""
print(f"\nExercise {exercise}\n")
exercise += 1
data["spend_category"] = "dużo"
data.loc[data["total_spend"].between(1000, 2000), "spend_category"] = "średnio"
data.loc[data["total_spend"] < 1000, "spend_category"] = "mało"
print(data)
# 16)	Oblicz i wyświetl ilu klientów należy do poszczególnych kategorii spend_category
print(f"\nExercise {exercise}\n")
exercise += 1
print(data['spend_category'].value_counts())
# 17)	Zamień nazwy miast na pisane małą literą
print(f"\nExercise {exercise}\n")
exercise += 1
data['city'] = data['city'].str.lower()
print(data['city'])
# 18)	Utwórz kolumnę days_since_last_purchase i uzupełnij je ilością dni od ostatniego zakupu do dziś.
# (today = pd.Timestamp("2025-11-21"), przykładowa aktualna data)
print(f"\nExercise {exercise}\n")
exercise += 1
today = pd.Timestamp.today()
data['days_since_last_purchase'] = (today - pd.to_datetime(data['last_purchase'], dayfirst=True)).dt.days
print(data['days_since_last_purchase'])
# 19)	Wyświetl klienta z najświeższym zakupem
print(f"\nExercise {exercise}\n")
exercise += 1
print(data.loc[data['days_since_last_purchase'].idxmin()])
# 20)	Sprawdź średnie wydatki (total_spend) pogrupowane po mieście (city)
print(f"\nExercise {exercise}\n")
exercise += 1
print(data.groupby("city")["total_spend"].mean())
# 21)	Wyciągnij z kolumny name imię i nazwisko i umieść je w osobnych kolumnach first_name i last-name
print(f"\nExercise {exercise}\n")
exercise += 1
data[["first_name", "last_name"]] = data["name"].str.split(" ", expand=True)
print(data)
"""
Zmodyfikuj wczytaną tabelę używając komend.
"""
data.loc[2, "city"] = None
data.loc[4, "total_spend"] = None
data.loc[1, "age"] = None

# 22)	Znajdź i wyświetl w których kolumnach są Null
print(f"\nExercise {exercise}\n")
exercise += 1

print(data.columns[data.isnull().any()])
# 23)	Policz liczbę Null w każdej kolumnie
print(f"\nExercise {exercise}\n")
exercise += 1

print(data.isnull().sum())
# 24)	Policz procent brakujących danych
print(f"\nExercise {exercise}\n")
exercise += 1

print(round(data.isnull().sum().sum() / data.size * 100, 2))
# 25)	Wyświetl tylko wiersze, które mają braki
print(f"\nExercise {exercise}\n")
exercise += 1

print(data[data.isnull().any(axis=1)])
# 26)	Usuń wiesze które zawierają braki
print(f"\nExercise {exercise}\n")
exercise += 1

print(data.dropna())
# 27)	Uzupełnij puste wartości w kolumnie age wstawiają średnią wieku
print(f"\nExercise {exercise}\n")
exercise += 1

print(data['age'])
data['age'] = data['age'].fillna(round(data['age'].mean()))
print(data['age'])
# 28)	Uzupełnij puste wartości w kolumnie city tekstem „Nieznane”
print(f"\nExercise {exercise}\n")
exercise += 1

data['is_missing_city'] = ~data['city'].isna()
print(data['is_missing_city'])

print(data['city'])
data['city'] = data['city'].fillna('Nieznane')
print(data['city'])
# 29)	Stwórz nową kolumnę is_missing_city i uzupełnij ją wartościami boolean w zależności od tego czy miasto zostało podane.
print(f"\nExercise {exercise}\n")
exercise += 1

data['is_missing_city'] = ~data['city'].isna()
print(data['is_missing_city'])

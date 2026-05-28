"""
    Zadania z pliku Python_API_Tasks_1
"""
import json

exercise = 1
print(f"Exercise {exercise}")
exercise += 1
# 1.	Zapoznaj się z NBP Web API (przeczytaj o dostępnych opcjach) (https://api.nbp.pl/)
# 2.	Za pomocą biblioteki request pobierz aktualny kurs euro. Pobierz go w formacie XML oraz JSON.
# Z obu rodzajów danych wyciągnij dokładną wartość i przypisz ją do zmiennej typu float
import requests
import xmltodict

print("\nXML")
euro_xml = requests.get('https://api.nbp.pl/api/exchangerates/rates/a/eur/?format=xml')
print(euro_xml.text)
euro_xml = xmltodict.parse(euro_xml.text)
euro_value_from_xml = euro_xml['ExchangeRatesSeries']['Rates']['Rate']['Mid']
euro_value_from_xml = float(euro_value_from_xml)
print(euro_value_from_xml)
print(type(euro_value_from_xml))

print("\nJSON")
euro_json = requests.get('https://api.nbp.pl/api/exchangerates/rates/a/eur/?format=json')
print(type(euro_json))
euro_json = euro_json.json()
print(euro_json)
euro_value_from_json = euro_json['rates'][0]['mid']
print(euro_value_from_json)
print(type(euro_value_from_json))

# 3.	Napisz funkcję, która będzie pobierać żądany kurs. def get_exchange_rates(currency: str) -> float:
print(f"Exercise {exercise}")
exercise += 1

def get_exchange_rates(currency: str) -> float:
    data_a = requests.get(f"https://api.nbp.pl/api/exchangerates/tables/a/?format=json")
    data_b = requests.get(f"https://api.nbp.pl/api/exchangerates/tables/b/?format=json")
    data_a = data_a.json()
    data_b = data_b.json()
    data = data_a[0]['rates'] + data_b[0]['rates']

    for val in data:
        if currency == val['currency']:
            return val['mid']
    print("There is no currency like the one you provided")
    return 0.0

get_exchange_rates('bat')

# 4.	Rozszerz funkcję o obsługę danych historycznych. def get_exchange_rates(currency: str,
# date_from: str, date_to: str = None) -> float:
print(f"Exercise {exercise}")
exercise += 1

from _datetime import date, timedelta

def find_currency(currency: str) -> tuple[str, str] | None:
    if not currency:
        print("The provided currency is not valid.")
        return None

    data_a = requests.get(f"https://api.nbp.pl/api/exchangerates/tables/a/?format=json")
    data_a = data_a.json()

    for val in data_a[0]['rates']:
        if currency == val['currency']:
            return val['code'], 'a'
    else:
        data_b = requests.get(f"https://api.nbp.pl/api/exchangerates/tables/b/?format=json")
        data_b = data_b.json()

        for val in data_b[0]['rates']:
            if currency == val['currency']:
                return val['code'], 'b'
        else:
            print("404 Not Found\nThe provided currency is not available.")
            return None


def get_exchange_rates(currency: str, date_from: str, date_to: str = None) -> dict | None:
    try:
        code, table = find_currency(currency)
    except TypeError:
        print("404 Not Found\nThe provided currency is not available or is not valid")
        return None

    try:
        if not date_to:
            dt = date.today()
        else:
            dt = date.fromisoformat(date_to)

        df = date.fromisoformat(date_from)

        if dt > date.today():
            raise ValueError

        if df > dt:
            raise ValueError

    except ValueError:
        print("400 Bad Request")
        return None

    exchange_rates = {}

    if dt.year == df.year or (df.year + 1 == dt.year and df.month >= dt.month):
        data = requests.get(f'https://api.nbp.pl/api/exchangerates/rates/{table}/{code}/{df}/{dt}/')
        data = data.json()

        for val in data['rates']:
            exchange_rates[val['effectiveDate']] = val['mid']
    else:
        actual_year = df.year

        while True:
            if actual_year == df.year:
                end_year_date = f"{actual_year + 1}-01-01"
                data = requests.get(f'https://api.nbp.pl/api/exchangerates/rates/{table}/{code}/{df}/\
                    {end_year_date}/')
                data = data.json()

                for val in data['rates']:
                    exchange_rates[val['effectiveDate']] = val['mid']
            elif actual_year == dt.year:
                last_year_date = f"{dt.year}-01-01"
                data = requests.get(f'https://api.nbp.pl/api/exchangerates/rates/{table}/{code}/\
                    {last_year_date}/{dt}/')
                data = data.json()

                for val in data['rates']:
                    exchange_rates[val['effectiveDate']] = val['mid']

                break
            else:
                data = requests.get(f'https://api.nbp.pl/api/exchangerates/rates/{table}/{code}/{actual_year}\
                -01-01/{actual_year + 1}-01-01/')
                data = data.json()

                for val in data['rates']:
                    exchange_rates[val['effectiveDate']] = val['mid']

                if f"{actual_year + 1}-01-01" == date_to:
                    break

            actual_year += 1
    try:
        if len(exchange_rates) == 0:
            raise ValueError
        return exchange_rates

    except ValueError:
        print("404 Not found")
        return None


print(get_exchange_rates('bat (Tajlandia)', '2027-01-01', '2026-01-01'))
print(get_exchange_rates('balt (Tajlandia)', '2012-01-01', '2012-01-31'))

# print(get_exchange_rates('bat (Tajlandia)', '2012-01-01', '2012-01-31'))
# print(get_exchange_rates('bat (Tajlandia)', '2012-01-01', '2015-06-01'))
# print(get_exchange_rates('bat (Tajlandia)', '2026-05-24'))

# 5.	Zastanów się w jaki sposób obsłużyć przypadek, w którym podany jest tylko jeden dzień, a nie przedział.
# Np. get_exchange_rates(„USD”, „2026-02-25”)
# 6.	Do powyższej funkcji dopisz obsługę błędów adekwatną do komunikatów błędów obsługiwanych przez BNP.
# (Poszerz ją o brakujące argumenty)
# 7.	Utwórz trzy wywołania funkcji get_exchange_rates(), które udowodnią, że obsługa błędów działa prawidłowo.
# 8.	Oblicz średni kurs Euro z ostatnich 15 dni.

def get_date_from_days(days: int) -> str:
    date_from = date.today() - timedelta(days)

    return date_from.isoformat()

def get_avg_currency(currency: str, days: int) -> float:
    data = get_exchange_rates(currency, get_date_from_days(days))

    return round(sum(data.values()) / len(data.values()), 2)

print(f"Average currency of {'euro'} from {15} days is {get_avg_currency('euro', 15)}\n")

# 9.	Sprawdź w jaki sposób zapisujemy typ formatu json do pliku. Zapisz w ten sposób kurs Euro z ostatnich 15 dni.

def log_currency_to_file(currency: str, days: int) -> None:
    data = get_exchange_rates(currency, get_date_from_days(days))

    with open("materialy/euro_last_15_days.json", "w", encoding="utf-8") as f:
        json.dump(data, f)

log_currency_to_file('euro', 15)

# 10.	Napisz pseudo-aplikacje w terminalu (wykorzystaj input()), która będzie pytać użytkownika, ile ma złotych
# i na jaką walutę chciałby je przewalutować. Aplikacja ta ma zwrócić przewalutowaną wartość.

def currency_exchange(balance: int | float, currency: str) -> int | float | None:
    try:
        code, _ = find_currency(currency)
    except:
        print("Not valid currency")
        return None

    data = requests.get(f'https://api.nbp.pl/api/exchangerates/rates/c/{code}/today/')
    data = data.json()

    return round(balance / data['rates'][0]['ask'], 2)

# zloty = int(input("How many zloty you have?: \n"))
# currency = input("What currency you want?: \n")
# print(f"{zloty} złoty -> {currency_exchange(zloty, currency)} {currency}")

# 11.	Za pomocą matplot narysuj wykres zmian kursu GBP w przeciągu ostatnich 60dni.
import matplotlib.pyplot as plt

data = get_exchange_rates('funt szterling', get_date_from_days(60))
x = [d for d, _ in enumerate(data.keys(), start=1)]
y = [c for c in data.values()]

plt.plot(x, y, marker='o', color='b', linestyle='-', linewidth=2)
plt.title("Wykres zmian kursu GDB")
plt.xlabel("Dni")
plt.ylabel("Kursy")
plt.grid(True)
plt.show()

# 12.	API NBP ma limit 93 dni dla zapytań. Jeśli zapytanie je przekroczy, spraw, aby Twoje rozwiązanie
# automatycznie dzieliło je na mniejsze.


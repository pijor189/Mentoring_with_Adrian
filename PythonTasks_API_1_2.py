"""
Disclaimer Ta sekcja ma na celu pokazać Ci inne API, a pech też chciał, że jest ono bardzo nieprzyjemne dla użytkownika
i posiada relatywnie mało wiedzy w Internecie. Biorąc to pod uwagę, weź te zadania na luzie, bardziej jako wyzwanie do
zabawy z którym trzeba wiele eksperymentować i szukać samemu rozwiązań – w razie czego pytaj :).
Nasz Endpoint to - https://dane.gov.pl/<api_ver>/<rest of the path> dane.gov.pl api
Na potrzeby zadania znalazłem bazę danych na Strona główna - Otwarte Dane w której znajdują się imiona męskie i żeńskie
 nadawane dzieciom w 2025. Patrząc na link, możemy znaleźć interesujący nasz resource id - 1187350, którego użyjemy w
  naszym API. Tabela ta zawiera 25864 wpisy. Imiona pierwsze nadane dzieciom w Polsce w 2025 r. wg USC - Otwarte Dane
  – zapoznaj się z tym jaki rodzaj innych danych zawiera ta tabela - poza imieniem.

13.	Do sprawdzenia formatu danych na pobranych danych, możesz użyć response.headers["Content-Type"]. Typ danych który
 otrzymujemy powinien być typu application/……json. Jeśli nie jest, napisz do mnie :) (sam się tu mocno zaskoczyłem)
14.	Moduł request, posiada również interesujący parametr nazywający się param. Pozwala on nam na dodanie słów kluczy
w wyszukiwarce, które znajdują się za przecinkiem  . Pozwoli Ci to na filtrowanie danych które są zwracane.
Korzystając z tej wiedzy pobierz 1000 wpisów z bazy imion.
"""
import time

import requests

data = []
count = int(1000 / 50)
url = 'https://api.dane.gov.pl/1.4/resources/1187350/data'

for key in range(1, count + 1):
    response = requests.get(url ,params={"page": 1, "per_page": 50})
    content_type = response.headers.get("Content-Type", "")
    if "application/vnd.api+json" in content_type:
        payload = response.json()
        data += payload.get("data", [])

for item in data:
    print(item['attributes'])

"""
15.	Korzystając z samego modułu request pobierz najczęściej oraz najrzadziej występujące męskie i damskie imię.
(odp. Amadeusz=2, Jan=632, Anastazja=2, Zofia=475)
(Dopuszczam, że mogą się tu pojawić inne imiona dla minimalnej ilości.)
"""
data = []
page = 1
url = 'https://api.dane.gov.pl/1.4/resources/1187350/data'


def get_api_result(url: str, params: dict) -> list | str:
    response = requests.get(url, params=params)
    content_type = response.headers.get("Content-Type", "")

    if not "application/vnd.api+json" in content_type:
        return f"Another content type as expected: {content_type}"

    payload = response.json()

    try:
        data = payload["data"]
    except KeyError as e:
        return f"Invalid params: {e}"

    if not data:
        return "Not data"

    result = []

    for d in data:
        for key, val in d.items():
            if key == "attributes":
                person = []
                for i in range(1, 8):
                    value = val[f"col{i}"]['val']
                    person.append(value if isinstance(value, str) else int(value))
                if len(data) == 1:
                    result = person
                else:
                    result.append(person)

    return result


print(get_api_result(url, {"page": 1, "per_page": 2}))
print(get_api_result(url, {"page": 1, "per_page": 1, "q": "col6:kobieta", "sort": "col7"}))
print(get_api_result(url, {"page": 1, "per_page": 1, "q": "col6:kobieta", "sort": "-col7"}))
print(get_api_result(url, {"page": 1, "per_page": 1, "q": "col6:mężczyzna", "sort": "col7"}))
print(get_api_result(url, {"page": 1, "per_page": 1, "q": "col6:mężczyzna", "sort": "-col7"}))
print(get_api_result(url, {"page": 1, "per_page": 1, "q": "col5:Damian", "sort": "-col7"}))

"""
16.	Przefiltruj dane dla imienia Damian. W jakim Województwie nadano to imię najczęściej oraz w jakiej ilości?
17.	Stwórz swoje własne zapytanie :).
"""

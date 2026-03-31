"""
Zadania z pliku Python Tasks - wyjątki i algorytmy 1
"""
from math import expm1
from sys import exception

exercise = 1

# 1)	Napisz obsługę przechwytywania wyjątku dzielenia przez zero w bloku try-except dla operacji 1/0.
print(f"Exercise {exercise}")
exercise += 1

try:
    a = 1
    b = 0
    c = a / b
except:
    print("Attempt to divide by 0, an error was returned")

# 2)	Rozszerz powyższe rozwiązanie o brakującą obsługę wyjątków z grupy ZeroDivisionError, ArithmeticError, Exception.
print(f"Exercise {exercise}")
exercise += 1

try:
    a = 1
    b = 0
    c = a / b
except ZeroDivisionError as e:
    print(f"Attempt to divide by 0, an error {e} was returned")
except ArithmeticError as e:
    print(f"ArithmeticError was returner: {e}")

# 3)	Sprawdź jakie znaczenie ma kolejność w zadaniu 2, napisz jaka kolejność jest poprawna.
print(f"Exercise {exercise}")
exercise += 1

try:
    a = 1
    b = 0
    c = a // b
except SyntaxError as e:
    print(f"Invalid syntax {e}")
except ZeroDivisionError as e:
    print(f"Attempt to divide by 0, an error {e} was returned")
except ArithmeticError as e:
    print(f"ArithmeticError was returner: {e}")
# patrząc na to, że wpisałem ZeroDivisionError jako ostatnie w tym przypadku, to i tak zwróciło ten błąd

# 4)	Rozszerz powyższe rozwiązanie o blok else, w którym rzucisz wyjątek (raise()) PermissionError, że żaden wyjątek nie został rzucony.
print(f"Exercise {exercise}")
exercise += 1

try:
    a = 1
    b = 1
    c = a / b
except SyntaxError as e:
    print(f"Invalid syntax {e}")
except ZeroDivisionError as e:
    print(f"Attempt to divide by 0, an error {e} was returned")
except ArithmeticError as e:
    print(f"ArithmeticError was returner: {e}")
except PermissionError as e:
    print(f"No exception was thrown: {e}")
else:
    pass
    # raise PermissionError

# 5)	Utwórz wyjątko-cepecje. Umieść całą obsługę wyjątków którą napisałeś, w kolejnym bloku try-except. Tym, razem oczekuj rzuconego przez Ciebie wyjątku PermissionError.
#       W else wyprintuj że „Something is no yes”, a w finally „All is gud.”. Co się wyświetli?
print(f"Exercise {exercise}")
exercise += 1

try:
    try:
        a = 1
        b = 1
        c = a / b
    except SyntaxError as e:
        print(f"Invalid syntax {e}")
    except ZeroDivisionError as e:
        print(f"Attempt to divide by 0, an error {e} was returned")
    except ArithmeticError as e:
        print(f"ArithmeticError was returner: {e}")
    except PermissionError as e:
        print(f"No exception was thrown: {e}")
    else:
        raise PermissionError
except PermissionError as e:
    print(f"Something is no yes: {e}")
finally:
    print(f"All is gud")
# wyświetliło się obsłużenie wyjątku PermissionError jednak bez żadnego kodu błędu, do którego próbuje się odwołać w ramach print(), dodatkowo wyświetla się zawsze finally

# 6)	Napisz jeszcze raz obsługę wyjątków try, except Exception as e dla 1/0.
#       Tym razem w bloku obsługi błędu wyświetl nazwę klasy wyjątku (polecam zgooglować), argumenty wyjątku, typ, treść zawierające się w e.
print(f"Exercise {exercise}")
exercise += 1

import traceback

try:
    a = 1
    b = 0
    c = a // b
except SyntaxError as e:
    print(f"Invalid syntax {e}")
except ZeroDivisionError as e:
    print(f"Attempt to divide by 0, an error {e} was returned")
    print(f"{e.__class__.__name__}")
    print(f"{e.args}")
    print(f"{type(e)}")
    print(f"{str(e)}")
    # traceback.print_exc()
except ArithmeticError as e:
    print(f"ArithmeticError, an error {e} was returned")
    print(f"{e.__class__.__name__}")
    print(f"{e.args}")
    print(f"{type(e)}")
    print(f"{str(e)}")
    # traceback.print_exc()

# 7)	Napisz własną klasę wyjątków PythonTasksError (Jest to klasa, która dziedziczy po Exception) po której będą dziedziczyć pozostałe wyjątki w zadaniach.
print(f"Exercise {exercise}")
exercise += 1

class PythonTasksError(Exception):
    pass

try:
    raise PythonTasksError
except PythonTasksError as e:
    print(f"Error: {e}")


"""
8)	Napisz pierwszy wyjątek dziedziczący po PythonTasksError - WednesdayError oraz rzuć go za pomocą raise() w nowej metodzie is_it_wednesday_my_dudes().
W tym celu możesz wykorzystać poniższy kod:

from datetime import date
if date.today().weekday() == 2:
"""
print(f"Exercise {exercise}")
exercise += 1

class WednesdayError(PythonTasksError):
    def __init__(self, comunicate: str):
        self.comunicate = comunicate

    def __str__(self):
        return f"{self.__class__.__name__}"


def is_it_wednesday_my_dudes():
    raise WednesdayError("it's wednesday error dude")

try:
    raise WednesdayError("bo tak")
    is_it_wednesday_my_dudes()
except WednesdayError as e:
    print(f"Error was raised: {e.comunicate}")

class Suma:
    def __init__(self):
        self.a = "Imie"
        self.b = "Nazwisko"

    def __str__(self):
        return f"{self.a + ' ' + self.b}"

s = Suma()
print(s)

a = 1
b = 1
print(a is b)
print(id(a))
print(id(b))
print(frozenset([1,2,3]))
print(bytearray([1,2,3]))
"""
9)	Napisz klasę Kalkulator z metodami:
•	sum(a, b), która rzuca wyjątek SmallScreenError, jeśli suma jest większa niż milion i udajemy, że nie jest w stanie jej wyświetlić
•	substract(a, b), te akurat działającą :) 
•	divide(a, b), która przechwyci domyślny wyjątek w przypadku dzielenia przez 0, napisze „nie dzieli się przez 0” i rzuci ten sam wyjątek.
•	sqrt(x), która rzuca wyjątek NegativeRootError, jeśli liczby jest ujemna
"""
print(f"Exercise {exercise}")
exercise += 1

class SmallScreenError(PythonTasksError):
    pass

class NegativeRootError(PythonTasksError):
    pass

class Calculator:
    def __init__(self, a: int | float, b: int | float):
        self.a = a
        self.b = b

    def __str__(self):
        return f"{self.a}, {self.b}"

    def set_a_b(self, a: int | float, b: int | float):
        self.a = a
        self.b = b

    def sum(self) -> int | float:
        result = self.a + self.b
        if result < 1_000_000:
            return result
        else:
            raise SmallScreenError

    def substract(self) -> int | float:
        return self.a - self.b

    def divide(self) -> int | float:
        return a / b

    def sqrt(self) -> int | float:
        result = self.a ** 0.5
        print(type(result))
        if result > 0:
            return result
        else:
            raise NegativeRootError

try:
    calculator = Calculator(5, 0)
    # calculator.divide()
    calculator.set_a_b(1_000_000, 0)
    calculator.sum()
    calculator.set_a_b(-1,-1)
    calculator.sqrt()
except NegativeRootError as e:
    print(f"NegativeRootError: {e}")
except TypeError as e:
    print(f"We have a problem: {e}")
except ZeroDivisionError as e:
    print(f"Attempt to divide by 0: {e}")
    raise ZeroDivisionError
except SmallScreenError as e:
    print(f"The display is too small, it is not possible to show the result of the operation. Error code: {e}")


"""
10)	Napisz klasę walidującą formularz. Klasa ma przyjmować dane użytkownika w postaci słownika.
{
    "name": "Jan",
    "age": 17,
    "email": "jan@mail.com",
}
Napisz odpowiednie mechanizmy sprawdzające poprawność danych. Rzuć adekwatny wyjątek zawierający informację, które pole jest błędne oraz dlaczego.
"""
print(f"Exercise {exercise}")
exercise += 1

class FormIsNotValid(PythonTasksError):
    def __init__(self, field, communicate):
        self.field = field
        self.communicate = communicate

    def __str__(self):
        return f"Error in '{self.field}': {self.communicate}"


class CheckForm:
    def __init__(self, form: dict):
        self.form = form

    def __str__(self):
        return f"{self.form}"

    def isValidForm(self):
        if not isinstance(self.form, dict) or len(self.form) == 0:
            raise FormIsNotValid("form", "Missing form")

        name = self.form.get("name")
        if not name:
            raise FormIsNotValid("name", "missing name")
        elif not isinstance(name, str) or not name.isalpha():
            raise FormIsNotValid("name", "name should be a string with only alphabetic chars")

        age = self.form.get("age")
        if not age:
            raise FormIsNotValid("age", "missing age")
        elif not isinstance(age, int):
            raise FormIsNotValid("age", "age should be an integer")
        elif age < 0:
            raise FormIsNotValid("age", "age should be not a smaller than 0")

        email = self.form.get("email")
        if not email:
            raise FormIsNotValid("email", 'missing email')
        elif "@" not in email or "." not in email[email.index("@"):]:
            raise FormIsNotValid("email", 'invalid email')

        if len(self.form.keys()) != 3:
            raise FormIsNotValid("key", "More/less keys than expected")

        return True

try:
    example_form = {"name": "Jan", "age": 17, "email": "jan@mail.com"}
    example_form1 = {"name": "Jan", "age": 17}
    example_form2 = {"name": "Jan", "age": 17, "email": "janmail.pl"}
    example_form3 = {}
    form_to_check = CheckForm(example_form3)
    if form_to_check.isValidForm():
        print(f"Everything is okay with form: {form_to_check}")
except FormIsNotValid as e:
    print(e)


# 11)	Napisz funkcję, która przyjmie dowolną kolekcję liczb i posortuje ją bąbelkowo
print(f"Exercise {exercise}")
exercise += 1

collection = [2,5,1,0,99,18,22,11,14,8]

def bubble_sort(collection: list[int]) -> list[int]:
    for i in range(len(collection)):
        swap = False
        for j in range(len(collection) - i - 1):
            if collection[j] > collection[j + 1]:
                collection[j], collection[j + 1] = collection[j + 1], collection[j]
                swap = True
        if not swap:
            break
    return collection

print(f"Before bubble sort: {collection}\nAfter bubble sort: {bubble_sort(collection)}")

# 12)	Dla urozmaicenia zadania 11, rozszerz go o porównywanie elementów z użyciem lambdy, o ile tego nie zrobiłeś.
print(f"Exercise {exercise}")
exercise += 1

collection = [2,5,1,0,99,18,22,11,14,8]

# ascending sort by default
def bubble_sort_lambda(collection: list[int], key=lambda x: x) -> list[int]:
    for i in range(len(collection)):
        swap = False
        for j in range(len(collection) - i - 1):
            # In this place, we use a key that defines what type of sorting we want: descending, ascending, by even numbers, etc.
            if key(collection[j]) > key(collection[j + 1]):
                collection[j], collection[j + 1] = collection[j + 1], collection[j]
                swap = True
        if not swap:
            break
    return collection

# descending sort
print(f"Before bubble sort: {collection}\nAfter bubble sort: {bubble_sort_lambda(collection, key=lambda x: -x)}")
# even numbers at the end and ascending
print(f"Before bubble sort: {collection}\nAfter bubble sort: {bubble_sort_lambda(collection, key=lambda x: (x % 2 == 0, x))}")
# even numbers at the beginning and descending
print(f"Before bubble sort: {collection}\nAfter bubble sort: {bubble_sort_lambda(collection, key=lambda x: (x % 2 != 0, -x))}")
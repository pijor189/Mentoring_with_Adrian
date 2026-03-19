"""
Zadania z pliku PythonTasks4 4
"""

zadanie = 1
# 1)	Stwórz klasę Dog, która będzie miała zahardcodowane atrybuty name, numer_of_legs, breed, age oraz metodę make_sound()
print(f"\nZadanie {zadanie}\n")
zadanie += 1

class Animal:
    def __init__(self, name: str, numer_of_legs: int, breed: str, age: int):
        self.name = name
        self.numer_of_legs = numer_of_legs
        self.breed = breed
        self.age = age

    def __str__(self):
        return f"Imię: {self.name}, liczba nóg: {self.numer_of_legs}, rasa: {self.breed}, lat: {self.age}"

    def make_sound(self):
        pass

class Dog(Animal):
    def __init__(self, name: str, numer_of_legs: int, breed: str, age: int):
        super().__init__(name, numer_of_legs, breed, age)

    def make_sound(self):
        print("Hau hau")

dog1 = Dog("Luna", 4, "Kundel", 2)
print(dog1)
dog1.make_sound()

# 2)	Stwórz klasę Counter, która będzie miała wewnętrzny stan licznika oraz metody increment(), show() oraz reset()
print(f"\nZadanie {zadanie}\n")
zadanie += 1

class Counter:
    def __init__(self):
        self.counter = 0

    def __str__(self):
        return f"{self.counter}"

    def increment(self):
        self.counter += 1

    def show(self):
        print(f"Wartość countera wynosi: {self}")

    def reset(self):
        self.counter = 0

counter = Counter()
counter.show()
counter.increment()
counter.show()
counter.reset()
counter.show()

# 3)	Stwórz klasę Person, która będzie miała name, surname oraz metodę introduce(), której zadaniem będzie wyświetlenie zdania „Cześć, nazywam się …”
print(f"\nZadanie {zadanie}\n")
zadanie += 1

class Person:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"{self.name} {self.surname}"

    def __eq__(self, other):
        return self.name == other.name and self.surname == other.surname

    def introduce(self):
        print(f"Cześć, nazywam się {self}")

person1 = Person("Krzysztof", "Pijor")
person1.introduce()

# 4)	Przeczytaj czym cechuje się magiczna metoda __init__() oraz __new__(). Dowiedz się jakie są różnice między nimi. Rozszerz klasę Dog o metodę magiczną __init__(),
#       która pozowli na dynamiczne nadanie imienia, gatunku i wieku psa.
print(f"\nZadanie {zadanie}\n")
zadanie += 1

print("__init__ inicjazuje nowo utworzony obiekt, __new__ tworzy nowy obiekt i zwraca go, __new__ wywołuje się przed __init__ w momencie tworzenia obiektu, jest statyczną metodą gdzie __init__ jest instancją obiektu")

# 5)	Przeczytaj czym cechuje się magiczna metoda __str__() oraz __repr_(). Jakie są róźnice między nimi. Rozszerze klasę Person o metody magiczne __str__() oraz __repr_()
print(f"\nZadanie {zadanie}\n")
zadanie += 1

print("__str__ i __repr__ reprezentują obiekt jako tekst, __str__ ma być bardziej czytelne i wywołane będzie przez print(), a __repr__ techniczne, można wywołać podając sam obiekt")

# 6)	Stwórz klasę Book z atrybutami title, author, pages i metodą __len__() zwracającą liczbę stron książki.
print(f"\nZadanie {zadanie}\n")
zadanie += 1

class Book:
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"Książka: {self.title}\nAutor: {self.author}"

    def __len__(self):
        return self.pages

book1 = Book("Opisanie świata", "Marco Polo", 741)
print(book1, f"\nLiczba stron: {len(book1)}")

# 7)	Przeczytaj w jakim celu używa się metody magicznej __eq__(). Poszerz klasę Person  o __eq__(), która zwróci True jeśli wszystkie atrybuty klasy są sobie równe.
print(f"\nZadanie {zadanie}\n")
zadanie += 1

person2 = Person("Krzysztof", "Pijor")
person2.introduce()
print(f"Czy te dwie osoby {person1} oraz {person2} to te same osoby?: {person1 == person2}")

person3 = Person("Tomasz", "Pijor")
person3.introduce()
print(f"Czy te dwie osoby {person1} oraz {person3} to te same osoby?: {person1 == person3}")

# 8)	Stwórz klasę Animal na wzór klasy Dog z pierwszego zadania, a następnie klasy Cat i Dog, które dziedziczą po Animal. Celem zadania jest wyświetlenie danych o zwierzętach oraz wywołanie adekwatnej metody make_sound()
print(f"\nZadanie {zadanie}\n")
zadanie += 1

class Cat(Animal):
    def __init__(self, name: str, numer_of_legs: int, breed: str, age: int):
        super().__init__(name, numer_of_legs, breed, age)

    def make_sound(self):
        print("Miau miau")

cat1 = Cat("Duncan", 4, "Devon rex", 8)
print(cat1)
cat1.make_sound()

# 9)	Stwórz klasę Shape, oraz klasy dziedziczące Circle, Square i Triangle, z odpowiednią metodą calculate_area().
print(f"\nZadanie {zadanie}\n")
zadanie += 1

class Shape:
    def __init__(self, a):
        self.a = a

    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, a):
        super().__init__(a)

    def __str__(self):
        return f"Koło o promieniu {self.a}"

    def calculate_area(self):
        return 3.14 * self.a ** 2


class Square(Shape):
    def __init__(self, a):
        super().__init__(a)

    def __str__(self):
        return f"Kwadrat o bokach {self.a}"

    def calculate_area(self):
        return self.a ** 2


class Triangle(Shape):
    def __init__(self, a, h):
        super().__init__(a)
        self.h = h

    def __str__(self):
        return f"Trójkąt o boku {self.a} oraz wysokości {self.h}"

    def calculate_area(self):
        return 0.5 * self.a * self.h


circle1 = Circle(10)
square1 = Square(10)
triangle1 = Triangle(10, 5)
print(circle1, f"pole wynosi: {circle1.calculate_area()}", sep=' ')
print(square1, f"pole wynosi: {square1.calculate_area()}", sep=' ')
print(triangle1, f"pole wynosi: {triangle1.calculate_area()}", sep=' ')

# 10)	Stwórz klasę Mother, Father z atrybutem eye_color (mają różne kolory oczu) i metodą __str__() wyświetlającą ten kolor. Następnie utwórz klasę Child, która będzie dziedziczyć kolor oczu po rodzicach.
# Sprawdź z którego rodzica dziecko dziedziczy kolor oczu, potestuj co zmienić w dziedziczeniu, aby kolor oczu był taki jak u drugiego z rodziców.
print(f"\nZadanie {zadanie}\n")
zadanie += 1

class Human:
    def __init__(self, eye_color: str):
        self.eye_color = eye_color

    def __str__(self):
        return f"{self.eye_color}"

class Mother(Human):
    def __init__(self, eye_color):
        super().__init__(eye_color)

    def show(self):
        print("Zadanie 21, wywołanie metody z klasy rodzica")

class Father(Human):
    def __init__(self, eye_color):
        super().__init__(eye_color)

class Child(Mother):
    def __init__(self, eye_color):
        super().__init__(eye_color)

mother1 = Mother("niebieskie")
father1 = Father("brązowe")
child1 = Child(mother1)
print(f"Kolor oczu matki: {mother1}, ojca: {father1}, dziecko odziedziczyło po matce i ma kolor: {child1}")

# 11)	Utwórz klasę PersonChild(), która będzie dziedziczyć po Person z zadania 7). Przeciąż metodę magiczną __eq__() tak aby sprawdzała tylko i wyłącznie imię danej osoby.
print(f"\nZadanie {zadanie}\n")
zadanie += 1

class PersonChild(Person):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __eq__(self, other):
        return self.name == other.name

    #   tutaj się zastanawiam, czy to MRO (method resolution order) sprawia, że jeśli w taki sposób przeciąże __str__ to sprawi, że będzie to lepiej zoptymalizowane, czy powinienem coś takiego tutaj zrobić i przeciążać __str__?
    def __str__(self):
        return super().__str__()

personChild1 = PersonChild("Krzysztof", "Pijor")
personChild2 = PersonChild("Tomasz", "Pijor")
personChild3 = PersonChild("Krzysztof", "Pijor")
print(f"Czy te dwie osoby {personChild1} oraz {personChild2} mają tak samo na imię?: {personChild1 == personChild2}")
print(f"Czy te dwie osoby {personChild1} oraz {personChild3} mają tak samo na imię?: {personChild1 == personChild3}")

# 12)	Utwórz obiekty Person(„Roberto”, „Alwaro”) oraz PersonChild(„Roberto”, „Bambaro”), a następnie sprawdź co zwórci porównanie tych obiektów Person == PersonChild oraz PersonChild  == Person. Zagłąb i wyjaśnij to zjawisko .
print(f"\nZadanie {zadanie}\n")
zadanie += 1

person4 = Person("Roberto", "Alwaro")
personChild4 = PersonChild("Roberto", "Bambaro")
print(f"{person4} vs {personChild4} = {person4 == personChild4}")
print(f"{personChild4} vs {person4} = {personChild4 == person4}")
"""
Przed napisaniem tego wydawało mi się, że będzie to działać na zasadzie, która klasa została pierwsza użyta w tym porównaniu i wtedy będzie wykorzystana metoda __eq__ z danej klasy dla całego porównania i wyniki będą kolejno False, True
Jednak wyniki wskazują co innego, wydaje mi się w takim razie, że szuka wspólnego mianownika w każdym przypadku, jeśli są to klasy po sobie dziedziczące i wykorzystuje wtedy zawsze przeciążoną metodę __eq__ przy porównaniu obiektów tych klas
"""

# 13)	Stwórz klasę BankAccount i ukryj(protected lub private) w niej atrybut balance. Dodaj metody get_balance() i set_balance().
print(f"\nZadanie {zadanie}\n")
zadanie += 1

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def __str__(self):
        return f"{self.__balance}"

    def get_balance(self):
        return self.__balance

    def set_balance(self, value):
        self.__balance = value

    def czy_ujemny_balans(self):
        if self.__balance < 0:
            print(f"Uwaga, obecny balans jest ujemny")

    def show(self):
        print(f"Obecny balans wynosi: {self.__balance}")

bankAccount1 = BankAccount(1000)
bankAccount1.show()

# 14)	Dodaj do klasy BankAccount, sprawdzanie czy balans jest ujemny, jeśli tak, to wypisz ostrzeżenie dla użytkownika o ujemnym balansie.
print(f"\nZadanie {zadanie}\n")
zadanie += 1

bankAccount1.set_balance(-1)
bankAccount1.czy_ujemny_balans()

# 15)	Stwórz klasę RivalBankAccount i zaimplementuj w niej atrybut balance poprzez dekorator @property (sprawdź i wypisz różnicę pomiędzy tym rozwiązaniem a tym z zadania 13)
print(f"\nZadanie {zadanie}\n")
zadanie += 1

class RivalBankAccount:
    def __init__(self, balance):
        self._balance = balance

    def __str__(self):
        return f"{self._balance}"

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value

    def czy_ujemny_balans(self):
        if self._balance < 0:
            print(f"Uwaga, obecny balans jest ujemny")

    def show(self):
        print(f"Obecny balans wynosi: {self._balance}")

bankAccount2 = RivalBankAccount(10000)
bankAccount2.show()
bankAccount2.balance = -1
bankAccount2.czy_ujemny_balans()

# @property pozwala nam korzystać z metod jak z atrybutu, jest bardziej czytelny zapis

# 16)	Napisz klasę Temperature zaimplementuj celsius i fahrenheit jako właściwości (z konwersją).
print(f"\nZadanie {zadanie}\n")
zadanie += 1

class Temperature:
    #  nie jestem pewien czy dobrze zrozumiałem zamysł tego zadania i zrobiłem to klasycznie przez inicjalizację obiektu sprawdzając w jakim formacie go podamy przy tworzeniu
    def __init__(self, value: int, type: str):
        if type.capitalize() == "C" or type.capitalize() == "F":
            self.type = type.capitalize()
            self.value = value
        else:
            print("Podałeś zły typ, obiekt zostanie usunięty")
            del self

    def __str__(self):
        return f"{self.value}{self.type}"

    def changeType(self):
        if self.type == "C":
            self.type = "F"
            self.value = 1.8 * self.value + 32
        else:
            self.type = "C"
            self.value = 5 / 9 * (self.value - 32)
        return self

temp1 = Temperature(20, "c")
print(f"Obecnie mamy na dworze temperaturę wynoszącą: {temp1} / {temp1.changeType()}")
temp2 = Temperature(20, "a")
# print(f"Obecnie mamy na dworze temperaturę wynoszącą: {temp2} / {temp2.changeType()}")            # error, przez źle podany parametr typu obiekt temp2 został od razu usunięty

# 17)	W jaki sposób możemy usunąć z klasy property oraz cały obiekt klasy?
print(f"\nZadanie {zadanie}\n")
zadanie += 1

"""
cały obiekt klasy możemy usunąć przez instrukcję del obiekt, tak jak to zrobiłem w poprzednim zadaniu w przypadku podaniu złego typu
żeby usunąć z klasy property należy zrobić 
@abc.deleter
def abc(self):
    del self._abc
    
a żeby go wywołać:
obj = Klasa()
del obj.abc
"""

# 18)	Jak utworzyć klasę bez implementacji? (chodzi o słowo kluczowe)
print(f"\nZadanie {zadanie}\n")
zadanie += 1

class Pusta:
    pass
pusta_klasa = Pusta()
print(type(pusta_klasa))

# 19)	Jeśli w powyższych zadaniach korzystając z __init__, używałeś słowa kluczowego self, co się stanie, jeśli je zmienisz? Np. na selfie
print(f"\nZadanie {zadanie}\n")
zadanie += 1

class Selfie:
    def __init__(selfie, a):
        selfie.a = a

    def __str__(selfie):
        return f"{selfie}"

    def __del__(selfie):
        del selfie

    def show(selfie):
        print(f"To jest {selfie.a} selfie")

selfie = Selfie(1)
selfie.show()
del selfie
# w definicji słowa kluczowego "selfie" jest opisane, że zazwyczaj nazywa się self, ale poza tym działa tak samo, odnosi się do siebie

# 20)	Czy w klasie bez __init__() można dalej używać słowa kluczowego self?
print(f"\nZadanie {zadanie}\n")
zadanie += 1

class Tmp:
    def show(self, name):
        self.name = name
        print(f"{self.name} jest obiektem typu Tmp bez metody magicznej __init__(). Można dalej używać słowa kluczowego self")

tmp = Tmp()
tmp.show("tmp")

# 21)	Zakładając, że mamy klasę rodzica i dziecka czy używając obiektu dziecka możemy wywołać metodę rodzica? Jeśli tak, to w jaki sposób?
print(f"\nZadanie {zadanie}\n")
zadanie += 1

child1.show()
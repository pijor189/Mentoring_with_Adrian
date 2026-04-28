class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        self.up = None
        self.mother = None
        self.father = None

    def __str__(self):
        return f"{self.name} {self.surname} Age: {self.age}"

    def level(self):
        if not self.up:
            self.level = 0
        else:
            self.level = self.up.level + 1
        return self.level

    def append(self, person):
        if person.name[-1] == 'a' and not self.mother:
            self.mother = person
            self.mother.up = self
        elif person.name[-1] != 'a' and not self.father:
            self.father = person
            self.father.up = self
        else:
            print("Bad parent")

def show(person: Person):
    if not person:
        return
    print("\t" * person.level(), "|-", person)
    show(person.mother)
    show(person.father)


krzychu = Person("Krzysztof", "Pijor", 30)
ania = Person("Anna", "Pijor", 52)
tomek = Person("Tomasz", "Pijor", 53)
helena = Person("Helena", "Kot", 80)
janek = Person("Jan", "Kot", 82)
jadzia = Person("Jadwiga", "Pijor", 78)
leszek = Person("Leszek", "Pijor", 42)
tomek.append(jadzia)
tomek.append(leszek)
krzychu.append(ania)
krzychu.append(tomek)
ania.append(helena)
ania.append(janek)

show(krzychu)
"""
Zadania z pliku Python Tasks wyjątki i algorytmy 1 - dalsza część dotycząca list
https://eduinf.waw.pl/inf/alg/001_search/0084.php
"""
exercise = 13
"""
13)	Zaimplementuj listę jednokierunkową dla liter „A”, „B”, „C”. Atrybutami są:
•	value wskazujące wartość danego obiektu.
•	next wskazującą następny obiekt klasy, None oznacza koniec listy. 
Zaimplementuj metody:
•	append(value) – dodaje na koniec nową instancję obiektu.
•	find(value) – zwraca pierwszy obiekt z daną wartością.
•	delete(value) – usuwa pierwszy element z daną wartością.
•	__len__() – liczba elementów w Twojej liście.
•	__iter__() i __next__() – do iterowania przez elementy (Iterator) # do przeczytania
•	__str__() – ładna prezentacja wartości listy, np. „A -> B -> C”
•	reverse() – odwróć kolejność listy
"""
print(f"Exercise {exercise}")
exercise += 1

class EmptyListError(Exception):
    pass

class ValueNotFoundError(Exception):
    pass

class Element:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class OneLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        elem = Element(value)
        if not self.head:
            self.head = elem
            return
        current_elem = self.head
        while current_elem.next:
            current_elem = current_elem.next
        current_elem.next = elem

    def find(self, value):
        current_elem = self.head
        while current_elem:
            if current_elem.value == value:
                return current_elem
            current_elem = current_elem.next
        return None

    def delete(self, value):
        if not self.head:
            raise EmptyListError("Pusta lista")
        current_elem = self.head
        prev_elem = None
        while current_elem:
            if current_elem.value == value:
                if prev_elem:
                    prev_elem.next = current_elem.next
                else:
                    self.head = current_elem.next
                return
            prev_elem = current_elem
            current_elem = current_elem.next
        else:
            raise ValueNotFoundError(f"Nie ma takiej wartości: {value}")

    def __len__(self):
        count = 0
        current_elem = self.head
        while current_elem:
            count += 1
            current_elem = current_elem.next
        return count

    def __iter__(self):
        self.iter_elem = self.head
        return self

    def __next__(self):
        if not self.iter_elem:
            raise StopIteration
        value = self.iter_elem.value
        self.iter_elem = self.iter_elem.next
        return value

    def __str__(self):
        values = []
        current_elem = self.head
        while current_elem:
            values.append(str(current_elem.value))
            current_elem = current_elem.next
        return " -> ".join(values)

    def reverse(self):
        prev_elem = None
        current_elem = self.head
        while current_elem:
            next_elem = current_elem.next
            current_elem.next = prev_elem
            prev_elem = current_elem
            current_elem = next_elem
        self.head = prev_elem

try:
    # tworzymy listę
    one_linked_list = OneLinkedList()
    print(one_linked_list.head)
    # one_way_list.delete("A")

    one_linked_list.append("A")
    one_linked_list.append("B")
    one_linked_list.append("C")
    print(one_linked_list)
    print(len(one_linked_list))
    b = one_linked_list.find("B")
    print(b)
    one_linked_list.reverse()
    print(one_linked_list)
    one_linked_list.delete("B")
    # one_way_list.delete("B")
    print(one_linked_list)
    print(len(one_linked_list))
    one_linked_list.reverse()
    one_linked_list.append("B")
    one_linked_list.append("D")
    print(one_linked_list)
    print(len(one_linked_list))

except EmptyListError as e:
    print(f"Próba usunięcia elementu z pustej listy: {e}")
except ValueNotFoundError as e:
    print(f"Próba usunięcia nieistniejącego elementu: {e}")

"""
14)	Rozszerz listę jednokierunkową o wyjątki: 
•	EmptyListError – przy próbie usunięcia z pustej listy
•	ValueNotFoundError – przy próbie usunięcia nieistniejącego elementu
"""
print(f"Exercise {exercise}")
exercise += 1

# 15)	Rozszerz listę o drugi kierunek – prev. Musi on być uzupełniany tak samo jak i next.
print(f"Exercise {exercise}")
exercise += 1

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        elem = Element(value)
        if not self.head:
            self.head = elem
            self.tail = elem
            elem.next = elem
            elem.prev = elem
            return
        elem.prev = self.tail
        elem.next = self.head
        self.tail.next = elem
        self.head.prev = elem
        self.tail = elem

    def find(self, value):
        if not self.head:
            return None

        current_elem = self.head
        while True:
            if current_elem.value == value:
                return current_elem
            current_elem = current_elem.next
            if current_elem == self.head:
                break
        return None

    def delete(self, value):
        if not self.head:
            raise EmptyListError("Pusta lista")

        current_elem = self.head
        while True:
            if current_elem.value == value:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                    return

                current_elem.prev.next = current_elem.next
                current_elem.next.prev = current_elem.prev

                if current_elem == self.head:
                    self.head = current_elem.next
                if current_elem == self.tail:
                    self.tail = current_elem.prev
                return

            current_elem = current_elem.next
            if current_elem == self.head:
                break

        raise ValueNotFoundError(f"Value not found: {value}")

    def __len__(self):
        if not self.head:
            return 0

        count = 0
        current_elem = self.head
        while True:
            count += 1
            current_elem = current_elem.next
            if current_elem == self.head:
                break
        return count

    def __iter__(self):
        self.iter_elem = self.head
        self.started = False
        return self

    def __next__(self):
        if not self.head:
            raise StopIteration

        if self.started and self.iter_elem == self.head:
            raise StopIteration

        self.started = True
        value = self.iter_elem.value
        self.iter_elem = self.iter_elem.next
        return value

    def __str__(self):
        if not self.head:
            return "Empty list"

        values = []
        current_elem = self.head
        while True:
            values.append(str(current_elem.value))
            current_elem = current_elem.next
            if current_elem == self.head:
                break
        return " -> ".join(values)

    def reverse(self):
        if not self.head or self.head == self.tail:
            return

        current = self.head
        while True:
            current.next, current.prev = current.prev, current.next
            current = current.prev
            if current == self.head:
                break
        self.head, self.tail = self.tail, self.head


try:
    double_linked_list = DoubleLinkedList()
    print(double_linked_list)

    double_linked_list.append("A")
    double_linked_list.append("B")
    double_linked_list.append("C")
    print(double_linked_list)

    double_linked_list.append("D")
    double_linked_list.delete("B")
    double_linked_list.append("E")
    print(double_linked_list)

    double_linked_list.reverse()
    print(double_linked_list)

except EmptyListError as e:
    print(f"Próba usunięcia elementu z pustej listy: {e}")
except ValueNotFoundError as e:
    print(f"Próba usunięcia nieistniejącego elementu: {e}")

# 16)	Zadanie z gwiazdką*. Dodaj atrybuty head i tail, które będą ustawiane na element początku i końca listy. Podepnij prev pierwszego elementu tak, aby wskazywał na ostatni element listy, a next ostatniego na pierwszy. W ten sposób uzyskasz listę zapętloną dwukierunkową.
print(f"Exercise {exercise}")
exercise += 1

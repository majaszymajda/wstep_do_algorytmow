from random import randint
import time
import uuid


# tworzenie klasy reperzetujacej wezel listy
class Node():

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


# tworzenie klasy reprezentującej całą listę
class LinkedList():

    def __init__(self):
        self.start_node = None

    def insert(self, data):
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return
        n = self.start_node
        while n.next_node is not None:
            n = n.next_node
        n.next_node = new_node

    def remove(self, key):
        temp = self.start_node
        if (temp is not None):
            if (temp.data._id == key._id):
                self.start_node = temp.next_node
                temp = None
                return
        while(temp is not None):
            if temp.data._id == key._id:
                break
            prev = temp
            temp = temp.next_node

        if(temp is None):
            return

        prev.next_node = temp.next_node
        temp = None

    def size(self):
        counter = 0
        if self.start_node is None:
            return counter
        else:
            n = self.start_node
            while n is not None:
                counter += 1
                n = n.next_node
        return counter

    def __iter__(self):
        self.current_node = self.start_node
        return self

    def __next__(self):
        if self.current_node is None:
            raise StopIteration
        else:
            result = self.current_node.data
            self.current_node = self.current_node.next_node
            return result


# klasa klientow "budowe" listy klienta
class Klient:

    typy = ['A', 'B', 'C']
    typ: str
    zajetosc: int

    def __init__(self):
        self._id = uuid.uuid1()
        self.typ = self.typy[randint(0, 2)]
        self.zajetosc = randint(1, 10)

    def __str__(self):
        return f'Klient typ: {self.typ} - zajętość - {self.zajetosc}'


# klasa opisujaca "budowe" listy okienka
class Okienko:

    nr: int
    typ: str
    zajetosc: int

    _counter = 1

    def __init__(self, typ):
        self.nr = self._counter
        Okienko._counter = self._counter + 1
        self.typ = typ
        self.zajetosc = 0

    def __str__(self):
        return f'Okienko nr. {self.nr} - {self.typ} - zajętość - {self.zajetosc}'

    def czy_wolne(self):
        return self.zajetosc == 0

    def dodaj_klienta(self, klient):
        self.zajetosc = klient.zajetosc

    def zmniejsz_zajetosc(self):
        if (self.zajetosc > 0):
            self.zajetosc = self.zajetosc - 1


# zad 1.1 - przypisanie okienku jego typu:  A, B, C lub E
okienka = [
    Okienko('A'),
    Okienko('A'),
    Okienko('A'),
    Okienko('B'),
    Okienko('B'),
    Okienko('B'),
    Okienko('C'),
    Okienko('C'),
    Okienko('C'),
    Okienko('E')
]


# sprawdzanie wolnego okienka dla klienta danego typu
def znajdz_wolne(klient: Klient):
    typ = klient.typ
    for okienko in okienka:
        if (okienko.typ == typ or okienko.typ == 'E') and okienko.czy_wolne():
            return okienko
    return None


# redukcja zajetosci klienta
def zmniejsz_zajetosci():
    for okienko in okienka:
        okienko.zmniejsz_zajetosc()


# zad 1.2 - stworzenie listy klientow
lista = LinkedList()

for okienko in okienka:
    print(okienko)

for i in range(30):
    lista.insert(Klient())

for i in lista:
    print(i)

print(lista.size())

# zad 1.3

for i in lista:
    print(i)
print(lista.size())

counter = 0
while True:
    print('ilosc klientow oczekujacych: ', lista.size())
    if lista.size() == 0:
        break
    counter += 1
    clients_to_delete = []
    for klient in lista:
        okienko = znajdz_wolne(klient)
        if okienko:
            clients_to_delete.append(klient)
            okienko.dodaj_klienta(klient)
    zmniejsz_zajetosci()
    for client in clients_to_delete:
        lista.remove(client)
    for okienko in okienka:
        print(okienko)
    time.sleep(2)
    print(f'ilosc osob obsluzonych:  {30-lista.size()}')

# zad 1.4 wyswietlenie "czasu obslugi" w iteracjach 
print('Ilosc iteracji', counter)

# usprawnieniem jakie mozna wprowadzic jest posortowanie listy klientow
# pod wzgledem typu A, B, C

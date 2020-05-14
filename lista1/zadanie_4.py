import numpy as np


# sprawdzenie czy podany produkt istnieje
def produkt_istnieje(id_produktu, produkty):
    for produkt in produkty:
        if id_produktu == produkt[0]:
            return produkt
    return None


#  sprawdzenie czy nie kupujemy "połowy produktu na sztuki",
#  val to cena jednostkowa jezeli produkt[2]= true
#  to jest to produkt jest w sztukach
#  czyli cena nie moze byc zmiennoprzecinkowa
def produkt_ok(produkt: list):
    val = produkt[1]
    if produkt[2] == True and int(val) != float(val):
        return False
    return True


# macierz transakcji
transakcje = np.array([
    [1, 4, 6],
    [1, 6, 2],
    [1, 5, 1],
    [2, 5, 4],
    [1, 3, 2],
    [2, 1, None],
    [2, 404, None],
    [2, 409, None]
])
# macierz [nr towaru, cena jednost, inf czy sztuki czy wag]
# true = na sztuki
# false = na wage

produkty = np.array([
    [4, 7, True],
    [6, 3, True],
    [5, 2, True],
    [3, 3.5555555, True],
    [1, 30, False]
])

zle_produkty = []
for i, produkt in enumerate(produkty):      
    # enumerate zwraca obiekt wyliczenia
    try:
        if not produkt_ok(produkt):
            zle_produkty.append(i)
            raise Exception(f'produkt id:{produkt[0]+1} nie jest liczba calk')
    except Exception as e:
        print(e)
# usuwanie zlych produktow
for index in zle_produkty:
    produkty = np.delete(produkty, index, 0)


# ppdkt1
for transakcja in transakcje:
    try:
        if produkt_istnieje(transakcja[1], produkty) is None:
            raise Exception(f'produkt o id:{transakcja[1]} nie ma w bazie')
    except Exception as e:
        print(e)

print('\n')
# ppdkt2
# funkcja do liczenia ceny paragonu


def print_sum(klient_id: int):
    licznik = 0
    for transakcja in transakcje:
        if transakcja[0] != klient_id:
            continue
        produkt = produkt_istnieje(transakcja[1], produkty)
        if produkt is not None:
            if produkt[2] == True:
                licznik += (transakcja[2] * produkt[1])
            else:
                licznik += produkt[1]
    print(f'Klient {klient_id}: {licznik}')


print_sum(1)
print_sum(2)

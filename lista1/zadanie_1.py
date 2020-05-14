import numpy as np
import random


# wstep
oceny = [2.0, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5]
studenci = int(input('Podaj liczbę studentow: '))
przedmioty = int(input('Podaj liczbę przedmiotów:'))

# print(f'Liczba studentów {studenci} ')
# print(f'Liczba przedmiotow {przedmioty} ')

macierz_ocenowa = np.zeros((studenci, przedmioty))

for i in range(studenci):
    for j in range(przedmioty):
        macierz_ocenowa[i][j] = random.choice(oceny)

print(macierz_ocenowa)

# ppkt1

niezaliczone = int(input('Podaj liczbę niezaliczonych przedmiotow: '))
licznik_uczniow = 0

for i in range(studenci):
    licznik_ocen = 0
    for j in range(przedmioty):

        if macierz_ocenowa[i][j] < 3:
            licznik_ocen += 1

    if licznik_ocen >= niezaliczone:
        licznik_uczniow += 1

print(f'Liczba studentow, ktora nie zaliczyła conajmniej {niezaliczone}')
print(f' przedmiotow to: {licznik_uczniow}')
# ppdkt2

najwyzsza_srednia = 0
student_najlepszy = 0
najnizsza_srednia = 6 
student_najgorszy = 0

for i in range(studenci):
    suma = 0
    srednia_studenta = 0

    for j in range(przedmioty):
        suma += macierz_ocenowa[i][j]
        # print(suma)
        # print("  ")

    srednia_studenta = suma/przedmioty

    print(f'stud {i+1} ma srednia: {round(srednia_studenta,2)}')

    if srednia_studenta > najwyzsza_srednia:
        najwyzsza_srednia = srednia_studenta
        student_najlepszy = i

    if srednia_studenta < najnizsza_srednia:
        najnizsza_srednia = srednia_studenta
        student_najgorszy = i

print(f'Student z najwyższa srednia to {student_najlepszy+1}')
print(f'A student z najgorsza srednia to  {student_najgorszy+1}')

# ppdkt3

najwyzsza_ocena = macierz_ocenowa.max()

print(macierz_ocenowa)
osoba_z_najwieksza_liczba_ocen = 0
najwieksza_ilosc_max_oceny = 0

for i in range(studenci):
    liczba_maxy_ocen = 0
    for j in range(przedmioty):
        if najwyzsza_ocena == macierz_ocenowa[i][j]:
            liczba_maxy_ocen += 1
    if najwieksza_ilosc_max_oceny < liczba_maxy_ocen:
        najwieksza_ilosc_max_oceny = liczba_maxy_ocen
        osoba_z_najwieksza_liczba_ocen = i


print(f'Student z najwieksza iloscia najwyzszej oceny,czyli {najwyzsza_ocena}')
print(f' to osoba o numerze: {osoba_z_najwieksza_liczba_ocen+1}')

# ppdkt4

macierz_transponowana = np.transpose(macierz_ocenowa)
for i in range(przedmioty):
    hist, bin_edges = np.histogram(macierz_transponowana[i], bins=[2, 3, 4, 5, 6 ])
    print(f'Histogram przedmiotu {i}: {hist}')


# ppdkt5
lista_studentow = []
for i in range(studenci):
    if np.average(macierz_ocenowa[i]) > 4.0:
        lista_studentow.append(i+1)
print(f'Studenci ze średnią powyżej 4.0: {lista_studentow}')

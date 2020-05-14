import numpy as np

a = int(input('Podaj rozmiar macierzy symetrycznej: '))

macierz_1 = np.random.randint(10, size=(a, a))
macierz_2 = np.random.randint(10, size=(a, a))

print(f'Pierwsza macierz:\n{macierz_1}')
print(f'Druga macierz:\n{macierz_2}')

odleglosc = 0
for i in range(a):
    for j in range(a):
        odleglosc = odleglosc + abs(macierz_1[i, j] - macierz_2[i, j])

print(f'Odległość symetryczna wynosi: {odleglosc}')

import numpy as np

# macierz_p = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 1, 2, 3]])
macierz = np.random.randint(1, 10, size=(4, 4))
print(f'Pierwotna macierz:\n{macierz}')
wiersze, kolumny = macierz.shape

for i in range(wiersze):
    for j in range(i + 1, kolumny):     # poruszam sie schodkowo po macierzy
        try:
            if macierz[i, i] == 0:
                continue    # pominiecie danej wartosci i przejscie dalej
            dzielnik = macierz[j, i] / macierz[i, i]
            # print(f'dzielnik to: {dzielnik}')
            for k in range(kolumny):
                macierz[j, k] = macierz[j, k] - (macierz[i, k] * dzielnik)
                # print(f'Macierz z kolejki {j}, {k}:\n{macierz}')
        except ValueError as e:         # wykluczam probem dzielenia przez zero
            print(f'Wystąpił problem: {e}')
print(f'Wynik:\n{macierz}')

import random


class Graf():
    def __init__(self, ilosc_wierzcholkow):
        self.ilosc_wierzcholkow = ilosc_wierzcholkow
        self.macierz_sasiedztwa = []
        for i in range(ilosc_wierzcholkow):
            self.macierz_sasiedztwa.append([])
            for j in range(ilosc_wierzcholkow):
                self.macierz_sasiedztwa[i].append(0)
        # print(self.macierz_sasiedztwa)

    def wypisanie_macierzy(self):
        for i in range(-1, self.ilosc_wierzcholkow):
            for j in range(-1, self.ilosc_wierzcholkow):
                if i == -1 and j == -1:
                    print("X", end=" ")
                elif (j == -1):
                    print(i, end=" ")
                elif (i == -1):
                    print(j, end=" ")
                else:
                    print(self.macierz_sasiedztwa[i][j], end=" ")
            print()

    def dodaj_krawedz(self, wierzcholek1, wierzcholek2):
        self.macierz_sasiedztwa[wierzcholek1][wierzcholek2] = 1
        self.macierz_sasiedztwa[wierzcholek2][wierzcholek1] = 1

    def usun_krawedz(self, wierzcholek1, wierzcholek2):
        self.macierz_sasiedztwa[wierzcholek1][wierzcholek2] = 0
        self.macierz_sasiedztwa[wierzcholek2][wierzcholek1] = 0

    def sprawdz_krawedz(self, wierzcholek1, wierzcholek2):
        # skoro istnieje od w1 do w2 to istnieje tez od w2 do w1
        return self.macierz_sasiedztwa[wierzcholek1, wierzcholek2] == 1

    def sasiedzi(self, wierzcholek):
        sasiady = []
        for i in range(self.ilosc_wierzcholkow):
            if self.macierz_sasiedztwa[wierzcholek][i] == 1:
                sasiady.append(i)
        print(sasiady)


def losowanie_grafu(graf, ilosc_krawedzi):
    for i in range(ilosc_krawedzi):
        wierzcholek1 = random.randint(0, graf.ilosc_wierzcholkow-1)
        wierzcholek2 = random.randint(0, graf.ilosc_wierzcholkow-1)
        graf.dodaj_krawedz(wierzcholek1, wierzcholek2)
        print(wierzcholek1)
        print(wierzcholek2)


if __name__ == "__main__":
    input("numerujemy wierzcholki od 0!")
    ilosc_wierzcholkow = int(input("podaj ilosc wierzcholkow: "))
    grafy = Graf(ilosc_wierzcholkow)
    grafy.wypisanie_macierzy()
    grafy.dodaj_krawedz(1, 2)
    grafy.sasiedzi(1)
    grafy.wypisanie_macierzy()
    losowanie_grafu(grafy, 5)
    grafy.wypisanie_macierzy()

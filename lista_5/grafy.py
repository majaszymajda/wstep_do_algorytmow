import random


class Stos():
    def __init__(self):     # konstruktor
        self.stos = []

    def dodawanie(self, s):      # dodawanie elemetu
        self.stos.append(s)

    def pobranie(self):          # pobranie elementu
        return self.stos.pop(len(self.stos)-1)

    def wielkosc(self):         # ilosc elementu w stosie
        return len(self.stos)

    def czy_pusty(self):
        if len(self.stos) == 0:
            return True
        else:
            return False

    def rozszerzanie(self, lista):
        for e in lista:
            self.dodawanie(e)


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
        return sasiady

    def szukanie_spojnych_skladowych(self):
        spojne_skladowe = []
        stos = Stos()
        ilosc_spojnych_skladowych = 0
        odwiedzone_wierzcholki = [False] * self.ilosc_wierzcholkow
        while not all(odwiedzone_wierzcholki):
            for i in range(self.ilosc_wierzcholkow):
                if odwiedzone_wierzcholki[i] == False:
                    stos.dodawanie(i)
                    odwiedzone_wierzcholki[i] = True
                    break

            spojne_skladowe.append([])

            while not stos.czy_pusty():
                wierzcholek = stos.pobranie()
                lista_sasiadow = self.sasiedzi(wierzcholek)
                if lista_sasiadow is not None:
                    for s in lista_sasiadow:
                        if not odwiedzone_wierzcholki[s]:
                            stos.dodawanie(s)
                            odwiedzone_wierzcholki[s] = True
                spojne_skladowe[ilosc_spojnych_skladowych].append(wierzcholek)

            ilosc_spojnych_skladowych += 1
        return spojne_skladowe


def losowanie_grafu(graf, ilosc_krawedzi):
    for i in range(ilosc_krawedzi):
        wierzcholek1 = random.randint(0, graf.ilosc_wierzcholkow-1)
        wierzcholek2 = random.randint(0, graf.ilosc_wierzcholkow-1)
        graf.dodaj_krawedz(wierzcholek1, wierzcholek2)


if __name__ == "__main__":
    # print("numerujemy wierzcholki od 0!")
    # ilosc_wierzcholkow = int(input("podaj ilosc wierzcholkow: "))
    ilosc_wierzcholkow = 5
    grafy = Graf(ilosc_wierzcholkow)
    # grafy.wypisanie_macierzy()
    # grafy.dodaj_krawedz(1, 2)
    # grafy.sasiedzi(1)
    # grafy.wypisanie_macierzy()
    losowanie_grafu(grafy, 3)
    # krawedzie = [
    #     (0, 1), (1, 2), (1, 3), (2, 3),
    #     (4, 5), (5, 6), (6, 4),
    #     (7, 8)]
    # for w1, w2 in krawedzie:
    #     grafy.dodaj_krawedz(w1, w2)

    grafy.wypisanie_macierzy()
    print(grafy.szukanie_spojnych_skladowych())

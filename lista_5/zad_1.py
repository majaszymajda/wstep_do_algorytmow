from grafy import Graf, losowanie_grafu

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

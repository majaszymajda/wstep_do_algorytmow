from grafy import Graf, losowanie_grafu

if __name__ == "__main__":
    print("numerujemy wierzcholki od 0!")
    ilosc_wierzcholkow = int(input("podaj ilosc wierzcholkow: "))
    grafy = Graf(ilosc_wierzcholkow)
    a = int(input("podaj ilosc krawedzi: "))
    losowanie_grafu(grafy, a)
    grafy.wypisanie_macierzy()
    print(grafy.szukanie_spojnych_skladowych())

from time import time
from random import randint
import copy
import numpy as np




# tablice na pomiary
bubble_sort_times1 = []
bubble_sort_times2 = []
bubble_sort_times3 = []


# funkcja do tworzenia listy
def tworzenie_rand_list(n):
    return [randint(1, 99) for x in range(n)]


#  sortowanie Babelkowe wersja 1
def bubble_sort1(L):
    start_time = time()
    for i in range(len(L)):
        for j in range(0, (len(L)-1)-i):
            if L[j] > L[j+1]:
                temp = L[j]
                L[j] = L[j+1]
                L[j+1] = temp
    # print("posortowana lista:", L)
    end_time = time()
    calculated_time = round(abs(start_time - end_time), 2)
    bubble_sort_times1.append(calculated_time)


#  sortowanie Babelkowe wersja 2
# jezeli nie dokonamy zadnej zamiany w ciagu calego przejscia
# to znaczy ze ciag juz jest posortowany
def bubble_sort2(L):
    start_time = time()
    for i in range(len(L)):
        czy_byla_zamiana = 0
        for j in range(0, (len(L)-1)-i):
            if L[j] > L[j+1]:
                temp = L[j]
                L[j] = L[j+1]
                L[j+1] = temp
                czy_byla_zamiana = 1
        if czy_byla_zamiana != 1:
            break

    end_time = time()
    calculated_time = round(abs(start_time - end_time), 2)
    bubble_sort_times2.append(calculated_time)


# sortowanie Babelkowe wersja 3
# naiwna wersja przechodzaca za kazdym razem cala tablice
def bubble_sort3(L):
    start_time = time()
    dlugosc_ciagu = len(L)
    for i in range(dlugosc_ciagu):
        for j in range(0, (len(L)-1)):
            if L[j] > L[j+1]:
                temp = L[j]
                L[j] = L[j+1]
                L[j+1] = temp

    end_time = time()
    # print("posortowana lista:", L)
    calculated_time = round(abs(start_time - end_time), 2)
    bubble_sort_times3.append(calculated_time)


# funkcja do wykowywania 10 sortowan na 10 rand listach
def podpunkt4(n):
    for i in range(0, 20):
        L = tworzenie_rand_list(n)
        L1 = copy.deepcopy(L)
        L2 = copy.deepcopy(L)
        bubble_sort1(L)
        bubble_sort2(L1)
        bubble_sort3(L2)


def main():
    n = randint(1000, 2000)
    podpunkt4(n)
    print('Kolejne czasy bubble sort: ', bubble_sort_times1)
    print('Kolejne czasy bubble sort w wersji 2: ', bubble_sort_times2)
    print('Kolejne czasy bubble sort w wersji 3: ', bubble_sort_times3)

    print('Sredni czas bubble sort: %.2f ' % np.average(bubble_sort_times1))
    print('Sredni czas bubble sort 2 : %.2f' % np.average(bubble_sort_times2))
    print('Sredni czas bubble sort 3 : %.2f' % np.average(bubble_sort_times3))


main()

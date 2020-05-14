import matplotlib.pyplot as plt
from time import time
from random import randint
# import numpy as np
import copy

tab_dl_ciagow = [10, 20, 30, 50, 100, 200, 500, 1000]

# tablice na pomiary
bubble_sort_times = []
insert_sort_times = []
select_sort_times = []


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
    bubble_sort_times.append(calculated_time)


# sortowanie przez wstawianie
def insert_sort(L):
    start_time = time()
    for i in range(len(L)):
        for j in range(0, i):
            if L[i] < L[j]:
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
    # print("posotowana lista: ", L)
    end_time = time()
    calculated_time = round(abs(start_time - end_time), 2)
    insert_sort_times.append(calculated_time)


# sortowanie przez wybor
def select_sort(L):
    start_time = time()
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if L[i] > L[j]:
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
    # print("posortowana lista: ", L2)
    end_time = time()
    calculated_time = round(abs(start_time - end_time), 2)
    select_sort_times.append(calculated_time)


# funkcja do wykowywania sortowania dla roznych dl ciagu
def podpunkt3():
    for i in range(0, len(tab_dl_ciagow)):
        n = tab_dl_ciagow[i]
        L = tworzenie_rand_list(n)
        L1 = copy.deepcopy(L)
        L2 = copy.deepcopy(L)
        bubble_sort1(L)
        insert_sort(L1)
        select_sort(L2)


def wykresy():
    podpunkt3()

    # print('Kolejne czasy bubble sort: ', bubble_sort_times)
    # print('Kolejne czasy insertion sort: ', insert_sort_times)
    # print('Kolejne czasy selection sort: ', select_sort_times)

    plt.plot(tab_dl_ciagow, bubble_sort_times)
    plt.plot(tab_dl_ciagow, insert_sort_times)
    plt.plot(tab_dl_ciagow, select_sort_times)
    plt.legend(('Bubble_sort', 'Insert_sort', 'Select_sort'))
    plt.xlabel('ilosc elementow w tablicy')
    plt.ylabel('czas')
    plt.title('Wykres ')
    plt.grid(True)
    plt.show()


def main():
    wykresy()


main()

from time import time
from random import randint
import numpy as np
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


# funkcja do wykowywania 10 sortowan na 10 rand listach
def podpunkt2(n):
    for i in range(0, 10):
        L = tworzenie_rand_list(n)
        L1 = copy.deepcopy(L)
        L2 = copy.deepcopy(L)
        bubble_sort1(L)
        insert_sort(L1)
        select_sort(L2)


def main():
    n = randint(100, 5000)
    podpunkt2(n)

    print('Kolejne czasy bubble sort: ', bubble_sort_times)
    print('Kolejne czasy insertion sort: ', insert_sort_times)
    print('Kolejne czasy selection sort: ', select_sort_times)

    print('Sredni czas bubble sort: %.2f ' % np.average(bubble_sort_times))
    print('Sredni czas insertion sort: %.2f' % np.average(insert_sort_times))
    print('Sredni czas selection sort: %.2f' % np.average(select_sort_times))
    print('Maksymalny czas bubble sort: ', np.max(bubble_sort_times))
    print('Maksymalny czas insertion sort: ', np.max(insert_sort_times))
    print('Maksymalny czas selection sort: ', np.max(select_sort_times))


main()

# Implementirati Insertion-sort algoritam, proveriti njegovu funkcionalnost 
# i analizirati vreme izvršenja. Pseudokod algoritma je prikazan na slici 1 
# u PDFu.

import random
import time

def rand_list(min, max, num_of_el):
    list = random.sample(range(min, max), num_of_el)
    return list

def insertion_sort(niz):
    for j in range(1, len(niz)):
        key = niz[j]
        i = j - 1
        while i >= 0 and niz[i] > key:
            niz[i + 1] = niz[i]
            i = i - 1
        niz[i + 1] = key

if __name__ == "__main__":
    A = rand_list(0, 20, 10)
    print("Niz prije sortiranja:", A)

    start_time = time.perf_counter()
    insertion_sort(A)
    end_time = time.perf_counter() - start_time

    print("Slozen niz:", A)
    print("Vrijeme:", end_time)
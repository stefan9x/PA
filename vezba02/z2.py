# Implementirati Bubble sort algoritam, proveriti njegovu funkcionalnost i 
# analizirati vreme izvršenja.

import random
import time

def rand_list(min, max, num_of_el):
    list = random.sample(range(min, max), num_of_el)
    return list

def bubble_sort(niz):
    for i in range(0, len(niz)):
        for j in range(0, len(niz)-i-1):
            if niz[j] > niz[j + 1]:
                niz[j], niz[j + 1] = niz[j + 1], niz[j]
                               
if __name__ == "__main__":
    A = rand_list(0, 20, 10)
    
    print("Niz prije sortiranja:", A)

    start_time = time.perf_counter()
    bubble_sort(A)
    end_time = time.perf_counter() - start_time

    print("Slozen niz:", A)
    print("Vrijeme:", end_time)


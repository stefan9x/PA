import time
import random

def rand_list(min, max, num_of_el):
    list = random.sample(range(min, max), num_of_el)
    return list

def partition(A, pocetak, kraj):
    x = A[kraj]
    i = pocetak - 1
    for j in range(pocetak, kraj):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[kraj] = A[kraj], A[i + 1]
    return i + 1

def randomized_partition(A, pocetak, kraj):
    i = random.randint(pocetak, kraj)
    A[kraj], A[i] = A[i], A[kraj]
    return partition(A, pocetak, kraj)

def randomized_quicksort(A, pocetak, kraj):
    if pocetak < kraj:
        q = randomized_partition(A, pocetak, kraj)
        randomized_quicksort(A, pocetak, q - 1)
        randomized_quicksort(A, q + 1, kraj)

if __name__ == "__main__":

    A = rand_list(0, 20, 10)
    
    print("----Test-----")
    print("Niz:", A)
    randomized_quicksort(A, 0, len(A) - 1)
    print("Slozen niz:", A)
    print("-------------")
    
    A = rand_list(0, 2000, 1000)
    start_time = time.time()
    randomized_quicksort(A, 0, len(A) - 1)
    end_time = time.time() - start_time
    print("Vrijeme za",len(A),":", end_time)

    A = rand_list(0, 10000, 5000)
    start_time = time.time()
    randomized_quicksort(A, 0, len(A) - 1)
    end_time = time.time() - start_time
    print("Vrijeme za",len(A),":", end_time)

    A = rand_list(0, 100000, 50000)
    start_time = time.time()
    randomized_quicksort(A, 0, len(A) - 1)
    end_time = time.time() - start_time
    print("Vrijeme za",len(A),":", end_time)

    A = rand_list(0, 600000, 500000)
    start_time = time.time()
    randomized_quicksort(A, 0, len(A) - 1)
    end_time = time.time() - start_time
    print("Vrijeme za",len(A),":", end_time)
import random
import math
import time

def rand_list(min, max, num_of_el):
    list = random.sample(range(min, max), num_of_el)
    return list

def merge(A, pocetak, pilot, kraj, obrnuto=0):
    L_len = pilot - pocetak + 1
    R_len = kraj - pilot
    L, R = [], []

    for i in range(0, L_len):
        L.append(A[pocetak + i])
    for j in range(0, R_len):
        R.append(A[pilot + j + 1])

    i = 0
    j = 0

    if obrnuto == 0:
        L.append(math.inf)
        R.append(math.inf)

        for k in range(pocetak, kraj + 1):
            if L[i] <= R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
    else:
        L.append(-math.inf)
        R.append(-math.inf)

        for k in range(pocetak, kraj + 1):
            if L[i] >= R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1


# obrnuto == 0 - za rastuci(default ako nije unijeto nista)
# obrnuto != 0 - za opadajuci
def merge_sort(A, pocetak, kraj, obrnuto=0):
    if pocetak < kraj:
        pilot = (pocetak + kraj) // 2
        merge_sort(A, pocetak, pilot, obrnuto)
        merge_sort(A, pilot + 1, kraj, obrnuto)
        merge(A, pocetak, pilot, kraj, obrnuto)
		
if __name__ == "__main__":
    print("----Test-----")
    A = rand_list(0, 20, 10)
    print("Niz:", A)
    merge_sort(A, 0, len(A) - 1, 1)
    print("Slozen:", A)
    print("-------------")

    A = rand_list(0, 2000, 1000)
    start_time = time.time()
    merge_sort(A, 0, len(A) - 1)
    end_time = time.time() - start_time
    print("Vrijeme za",len(A),":", end_time)

    A = rand_list(0, 10000, 5000)
    start_time = time.time()
    merge_sort(A, 0, len(A) - 1)
    end_time = time.time() - start_time
    print("Vrijeme za",len(A),":", end_time)

    A = rand_list(0, 100000, 50000)
    start_time = time.time()
    merge_sort(A, 0, len(A) - 1)
    end_time = time.time() - start_time
    print("Vrijeme za",len(A),":", end_time)

    A = rand_list(0, 600000, 500000)
    start_time = time.time()
    merge_sort(A, 0, len(A) - 1)
    end_time = time.time() - start_time
    print("Vrijeme za",len(A),":", end_time)
    